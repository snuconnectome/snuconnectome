#!/bin/bash

# --- Configuration ---
# Add the commands to start your MCP servers to this array.
# Make sure they are activated within the virtual environment.
MCP_SERVERS=(
  "source .venv/bin/activate && sequential-thinking-mcp"
  "source .venv/bin/activate && serena start-mcp-server"
  # "source .venv/bin/activate && another-mcp-server" # Example: Add other servers here
)

# --- Script Body ---
echo "Starting MCP servers in the background..."

# Array to hold background process IDs (PIDs)
pids=()

# Function to clean up (kill) background servers
cleanup() {
  echo "Shutting down MCP servers..."
  for pid in "${pids[@]}"; do
    # Use kill to terminate the process group, ensuring child processes are also stopped.
    kill -TERM -- "-$pid" 2>/dev/null
  done
  echo "Cleanup complete."
}

# Trap the script's exit to run the cleanup function
trap cleanup EXIT

# Start all configured MCP servers in the background
for cmd in "${MCP_SERVERS[@]}"; do
  # Execute the command in a new process group so we can kill it and its children later.
  (set -m; bash -c "$cmd") &
  pids+=($!)
  echo "  - Started server with command: '$cmd' (PID: ${pids[-1]})"
done

echo "All servers started. Launching Gemini CLI..."
echo "------------------------------------------------"

# Execute the gemini command, passing along any arguments given to this script
gemini "$@"

echo "------------------------------------------------"
echo "Gemini CLI exited."
# The 'trap' will now call the cleanup function automatically.
