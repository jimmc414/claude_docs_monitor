#!/bin/bash
# claude_loop.sh — Run Claude Code in a loop with structured exit criteria
#
# Uses --json-schema to get a machine-readable completion signal from Claude,
# and --resume to maintain session context across retries within each goal.
#
# Usage:
#   ./claude_loop.sh                     # run default goals
#   ./claude_loop.sh goals.txt           # one goal per line from file

set -euo pipefail

# --- Configuration ---
MAX_RETRIES=5          # max attempts per goal
MAX_TURNS=15           # max agentic turns per attempt
ALLOWED_TOOLS="Bash,Read,Edit,Glob,Grep"

# Schema forces Claude to return a structured verdict after each run
SCHEMA='{
  "type": "object",
  "properties": {
    "completed": {
      "type": "boolean",
      "description": "true if the goal is fully accomplished"
    },
    "summary": {
      "type": "string",
      "description": "brief description of what was done or what remains"
    }
  },
  "required": ["completed", "summary"]
}'

# --- Goals ---
if [ "${1:-}" != "" ] && [ -f "$1" ]; then
    mapfile -t GOALS < "$1"
else
    GOALS=(
        "Fix any failing tests in the test suite"
        "Add input validation to all public API endpoints"
    )
fi

# --- Main loop ---
total=${#GOALS[@]}
passed=0
failed=0

for i in "${!GOALS[@]}"; do
    goal="${GOALS[$i]}"
    goal_num=$((i + 1))
    echo ""
    echo "===[$goal_num/$total] $goal ==="

    session_id=""
    goal_done=false

    for attempt in $(seq 1 "$MAX_RETRIES"); do
        echo "  Attempt $attempt/$MAX_RETRIES ..."

        if [ -z "$session_id" ]; then
            # First attempt — new session
            result=$(claude -p "$goal" \
                --allowedTools "$ALLOWED_TOOLS" \
                --max-turns "$MAX_TURNS" \
                --output-format json \
                --json-schema "$SCHEMA" \
                2>/dev/null) || true
        else
            # Subsequent attempts — resume the same session
            result=$(claude -p "Continue working. The previous run ended before finishing." \
                --resume "$session_id" \
                --allowedTools "$ALLOWED_TOOLS" \
                --max-turns "$MAX_TURNS" \
                --output-format json \
                --json-schema "$SCHEMA" \
                2>/dev/null) || true
        fi

        # Parse the structured output
        session_id=$(echo "$result" | jq -r '.session_id // empty')
        completed=$(echo "$result" | jq -r '.structured_output.completed // false')
        summary=$(echo "$result" | jq -r '.structured_output.summary // .result // "no output"')

        echo "  Status: completed=$completed"
        echo "  Summary: $summary"

        if [ "$completed" = "true" ]; then
            goal_done=true
            break
        fi
    done

    if [ "$goal_done" = true ]; then
        echo "  PASSED after $attempt attempt(s)"
        ((passed++))
    else
        echo "  FAILED — did not complete after $MAX_RETRIES attempts"
        ((failed++))
    fi
done

# --- Report ---
echo ""
echo "=== Results ==="
echo "Total: $total | Passed: $passed | Failed: $failed"
exit $((failed > 0 ? 1 : 0))
