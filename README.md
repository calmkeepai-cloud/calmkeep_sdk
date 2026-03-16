
---

# Calmkeep SDK

Calmkeep is an external runtime layer that enhances Claude-based workflows by preserving structural continuity across long, multi-turn interactions.

Instead of relying on raw model context alone, Calmkeep introduces a continuity layer that helps maintain consistent reasoning, architectural stability, and compound analytical workflows across extended sessions.

Calmkeep works by routing Claude API requests through a lightweight runtime that enforces structural coherence while leaving model execution and billing fully with Anthropic.

Your application sends prompts to Calmkeep → Calmkeep forwards the request to Claude → the structured response is returned.

Claude remains the underlying model. Calmkeep provides the orchestration layer.

---

# Installation

Install the SDK directly from GitHub:

```
pip install git+https://github.com/calmkeepai-cloud/calmkeep-sdk
```

The SDK provides a lightweight client for sending prompts through the Calmkeep runtime.

---

# Quick Start

Import the client:

```python
from calmkeep import CalmkeepClient
```

Initialize the client with your keys:

```python
client = CalmkeepClient(
    calmkeep_key="YOUR_CALMKEEP_SUBSCRIPTION_KEY",
    claude_key="YOUR_CLAUDE_API_KEY"
)
```

Run a prompt:

```python
response = client.complete(
    prompt="Continue evolving the existing multi-tenant API..."
)

print(response)
```

Calmkeep routes the request through the runtime before sending it to Claude.

---

# How Calmkeep Works

Calmkeep sits between your application and the Claude API.

```
Your Application
      ↓
Calmkeep Runtime
      ↓
Claude API
      ↓
Structured Response
```

The runtime introduces a continuity layer that stabilizes reasoning across extended workflows.

Key properties:

• Bring your own Claude API key
• Claude billing remains directly with Anthropic
• Calmkeep does not resell tokens
• No modification of model weights
• External orchestration layer only

---

# Authentication

Two keys are required:

### Calmkeep API Key

Issued when you subscribe to Calmkeep.

Example:

```
ck_xxxxxxxxxxxxxxxxx
```

### Claude API Key

Your existing Anthropic API key.

Example:

```
sk-ant-xxxxxxxxxxxx
```

Both keys are required for each request.

---

# Example Workflow

```python
from calmkeep import CalmkeepClient

client = CalmkeepClient(
    calmkeep_key="ck_example",
    claude_key="sk-ant-example"
)

response = client.complete(
    prompt="Design a distributed locking strategy for a multi-region system",
    temperature=0.2
)

print(response)
```

---

# Using Calmkeep with MCP (Claude Desktop / Cursor)

Calmkeep can also be accessed through the Model Context Protocol (MCP).

This allows MCP-compatible environments such as Claude Desktop or Cursor to access Calmkeep as a tool.

The MCP server acts as a lightweight bridge between your development environment and the Calmkeep runtime.

---

## Clone the MCP server

```
git clone https://github.com/calmkeepai-cloud/calmkeep-mcp
cd calmkeep-mcp
```

---

## Install dependencies

```
pip install -r requirements.txt
```

---

## Configure environment variables

Create a `.env` file:

```
CALMKEEP_URL=https://your-calmkeep-runtime.modal.run
CALMKEEP_API_KEY=your_calmkeep_subscription_key
ANTHROPIC_API_KEY=your_claude_api_key
```

---

## Launch the MCP server

```
python mcp_server.py
```

The MCP server exposes the tool:

```
calmkeep_chat(prompt)
```

This tool becomes available inside MCP-compatible environments.

---

# Claude Code Plugin

Developers using Claude Code can install the Calmkeep plugin.

Install from the plugin marketplace:

```
/plugin marketplace add calmkeepai-cloud/calmkeep-claude-plugin
/plugin install calmkeep-continuity
```

Or install directly from GitHub:

```
/plugin install https://github.com/calmkeepai-cloud/calmkeep-claude-plugin
```

After installation configure keys:

```
export CALMKEEP_API_KEY=YOUR_CALMKEEP_SUBSCRIPTION_KEY
export CLAUDE_API_KEY=YOUR_CLAUDE_API_KEY
```

Claude Code requests will then route through the Calmkeep runtime.

---

# Using Calmkeep in Cursor

Cursor users can route Claude calls through the Calmkeep SDK.

Install:

```
pip install git+https://github.com/calmkeepai-cloud/calmkeep-sdk
```

Example usage:

```python
from calmkeep import CalmkeepClient
import os

client = CalmkeepClient(
    calmkeep_key=os.getenv("CALMKEEP_API_KEY"),
    claude_key=os.getenv("ANTHROPIC_API_KEY")
)
```

Calmkeep helps maintain architectural stability across long Cursor sessions.

---

# Using Calmkeep with OpenClaw

OpenClaw workflows can integrate Calmkeep through environment variables.

```
export CALMKEEP_API_KEY=your_key
export ANTHROPIC_API_KEY=your_claude_key
```

Then call the Calmkeep client inside your workflow scripts.

---

# Troubleshooting

### Missing Calmkeep key

```
export CALMKEEP_API_KEY=your_key
```

### Claude API key not configured

```
export ANTHROPIC_API_KEY=your_claude_key
```

Ensure both keys are available to your environment before running Calmkeep.

---

# License

MIT License

---

# Calmkeep

Calmkeep provides an external continuity layer for Claude workflows, helping complex analytical sessions remain structurally stable across long reasoning chains.

---
