# AI Agents for Coding: A Practical Workshop

**From Zero to Productive with AI-Assisted Development**

---

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **Duration** | 120 minutes |
| **Target Audience** | Developers (all backgrounds) |
| **Prerequisites** | See [Pre-Workshop Checklist](#pre-workshop-checklist) |
| **Last Updated** | 2026-03-15 |
| **Version** | 0.2.0 (ready for delivery) |
| **Format** | Presenter's guide with hands-on exercises |

---

## Table of Contents

1. [Pre-Workshop Checklist](#pre-workshop-checklist)
2. [Agenda Overview](#agenda-overview)
3. [1. Welcome & Setting the Stage (5 min)](#1-welcome--setting-the-stage-5-min)
4. [2. The AI Coding Landscape (15 min)](#2-the-ai-coding-landscape-15-min)
5. [3. AI Subscriptions & Your License (10 min)](#3-ai-subscriptions--your-license-10-min)
6. [4. Hands-on: Getting Set Up & First Interactions (10 min)](#4-hands-on-getting-set-up--first-interactions-10-min)
7. [5. Prompt Engineering for Code (15 min)](#5-prompt-engineering-for-code-15-min)
8. [6. AGENTS.md & Custom Instructions (10 min)](#6-agentsmd--custom-instructions-10-min)
9. [7. Hands-on: Write Your First AGENTS.md (15 min)](#7-hands-on-write-your-first-agentsmd-15-min)
10. [8. Skills & Reusable Extensions (10 min)](#8-skills--reusable-extensions-10-min)
11. [9. Beyond VS Code: Terminal-Based Agents (15 min)](#9-beyond-vs-code-terminal-based-agents-15-min)
12. [10. Sub-agents & Advanced Patterns (5 min)](#10-sub-agents--advanced-patterns-5-min)
13. [11. Live Demo (Optional/Buffer) (5 min)](#11-live-demo-optionalbuffer-5-min)
14. [12. Q&A and Next Steps (5 min)](#12-qa-and-next-steps-5-min)
15. [Optional Extras](#optional-extras)
16. [Resources & Further Reading](#resources--further-reading)

---

## Pre-Workshop Checklist

**Participants: Please complete these steps BEFORE the workshop.**

### Essential Requirements

- [ ] **GitHub Account**: Create a GitHub account at github.com if you don't have one
- [ ] **Copilot License or Alternative Subscription**: Verify you have access to an AI coding tool
  - **GitHub Copilot**: Navigate to GitHub.com → Settings → Copilot and verify a plan is active
  - **Alternative**: ChatGPT Pro, Claude Pro, or other service (workshop will cover Copilot, but concepts transfer)
- [ ] **VS Code**: Install [Visual Studio Code](https://code.visualstudio.com/) (latest stable)
  - Windows: Download from [microsoft.com](https://code.visualstudio.com/) or install via Windows Store
  - macOS: Download .zip or use Homebrew: `brew install --cask visual-studio-code`
- [ ] **GitHub Copilot Extension**: Install in VS Code
  - Open VS Code → Extensions (Cmd+Shift+X / Ctrl+Shift+X)
  - Search: "GitHub Copilot"
  - Install official extension by GitHub (ID: `GitHub.copilot`)
- [ ] **GitHub Copilot Chat Extension**: Install in VS Code
  - Search: "GitHub Copilot Chat"
  - Install official extension by GitHub (ID: `GitHub.copilot-chat`)
- [ ] **Sign Into GitHub**: Verify VS Code is signed into your GitHub account
  - Check bottom-left avatar icon in VS Code — should show your GitHub username
  - If not signed in, click the avatar and authorize via GitHub.com
- [ ] **Verify Copilot is Active**: Open any `.py`, `.js`, or `.ts` file and start typing
  - You should see ghost text suggestions appear as you type
  - If not, see [Troubleshooting](#troubleshooting) below

### Optional But Recommended

- [ ] **A Sample Project**: Clone a repo (or use an existing project) to practice with
  - Suggestion: A personal project, open-source repo, or sample code
- [ ] **Node.js**: Install [Node.js](https://nodejs.org/) LTS (for some advanced exercises)
- [ ] **Git CLI**: Ensure Git is installed and configured
  - Test: `git --version` in terminal
  - Configure: `git config --global user.name "Your Name"` and `git config --global user.email "your@email.com"`

### Windows-Specific

- [ ] **Windows Terminal**: Install from Microsoft Store (recommended over cmd.exe)
  - Search "Windows Terminal" in Store, or: `winget install Microsoft.WindowsTerminal`
- [ ] **PowerShell 7+**: Recommended for modern shell experience
  - `winget install Microsoft.PowerShell`
- [ ] **WSL 2**: If you plan to use terminal-based agents, WSL 2 is recommended
  - See [Windows Subsystem for Linux installation](https://docs.microsoft.com/en-us/windows/wsl/install)

### Troubleshooting

**Copilot not showing suggestions?**

1. Check that the extension is enabled: VS Code → Extensions → GitHub.copilot → verify it says "Installed" not "Install"
2. Verify you're signed in: click the avatar in the bottom-left corner
3. Check file type: some file types (plain text, config files) may not get completions
4. Restart VS Code: sometimes needed after extension installation
5. Check your license: GitHub.com → Settings → Copilot → ensure a plan is listed (not expired)

**Extension won't install or activate on Windows?**

- Corporate network? Check if your firewall/proxy blocks `api.github.com` or `copilot.microsoft.com`
- Ask your IT/network team to whitelist these domains
- Try installing within VS Code while connected to personal WiFi as a test

**Copilot Chat won't open (Cmd+Shift+I)?**

- Verify both extensions are installed: `GitHub.copilot` AND `GitHub.copilot-chat`
- Restart VS Code
- Try accessing chat via the sidebar icon (should appear once extension is active)

**Still stuck?** Let the presenter know before the workshop starts — we can troubleshoot live.

---

## Agenda Overview

| Time | Section | Duration | Mode |
|------|---------|----------|------|
| 00:00 | Welcome & Setting the Stage | 5 min | Presentation |
| 00:05 | The AI Coding Landscape | 15 min | Presentation |
| 00:20 | AI Subscriptions & Your License | 10 min | Presentation + Handout |
| 00:30 | Hands-on: Getting Set Up & First Interactions | 10 min | **Hands-on** |
| 00:40 | Prompt Engineering for Code | 15 min | Presentation + Examples |
| 00:55 | AGENTS.md & Custom Instructions | 10 min | Presentation + Demo |
| 01:05 | Hands-on: Write Your First AGENTS.md | 15 min | **Hands-on** |
| 01:20 | Skills & Reusable Extensions | 10 min | Presentation + Demo |
| 01:30 | Beyond VS Code: Terminal-Based Agents | 15 min | Presentation + Demo |
| 01:45 | Sub-agents & Advanced Patterns | 5 min | Presentation |
| 01:50 | Live Demo (Optional/Buffer) | 5 min | Demo |
| 01:55 | Q&A and Next Steps | 5 min | Discussion |
| **02:00** | **END** | **Total: 120 min** | — |

---

## 1. Welcome & Setting the Stage (5 min)

### Talking Points

> **Opening**: "Today, we're going to spend 2 hours learning to use AI agents for coding. By the end, you'll understand not just HOW to use these tools, but WHEN and WHERE they fit into your workflow—regardless of what you're building."

**Key messages to deliver:**

1. **This is about productivity, not replacement**
   - AI agents are not replacing you; they're making you **faster and less bored**
   - Think of it as **pair programming with a very knowledgeable but sometimes confidently wrong partner**
   - Your job is to stay in the driver's seat — the AI is the navigator
   - The best code is still written by humans who understand the problem

2. **Everyone starts here**
   - Whether you've used Copilot before, tried ChatGPT, or this is your first time — you're in the right place
   - Quick poll: "Who's used Copilot before? ChatGPT? Claude? Other tools?"
   - All levels welcome — we'll move at the group's pace

3. **This is hands-on**
   - You'll have laptops open throughout
   - If you get stuck, raise your hand — no dumb questions
   - We'll troubleshoot together if anyone's setup isn't working

4. **The landscape moves fast**
   - These tools evolve weekly — new features, new capabilities
   - What matters most is **understanding the patterns**, not memorizing specific buttons
   - You'll be able to apply what you learn today to tools that don't exist yet

### Setup Check

- Confirm: "Everyone has VS Code open with Copilot active? Hands up if you need help."
- Have a backup plan: if 1-2 people have setup issues, continue; offer to help at break or after

---

## 2. The AI Coding Landscape (15 min)

### The Era of Autonomous AI

> **Key theme**: "The era of AI as text is over. Execution is the new interface. Autonomy is now configurable—you decide how much the AI does on its own."

This is the state of AI coding in March 2026: we've moved from "suggest what I should type" to "execute this feature autonomously, with my approval."

### Types of AI Coding Tools

Present this as a spectrum of capabilities and use cases:

#### **1. Inline Completions (Ghost Text)**

- **What it is**: AI suggests code as you type; you see faded suggestions
- **When to use**: Quick variable names, boilerplate, filling in obvious patterns
- **Example**: Type `def validate_` and the AI suggests `def validate_email(address: str) -> bool:`
- **Interaction**: Tab to accept, Escape to reject, keep typing to refine
- **Cost**: Free tier includes 2,000 completions/month; Pro+ unlimited
- **Best for**: Individual developers, quick refactors, learning patterns

#### **2. Chat / Ask Mode**

- **What it is**: Conversational AI — ask questions about code, architecture, syntax
- **When to use**: "How do I...?" questions, explain complex code, design discussion
- **Example**: "I need to validate user input. What's the difference between synchronous and async validation in React?"
- **Interaction**: Type in chat window, AI responds; you can follow up with clarifications
- **Cost**: Free tier 50 messages/month; Pro unlimited
- **Best for**: Learning, brainstorming, code review advice

#### **3. Edit Mode (Deprecated, but still available)**

- **What it is**: Select code or type instructions; AI edits your code in place
- **When to use**: Targeted refactoring, adding error handling, renaming variables
- **Example**: Select a function, ask "Add input validation to all parameters"
- **Interaction**: Cmd+I (macOS) / Ctrl+I (Windows), describe the edit, review and accept
- **⚠️ Status**: **Deprecated as of VS Code 1.111**. Still supported through v1.125, then removal.
- **Cost**: Counts as premium requests (300-1,500/month depending on tier)
- **Best for**: Small, focused changes
- **Note**: The recommended replacement is Chat mode with explicit code selection

#### **4. Agent Mode**

- **What it is**: Autonomous AI that can explore your codebase, modify multiple files, run commands
- **When to use**: Building new features, large refactors, multi-file changes, automation
- **Example**: "Add comprehensive error handling and logging to the payment module"
- **Interaction**: Describe the task; agent plans, executes, iterates until done or requests approval
- **Approvals**: Three levels (configurable in VS Code 1.111+): Default Approvals, Bypass Approvals, Autopilot
- **Cost**: Premium requests (expensive; ~0.04/request overage)
- **Best for**: Complex tasks, infrastructure work, large refactors

**Interaction Modes Comparison:**

| Tool | Setup | Speed | Power | Cost | Best For |
|------|-------|-------|-------|------|----------|
| Completions | Instant | Instant | Low | Free (limited) | Quick fills |
| Chat | Instant | ~5-30 sec | Medium | Free (limited) | Questions, learning |
| Edit* | 2 sec | ~5-15 sec | Medium-High | Premium request | Targeted changes *(deprecated)* |
| Agent | 5 sec | ~30-120 sec | High | Premium request | Complex tasks |

### Key Models Powering These Tools

- **Claude 4.6** (Anthropic): Flagship agentic model (Feb 17, 2026). Exceptional reasoning, code understanding, autonomous execution
- **GPT-5.2** (OpenAI): Latest flagship. Fast, reliable, broad knowledge, agentic workflows
- **Opus 4.6** (Anthropic): Extended reasoning and deep analysis
- **Gemini 3 Pro** (Google): Multimodal, great for docs and diagrams
- **Grok Code** (xAI): Fast iteration, cutting-edge
- **Smaller models**: Faster, cheaper, work well for scoped tasks

> **Presenter note**: The same PATTERNS apply across models. If you know how to prompt Claude well, you can adapt to GPT or Gemini. The interface changes; the thinking doesn't.

### The Tools Ecosystem

**IDE-Integrated Tools:**
- **GitHub Copilot** (Microsoft/GitHub): Market leader — VS Code, JetBrains, Neovim, GitHub.com
  - **Latest**: VS Code 1.111 introduces Autopilot mode (autonomous agents), agent permission levels, Edit Mode deprecated
- **Cursor**: IDE built around AI; powerful chat and agent modes; 1M+ daily active users
- **JetBrains + Copilot**: Official support for Copilot in IntelliJ, PyCharm, WebStorm, etc.

**Web-Based & Cloud Tools:**
- **ChatGPT** (OpenAI): Web interface, Codex cloud agent (Plus+ subscription)
- **Claude.ai** with Claude Code (Anthropic): Browser-based, includes terminal agent; Pro subscription
- **Windsurf** (Codeium): Cloud agents, Cascade agentic flow, live website editing previews; 1M+ users

**Terminal & Open-Source:**
- **Claude Code** (Anthropic): Terminal-based agent, multi-file editing, autonomous execution
- **OpenCode**: Open-source agent framework with sub-agent architecture
- **Aider**: Git-aware pair programming in the terminal
- **GitHub Copilot CLI**: `gh copilot suggest` for terminal commands

**Enterprise & Specialized:**
- **Salesforce Einstein for Developers**: Used by 20K+ devs at Salesforce; enterprise adoption
- **59% of Fortune 500** now evaluating or deploying AI coding tools (Cursor, Copilot, others)

### MCP: The Interop Standard

**Model Context Protocol (MCP)** is no longer emerging — it's becoming THE standard for agent-tool integration.

- **What it does**: Connects AI agents to databases, APIs, custom tools, file systems
- **Examples**: Query Postgres from within an agent, call Jira API, run your custom CLI tools
- **Status**: Supported in Copilot Pro/Business/Enterprise, native in Claude Code, strong support in OpenCode
- **Impact**: Agents can now "reach out" to your infrastructure and make informed decisions

---

## 3. AI Subscriptions & Your License (10 min)

### GitHub Copilot Plans

| Feature | Free | Pro ($10/mo) | Pro+ ($39/mo) | Business ($19/seat) | Enterprise ($39/seat) |
|---------|------|-------------|---------------|--------------------|-----------------------|
| **Completions** | 2,000/mo | Unlimited | Unlimited | Unlimited | Unlimited |
| **Chat messages** | 50/mo | Unlimited | Unlimited | Unlimited | Unlimited |
| **Premium requests** | 50/mo | 300/mo | 1,500/mo | 300/mo | 1,000/mo |
| **Agent mode** | ❌ | ✅ | ✅ | ✅ | ✅ |
| **Model selection** | Basic only | Extended | All (Claude, GPT, etc.) | Extended | All models |
| **Edit Mode*** | ❌ | ✅ | ✅ | ✅ | ✅ |
| **MCP support** | ❌ | ✅ (limited) | ✅ | ✅ | ✅ |
| **Org policies & audit** | ❌ | ❌ | ❌ | ✅ | ✅ |
| **IP indemnity** | ❌ | ❌ | ❌ | ✅ | ✅ |

*Edit Mode is deprecated as of VS Code 1.111; supported through v1.125, then removal.

### Alternative Subscriptions

If you're using a different AI service, here's how they compare for coding:

#### **ChatGPT / OpenAI**

| Feature | Free | Plus ($20/mo) | Pro ($200/mo) | Team ($25/user/mo) | Enterprise |
|---------|------|---------------|---------------|--------------------|-----------| 
| **Base Model** | GPT-4o mini | GPT-4o | o1-pro | GPT-4o / o1 | Custom |
| **Code Agent (Codex)** | ❌ | ✅ | ✅ | ✅ | ✅ |
| **Multi-file editing** | Limited | ✅ | ✅ | ✅ | ✅ |
| **Workspace features** | ❌ | ❌ | ❌ | ✅ | ✅ |
| **SSO & admin controls** | ❌ | ❌ | ❌ | ✅ | ✅ |

**Codex**: OpenAI's cloud-based coding agent. Runs in a sandbox, explores repos, creates PRs. Available with Plus and above.

#### **Claude / Anthropic**

| Feature | Free | Pro ($20/mo) | Team ($25/user/mo) | Enterprise ($30/user/mo) |
|---------|------|-------------|--------------------|----|
| **Base Model** | Claude 3.5 Sonnet | Claude 4.6 | Claude 4.6 | Claude 4.6 |
| **Claude Code (terminal agent)** | Limited | ✅ | ✅ | ✅ |
| **Multi-file editing** | Limited | ✅ | ✅ | ✅ |
| **Autonomous execution** | ❌ | ✅ | ✅ | ✅ |
| **Workspace features** | ❌ | ❌ | ✅ | ✅ |
| **SSO & SCIM** | ❌ | ❌ | ❌ | ✅ |

**Claude Code**: Anthropic's terminal-based agent. Multi-file editing, autonomous task execution, MCP support.

### Understanding "Premium Requests"

A **premium request** is any interaction that uses advanced AI reasoning (Edit mode, Agent mode, complex Chat queries).

- Simple completions: **NOT** premium (free tier limit: 2,000/month)
- Simple chat questions: Often free (depends on complexity)
- Edit mode interactions: **ALWAYS** premium (but Edit Mode is deprecated)
- Agent mode: **ALWAYS** premium
- Overages: $0.04/request for Pro+ Copilot; billed to your GitHub account

### How to Check Your Plan & Usage

**Check your Copilot tier:**

1. Go to GitHub.com → Settings → Copilot
2. Under "Your plan" — shows current tier and renewal date
3. Note the tier for reference during the workshop

**Check your usage:**

1. Same page → scroll to "Usage"
2. Shows premium requests used this month
3. Example: "123 / 300 used" means you have 177 premium requests left

**For org admins (Business/Enterprise):**

1. Organization settings → Copilot → Usage and adoption
2. Dashboard showing per-seat usage, trends, adoption metrics
3. Set spending limits and alerts

### Where Things Differ by Service

**If you're using ChatGPT Plus/Pro or Claude Pro** during the workshop:

- **Chat-based**: Use web interface instead of VS Code integration
- **File context**: Copy-paste code or use file upload; no automatic workspace integration
- **Agents**: Codex (ChatGPT) or Claude Code (Claude) are separate tools; not integrated into VS Code
- **Concepts transfer**: Everything about prompting, AGENTS.md structure, and patterns still applies

**Practical budgeting:**

- **Pro Copilot** (300/month): ~10 agent tasks or ~30 complex edits per month
- **Pro+ Copilot** (1,500/month): ~50 agent tasks or ~150 complex edits per month
- **ChatGPT Plus**: $20/mo, unlimited basic usage; Codex runs in chat
- **Claude Pro**: $20/mo, unlimited basic usage; Claude Code available

---

## 4. Hands-on: Getting Set Up & First Interactions (10 min)

### Exercise: Verify Your Setup (2 minutes)

1. **Open VS Code** — you should already have it open from the checklist
2. **Check the status bar** (bottom-right corner)
   - Should show a Copilot icon
   - Click it — should say "Copilot" and show an indicator (blue or green = active)
3. **Open Copilot Chat**
   - Keyboard: Cmd+Shift+I (macOS) or Ctrl+Shift+I (Windows)
   - Or click the chat icon in the left sidebar
   - Chat panel should appear on the right side
4. **Verify you're signed in**
   - Top of chat panel: should show your GitHub username
   - If you see "Sign In", click it and authorize via GitHub

> **Troubleshooting shortcut**: If Copilot Chat doesn't open, make sure you installed BOTH extensions: `GitHub.copilot` AND `GitHub.copilot-chat`.

### Exercise: Try Inline Completion (2 minutes)

1. **Create a new Python file** in VS Code
   - File → New File → select Python language
   - Or open an existing `.py` file
2. **Type a partial function definition**:

```python
def validate_email
```

3. **Watch for ghost text** — a faded suggestion should appear
   - The AI is suggesting the function signature and/or body
4. **Accept the suggestion**: Press Tab
5. **If you don't like it**: Press Escape and keep typing to refine

**What you're seeing**: Inline completions. This is the "free" Copilot experience.

### Exercise: Try Chat Mode (3 minutes)

1. **Copilot Chat** should still be open (Cmd+Shift+I)
2. **Ask a question**:

```
How do I validate an email address in Python using the email-validator library?
```

3. **Review the response**
   - Chat will provide an explanation plus a code block
   - Notice the buttons: "Copy", "Insert at Cursor" (if applicable)
4. **Follow up with a refinement**:

```
Add error handling to catch invalid email formats
```

5. **Observe**: Chat lets you iterate and refine

**What you're learning**: Chat mode is conversational and free (within limits). Great for questions.

### Exercise: Try Agent Mode (3 minutes — if time permits)

1. **In Copilot Chat**, look for a mode selector (dropdown or toggle)
   - You should see options: **Ask** (💬), **Edit** (✏️), **Agent** (🤖)
2. **Select Agent mode** (🤖)
3. **Give a simple task**:

```
Create a Python function that takes a list of numbers and returns the sum. Include docstrings and type hints.
```

4. **Observe**: Agent mode explores context, plans steps, and executes
5. **Notice**: You get to approve each step; watch how the agent reasons

**What you're learning**: Agent mode is more autonomous. This is the future interface.

### Note on Edit Mode

Edit Mode (Cmd+I) was the previous way to do targeted edits, but **it's deprecated as of VS Code 1.111**. You might see it in some documentation, but:
- Still works through v1.125
- Being removed after that
- Chat mode with code selection is the recommended replacement

---

## 5. Prompt Engineering for Code (15 min)

### The Pattern: Specific > Vague

**❌ Vague prompts**

```
Fix this code
Write a function to deploy
Add tests
```

**✅ Specific prompts**

```
This function throws an error when the input list is empty. 
Add a guard clause at the top to check for null or empty input and return an empty list.
```

```
Write a Python function that connects to a PostgreSQL database using psycopg2, 
retrieves user records where age > 21, and returns them as a list of dictionaries. 
Include error handling for connection failures.
```

```
Write unit tests for the UserRepository class. Test cases: 
1. create_user with valid data succeeds
2. create_user with missing email raises ValueError
3. find_user_by_id when user exists returns user
4. find_user_by_id when user doesn't exist returns None
```

### Best Practices with Examples

#### **1. Provide Context**

- Bad: "How do I deploy?"
- Good: "We use Docker and Kubernetes. How do I write a multi-stage Dockerfile to minimize image size for a Python web app?"

#### **2. Be Specific About Constraints**

- Bad: "Optimize this code"
- Good: "This API endpoint processes 10,000 requests per minute synchronously. Refactor to use async/await to improve throughput. Keep the error handling logic intact."

#### **3. Use the Right Mode for the Job**

- Quick syntax question? → **Chat mode** (free, instant)
- Small refactor? → **Chat mode with code selection** (targeted, often free)
- New feature across files? → **Agent mode** (powerful, costs more)
- Architecture discussion? → **Chat mode** (free if not too complex)

#### **4. Leverage Context Features**

- `@workspace` — give AI the whole project context
- `@file:path/to/file.py` — reference specific files
- `#selection` — reference highlighted code in chat
- Copy-paste relevant logs, error messages, existing code

#### **5. Iterate and Refine**

- Start broad: "Generate a Docker Compose setup for a full-stack app"
- Then narrow: "Add a health check endpoint to the web service"
- Then debug: "This network config isn't working. Here's the error… [paste logs]. What's wrong?"

**Golden rule**: If the AI gets something wrong, tell it WHY it's wrong, then ask again. Don't repeat the same prompt.

### Real-World Examples (Mixed Domains)

These are realistic prompts for various types of development:

#### **Web Backend (Python/Django)**

```
Write a Django REST API endpoint that:
1. Accepts POST requests with user email and password
2. Validates input (email format, password strength)
3. Creates a new user if email doesn't exist
4. Returns JWT token on success
5. Returns 400 for validation errors, 409 for duplicate email

Include error handling, logging, and unit tests.
```

#### **Frontend (React)**

```
Create a React component that:
- Displays a list of products fetched from /api/products
- Shows a loading spinner while fetching
- Handles errors with a user-friendly message
- Filters products by category (dropdown)
- Uses React hooks (useState, useEffect)
- Has prop validation

Include TypeScript types.
```

#### **Infrastructure (Terraform)**

```
Generate a Terraform module for an Azure App Service with:
- App Service Plan (customizable SKU)
- Web App with app settings and connection strings
- Application Insights for monitoring
- Key Vault integration for secrets
- Outputs for app ID and principal ID

Use variables for environment-specific values.
```

#### **Data / SQL**

```
Write a SQL query that:
1. Joins users and orders tables
2. Aggregates total spending per user
3. Filters for users with > $1000 spent in last 30 days
4. Orders by spending (highest first)
5. Includes error handling for missing data

Test it on this sample dataset: [paste or describe]
```

#### **Kubernetes**

```
Convert this Helm chart to support multiple environments (dev, staging, prod):
[paste chart]

Use overlays or separate values files for:
- Replica counts
- Resource limits
- Image tags
- Environment variables
- Ingress hosts

Include kustomization or values structure.
```

#### **Debugging**

```
I'm getting this error:
[paste error logs]

When running: [command you ran]

The relevant code is:
[paste code snippet]

What's the issue and how do I fix it?
```

---

## 6. AGENTS.md & Custom Instructions (10 min)

### The Problem They Solve

Every time you open Copilot, the AI starts from zero. It doesn't know:

- Your project's coding conventions
- Your architecture decisions
- Your security requirements
- Which patterns you prefer
- How your codebase is organized

**Result**: Without instruction files, you spend time correcting the AI. With them, the AI learns your project and gives better suggestions immediately.

### The Ecosystem of Instruction Files

Different tools support different formats:

| File | Scope | Supported By | Notes |
|------|-------|------------|-------|
| **`.github/copilot-instructions.md`** | GitHub Copilot only | GitHub Copilot, Copilot Chat | GitHub's official format |
| **`AGENTS.md`** | Multi-tool (emerging standard) | OpenCode, Copilot, future tools | Best for cross-tool portability |
| **`CLAUDE.md`** | Claude-based tools | Claude Code, Cursor (Claude mode) | Specialized for Claude models |
| **`GEMINI.md`** | Gemini-based tools | Gemini-based agents | Google's format |
| **`.cursorrules`** | Cursor IDE | Cursor only | Cursor-specific |

> **Key insight**: Start with `AGENTS.md`. It's becoming the standard. If you need to be Copilot-specific, also create `.github/copilot-instructions.md`. Have both point to the same content or just put different details in each.

### What to Put in AGENTS.md

**Structure** (roughly 100-300 lines):

```markdown
# Project: [Name]

## Overview
[1-2 paragraphs: what this project does, who uses it, why it exists]

## Tech Stack
- [Language, frameworks, versions]
- [Key dependencies]
- [Deployment platform/infrastructure]

## Project Structure
src/
├── api/         # REST endpoints
├── models/      # Data models
├── services/    # Business logic
└── tests/       # Unit and integration tests

## Coding Conventions
- **Naming**: snake_case for variables/functions, PascalCase for classes
- **Files**: One class per file, module-level docstrings required
- **Imports**: Sort alphabetically, group stdlib / third-party / local
- **Error handling**: Custom exceptions for validation; log and re-raise

## Architecture Decisions
- [Decision 1]: [Rationale]
- [Decision 2]: [Rationale]

## Security Requirements
- No hardcoded credentials; use secrets manager
- All APIs require authentication
- Data at rest: encrypted with AES-256
- Data in transit: TLS 1.3 minimum

## Testing
- All public methods must have unit tests
- Integration tests use test fixtures, not live databases
- Coverage: target 85% minimum
- Run: `pytest tests/` or `make test`

## DO ✅
- Use type hints
- Write docstrings for complex functions
- Validate input parameters
- Log important operations and errors
- Create small, focused PRs

## DON'T ❌
- Hardcode environment-specific values
- Use print() for logging; use the logging module
- Ignore error cases
- Create massive classes or functions
- Skip tests

## Deployment
- Staging: automatic on PR merge to `develop`
- Production: manual approval required
- Rollback: via previous deployment or git revert
```

### Example AGENTS.md for Multiple Domains

Here are quick examples for different types of projects:

**Web Backend:**
```markdown
# Project: User API Service

## Overview
REST API for user authentication, profiles, and account management. 
Used by web and mobile clients. Built with Python/FastAPI.

## Tech Stack
- Python 3.11+, FastAPI, Pydantic, SQLAlchemy
- PostgreSQL 15+, Redis for caching
- Docker, Kubernetes, GitHub Actions

## Coding Conventions
- snake_case functions and variables, PascalCase for classes
- Type hints required
- Docstrings for all public functions
- Error handling: raise custom exceptions, log before re-raising

## DO ✅
- Use dependency injection (Pydantic settings)
- Validate all inputs with Pydantic models
- Write unit tests for all endpoints

## DON'T ❌
- Use global variables
- Hardcode API secrets
- Log sensitive data (passwords, tokens)
```

**Frontend (React):**
```markdown
# Project: Dashboard UI

## Overview
React-based admin dashboard for our SaaS platform. 
Displays analytics, user management, billing.

## Tech Stack
- React 18+, TypeScript, Tailwind CSS
- Zustand for state management
- React Query for API calls
- Jest + React Testing Library

## Coding Conventions
- TypeScript everywhere; no `any` types
- Functional components with hooks
- PascalCase for components, camelCase for functions
- Props validation with TypeScript interfaces

## DO ✅
- Use custom hooks to share logic
- Memoize expensive components with React.memo
- Write integration tests for key flows

## DON'T ❌
- Class components
- Global state for UI-only data
- Fetch API directly; use React Query
```

**Infrastructure (Terraform):**
```markdown
# Project: Cloud Platform Infrastructure

## Overview
Terraform, Kubernetes, and CI/CD for our cloud platform on Azure.

## Tech Stack
- Terraform 1.7+, Azure provider v4.0+
- Kubernetes 1.29+, Helm 3
- GitHub Actions for CI/CD

## Coding Conventions
- Terraform: snake_case for variables and resources
- All modules: main.tf, variables.tf, outputs.tf structure
- Kubernetes: one namespace per app, use kustomize overlays

## Security Requirements
- No public endpoints without WAF
- All secrets in Key Vault
- Pod security: restricted PSS

## DO ✅
- Use modules for reusable infrastructure
- Add lifecycle blocks to prevent accidental destruction
- Enable diagnostic logging

## DON'T ❌
- Hardcode subscription IDs or region names
- Create resources in default namespace
- Store secrets in Git
```

---

## 7. Hands-on: Write Your First AGENTS.md (15 min)

### Exercise Overview

**Goal**: Create a basic AGENTS.md that teaches Copilot about YOUR project.

**Time**: ~15 minutes (some can finish after workshop and refine later)

### Step-by-Step

1. **Pick a project** (2 minutes to set up)
   - Use an existing project you work on
   - Or clone a sample repo provided
   - Or create a new toy project if nothing else available

2. **Create `AGENTS.md` at the repo root**
   - File → New File → Name it `AGENTS.md` (capital A and M)
   - Save it at the root of your project directory

3. **Fill in the template** (10 minutes)
   - Use the template below
   - Replace placeholders with YOUR project details
   - Aim for 100-200 lines; more is OK, less is OK too

4. **Test it** (3 minutes)
   - Open Copilot Chat
   - Ask it to generate code for your project
   - Does it follow your conventions?

### Template to Get Started

```markdown
# Project: [Your Project Name]

## Overview
[1-2 sentences: What does this project do? Who uses it?]

## Tech Stack
- [Languages, frameworks, versions]
- [Key libraries/dependencies]
- [Deployment platform]

## Project Structure
[Quick overview of main directories and what each does]

## Coding Conventions
- **Naming**: [e.g., snake_case for functions, PascalCase for classes]
- **Error Handling**: [How you handle errors]
- **Imports**: [e.g., alphabetical order, grouped by type]
- **Comments**: [Docstring requirements]

## Key Patterns & Decisions
- [Pattern 1: explanation]
- [Pattern 2: explanation]

## Security Requirements
- [Requirement 1]
- [Requirement 2]

## DO ✅
- [Best practice 1]
- [Best practice 2]

## DON'T ❌
- [Anti-pattern 1]
- [Anti-pattern 2]

## Testing & Quality
- How to run tests: [e.g., `pytest`, `npm test`]
- Coverage expectations: [e.g., 80%+]
- Linting/formatting: [e.g., Black, Prettier]

## Deployment
- How/where code is deployed
- Key environments: dev, staging, prod
- Rollback procedures
```

### Test It Out

Once you've written your AGENTS.md:

1. **Open Copilot Chat** in the project directory (Cmd+Shift+I)
2. **Ask Copilot to generate code**:
   - "Generate a new function for [a realistic task in your project]"
   - "Create a test for [existing functionality]"
3. **Observe**: Does the AI follow your conventions? Use the right tech stack? Match your patterns?
4. **Refine**: If not, add more specific rules to AGENTS.md

> **Presenter note**: If your AGENTS.md is in the repo root and you've saved it, Copilot should pick it up. If it doesn't seem to be using it, you may need to restart VS Code for it to reload.

---

## 8. Skills & Reusable Extensions (10 min)

### What Are Skills?

**Skills** are reusable instruction sets that can be loaded on demand. Think of them as "expertise modules" — load security expertise for security work, React patterns for React work.

- They complement AGENTS.md
- They're task-level, not project-level
- You can have many skills in a project

### When to Use Skills

**✅ Good use cases:**

- Domain-specific work (security review, test generation, API design)
- Switching between different project types or tech stacks within the same repo
- Standardizing practices across a team
- Loading specialized knowledge (compliance rules, coding standards)

**❌ Avoid when:**

- Simple, single-file edits (overkill)
- AGENTS.md already covers what you need (avoid duplication)
- The skill adds too much context and slows down responses
- You're just starting — master AGENTS.md first

### Relationship to AGENTS.md

Think of it this way:

| Aspect | AGENTS.md | Skills |
|--------|-----------|--------|
| **Scope** | Project-level | Task-level |
| **Loading** | Always (auto) | On demand |
| **Purpose** | Teaches AI about YOUR project | Provides DOMAIN expertise |
| **Example** | "Our code uses Python 3.11, Pydantic models, async/await" | "When generating tests, use pytest fixtures and mocks" |
| **Lifespan** | Lives in repo, evolves slowly | Can be versioned, shared across teams |

**They complement each other:**

- **AGENTS.md**: "Here's what we're building"
- **Skills**: "Here's HOW we build it [for this task]"

### What a Skill File Looks Like

A skill is a markdown file (e.g., `SKILL-TESTING.md`) with focused instructions:

```markdown
# Skill: Test Generation

## Purpose
Generate comprehensive unit and integration tests following our patterns.

## When to Use This Skill
Ask Copilot: "Using the Testing skill, generate tests for [function]"

## Testing Framework
- pytest for unit tests
- pytest-mock for mocking
- pytest-asyncio for async tests

## Test Structure
```python
# tests/test_users.py
import pytest
from unittest.mock import Mock
from app.services import UserService

@pytest.fixture
def user_service():
    """Fixture providing UserService with mocked dependencies."""
    return UserService(db=Mock())

def test_create_user_success(user_service):
    # Arrange
    # Act
    # Assert
    pass
```

## Patterns We Use
- Arrange-Act-Assert (AAA) structure
- One assertion per test (usually)
- Descriptive test names: `test_[what]_[given]_[then]`
- Use fixtures for setup, not setUp methods

## Coverage Goals
- Aim for 85%+ coverage
- All public APIs must have tests
- Edge cases and error paths required
```

### Where Skills Live

Skills can be stored:

- **In your repo**: `skills/SKILL-TESTING.md`, `skills/SKILL-SECURITY.md`
- **In a shared location**: Company skill library
- **Inline**: Referenced in AGENTS.md with full content

### Using Skills in Practice

In Copilot Chat, reference skills by name:

```
@skill:TESTING Generate tests for the UserRepository class
```

Or just mention it:

```
Using our testing patterns, generate tests for the checkout flow
```

**Then Copilot loads the skill** and applies its patterns to your code.

---

## 9. Beyond VS Code: Terminal-Based Agents (15 min)

### Why Terminal Agents Matter

- **Larger changes**: Edit multiple files across your codebase
- **Autonomous execution**: Run builds, tests, commands without waiting for approval
- **Better for batch work**: Refactor all modules at once, not one by one
- **Works on headless systems**: Servers, CI/CD pipelines, remote machines
- **Part of developer workflow**: Some engineers prefer terminal over GUI

### Tools Overview

#### **GitHub Copilot CLI**

- **Commands**: `gh copilot suggest "what you want"` and `gh copilot explain "command"`
- **Best for**: Shell command suggestions, explaining complex bash/PowerShell
- **Cost**: Included with your Copilot subscription
- **Install**: `gh extension install github/gh-copilot`
- **Example**:
  ```bash
  gh copilot suggest "find all Python files modified in the last week"
  # Suggests: find . -name "*.py" -mtime -7
  ```

#### **Claude Code (Anthropic)**

- **Features**: Multi-file editing, autonomous task execution, command execution, MCP support
- **Best for**: Large infrastructure refactors, multi-file features, complex reasoning
- **Cost**: Claude Pro ($20/mo) or API pricing
- **Access**: `claude.ai` → Claude Code toggle, or CLI: `claude code`
- **Real example**:
  ```
  claude code: Refactor all database queries to use prepared statements
  ```

#### **OpenCode**

- **Features**: Open-source agent framework; sub-agent architecture; supports multiple models
- **Best for**: Custom workflows, teams that want full control, infrastructure teams
- **Cost**: Free and open-source
- **Access**: <https://github.com/opencode/opencode>
- **Strength**: Integrates with AGENTS.md out of the box

#### **Aider**

- **Features**: Git-aware pair programming in the terminal; commits automatically
- **Best for**: Developers who commit frequently; teams using version control
- **Cost**: Free and open-source
- **Install**: `pip install aider-chat` (or `uv pip install aider-chat`)
- **Example**:
  ```bash
  aider                    # Start interactive session
  /ask "add error handling to payment module"
  # Aider explores code, makes changes, shows diffs, commits with message
  ```

### Demo: Terminal Agent in Action (Presenter)

> **Live demo suggestion**: Open Claude Code or OpenCode and execute a multi-file task. For example:
>
> **Task**: "Add logging to all functions in the utils module"
>
> **What to show**:
> 1. The agent explores the codebase
> 2. Identifies all functions in utils/
> 3. Plans the changes
> 4. Implements logging (same pattern across all functions)
> 5. Shows you a diff
> 6. Awaits your approval
>
> **Key points to highlight**:
> - The agent reads your AGENTS.md and follows your conventions
> - It can run arbitrary commands (tests, linting, validation)
> - It makes changes across multiple files in one shot
> - You maintain control: review, approve, iterate

### Platform-Specific Considerations

> **Note**: If `pip` is not available on your system (common on modern Macs), you can use [uv](https://docs.astral.sh/uv/) in place of `pip`. Simply replace `pip` with `uv pip` in any of the commands below.

#### **macOS & Linux**

Terminal agents work great natively. Just install Python and the tool:

```bash
pip install aider-chat
# Or with uv: uv pip install aider-chat
# or
git clone https://github.com/opencode/opencode && cd opencode && pip install -e .
# Or with uv: git clone https://github.com/opencode/opencode && cd opencode && uv pip install -e .
```

#### **Windows**

Terminal agents work best with:

- **WSL 2** (Windows Subsystem for Linux 2) — recommended for best experience
- **Windows Terminal** (native support varies)

**Setup if you want to try:**

```powershell
# In Windows PowerShell (as Administrator)
wsl --install

# Then in WSL 2 terminal:
pip install aider-chat
# Or with uv: uv pip install aider-chat
# or
git clone https://github.com/opencode/opencode && cd opencode && pip install -e .
# Or with uv: git clone https://github.com/opencode/opencode && cd opencode && uv pip install -e .
```

### When to Use Terminal vs. VS Code

| Scenario | Use Terminal Agent | Use VS Code Copilot |
|----------|-------------------|-------------------|
| Single-file edit | ❌ Overkill | ✅ Chat or Edit |
| Multi-file refactor | ✅ Perfect | ⚠️ Works, slower |
| Just asking a question | ❌ No | ✅ Chat |
| Running tests/builds | ✅ Natural | ⚠️ Possible |
| Large infrastructure work | ✅ Best | ⚠️ OK |
| CI/CD integration | ✅ Great | ❌ No |

---

## 10. Sub-agents & Advanced Patterns (5 min)

### What Are Sub-agents?

A **coordinator agent** delegates specialized tasks to **sub-agents**, each with its own role and AGENTS.md file.

**Example architecture:**

```
[Coordinator Agent] "Implement feature X with full CI/CD"
    ├─→ [@Security Agent] Review for vulnerabilities
    ├─→ [@Test Agent] Generate test cases
    ├─→ [@Ops Agent] Set up monitoring and alerting
    └─→ [@Docs Agent] Write API documentation
```

**Benefits:**

- Each sub-agent is specialized and has narrower scope
- Results are better because each one deep-dives its domain
- Cost-effective: coordinator makes high-level decisions; sub-agents handle details
- Scalable: add new sub-agents as needed
- Parallel execution: sub-agents can work simultaneously

### MCP (Model Context Protocol)

**What it is**: A standard for connecting AI agents to external tools and data sources.

**Examples of what MCP can connect:**

- **Databases**: Query Postgres, MongoDB, Cosmos DB from within the agent
- **APIs**: Call your service APIs, Jira, Slack, GitHub, PagerDuty
- **File systems**: Deep understanding of code structure, directory traversal
- **Custom tools**: Your proprietary scripts, CLI tools, build systems
- **Infrastructure**: Kubernetes API, Azure Resource Graph, AWS CloudFormation

**Status**: No longer emerging—becoming THE standard. Supported in Copilot Pro/Business/Enterprise and native in Claude Code.

**For developers**: MCP lets agents directly query your infrastructure and make informed decisions. Example: "Add monitoring to all services in the cluster" — the agent queries Kubernetes API to discover services, then adds the monitoring.

### Context Management Shortcuts

As you use Copilot and other agents, remember these shortcuts:

- **`@workspace`**: Include the entire project context
- **`@file:path/to/file.py`**: Reference specific files in chat
- **`#selection`**: Use highlighted code in chat
- **`@skill:SKILLNAME`**: Load a skill
- **Custom context via MCP**: Advanced, requires Enterprise/Pro+ and setup

---

## 11. Live Demo (Optional/Buffer) (5 min)

> **Presenter**: This section is optional. Use it if you're ahead of schedule or to showcase your personal workflow.

**Suggestion outline if you do this:**

1. **Show your AGENTS.md** (project-specific or personal)
   - Highlight: how it evolves as your project grows
   - Talk: how it reduces iteration time with Copilot

2. **Demo a task from start to finish**
   - Pick a real task from your backlog or sample project
   - Use agent mode or terminal agent to complete it
   - Show: exploration, decision-making, output
   - Highlight: how AGENTS.md and Skills guided the AI

3. **Show sub-agent architecture** (if using OpenCode or similar)
   - Different agents with different roles
   - How they collaborate
   - Demonstrate one in action if time permits

**Key takeaway**: "This is what's possible once you've mastered the basics from today. Start there, build up, and keep learning."

---

## 12. Q&A and Next Steps (5 min)

### Q&A Format

- **Open floor**: "Any questions about what we covered today?"
- **Expect questions on**:
  - License limits, overages, and planning
  - How to get Copilot approved if not yet available
  - Privacy and data concerns
  - Tool comparisons (Cursor vs. Copilot vs. Claude)
  - Integration with existing workflows
  - Edit Mode deprecation timeline

### Next Steps to Share

1. **This week**: Use completions and chat mode daily. Get comfortable with the interface.
2. **Next week**: Start using agent mode (or equivalent) for a small feature. Build confidence.
3. **Week 3-4**: Experiment with sub-agents or terminal agents on a real task.
4. **Ongoing**: Keep refining your AGENTS.md and Skills. They get better with each use.

### Resources to Provide

Handout or slide with these resources:

- 📄 **This workshop guide** (link to WORKSHOP-GUIDE.md)
- 📚 [GitHub Copilot Docs](https://docs.github.com/en/copilot)
- 📚 [Prompt Engineering Tips](https://docs.github.com/en/copilot/using-github-copilot/prompt-engineering-for-github-copilot)
- 📚 [VS Code 1.111 Release Notes](https://github.com/microsoft/vscode/releases) (Agent Mode, Edit Mode deprecation)
- 🤖 [OpenCode Agent Framework](https://github.com/opencode/opencode)
- 🤖 [Claude Code](https://claude.ai)
- 🤖 [Aider](https://aider.chat)
- 💬 [Model Context Protocol](https://modelcontextprotocol.io)
- 📝 **Next session**: "Let's meet again in 4 weeks. Bring your experiences and questions."

---

# Optional Extras

## Extra A: Security & Privacy Considerations

### What Data Does Copilot See?

- **Code context**: The files you have open and any selections you reference
- **Your prompts**: The questions you ask Copilot
- **Chat history**: Stored on GitHub servers; subject to retention policies

### Data Retention & Privacy

**For Free and Pro users:**

- Code snippets may be used to improve Copilot (unless you opt out)
- Chat history retained for 30 days by default
- You can delete chat history manually

**For Business and Enterprise:**

- Data retention policies set by your org admin
- Can be configured for no data retention, full encryption, etc.
- Audit logs available to compliance teams

### Sensitive Code & Exclusions

**Never paste into Copilot:**

- API keys, passwords, tokens
- Proprietary algorithms you can't disclose
- Security exploits or vulnerabilities you haven't patched

**Mitigation:**

- Use `AGENTS.md` to remind the AI: "Never include hardcoded secrets in examples"
- Business/Enterprise: Configure `.copilotignore` to exclude sensitive files
- Redact secrets in logs before pasting error messages
- When in doubt, don't paste it

### IP & Indemnity

**Free/Pro**: No IP indemnity — you're responsible for ensuring generated code doesn't infringe.

**Business/Enterprise**: GitHub provides IP indemnity — protected if generated code is determined to infringe (terms apply).

> **Talking point**: "For production code, especially anything novel, have a human review. AI accelerates; humans verify."

---

## Extra B: Practical Tips for Diverse Developers

### Web Backend Examples (Python/Django, Node/Express)

**Generate an API endpoint:**

```
Create a FastAPI endpoint that:
1. Accepts POST requests with user email and password
2. Validates input (email format, password strength)
3. Hashes the password using bcrypt
4. Stores the user in PostgreSQL
5. Returns JWT token on success
6. Returns 400 for validation errors, 409 for duplicate email

Include error handling, logging, and docstrings.
```

**Generate a database migration:**

```
Write a Django migration that:
1. Adds a `verification_token` field to the User model
2. Adds a `verified_at` timestamp field
3. Creates an index on `verification_token`
4. Sets a default value for existing users (empty string)

Use Django's migration framework.
```

### Frontend Examples (React, Vue, Angular)

**Generate a React component:**

```
Create a React component that:
- Displays a paginated list of products
- Shows a loading spinner while fetching from /api/products?page=N
- Handles errors with a user-friendly message
- Has "Previous" and "Next" buttons
- Shows current page number
- Uses React hooks (useState, useEffect)
- Includes TypeScript types

Include prop validation and unit tests.
```

### Mobile Examples (React Native, Flutter)

**Generate a React Native screen:**

```
Create a React Native screen that:
- Displays user profile information
- Fetches data from /api/users/:id
- Shows a loading indicator
- Has an "Edit Profile" button
- Handles network errors gracefully

Include TypeScript types.
```

### Infrastructure Examples (Terraform, Kubernetes, Docker)

**Generate a Terraform module:**

```
Create a Terraform module that manages an AWS RDS PostgreSQL instance:
- Configurable instance type, storage, backup retention
- Private security group (no public access)
- Monitoring with CloudWatch
- Parameter group for performance tuning
- Automated snapshots

Include variables, outputs, and documentation.
```

**Generate a Kubernetes manifest:**

```
Create a Kubernetes Deployment that:
- Deploys a Node.js web server (3 replicas)
- Uses image from ECR: 123456789.dkr.ecr.us-east-1.amazonaws.com/myapp:latest
- Exposes port 3000
- Has CPU/memory requests and limits
- Includes a liveness probe (HTTP GET /health)
- Uses a ConfigMap for environment variables
- Uses Secrets for database credentials

Include YAML with inline comments.
```

### Data & Analytics Examples (SQL, Python, dbt)

**Generate a SQL query:**

```
Write a SQL query that:
1. Joins users, orders, and order_items tables
2. Calculates total revenue per customer in last quarter
3. Filters for customers with > $5000 revenue
4. Ranks by revenue (highest first)
5. Includes customer email and order count

Handle NULLs and edge cases.
```

### DevOps & CI/CD Examples (GitHub Actions, GitLab CI)

**Generate a GitHub Actions workflow:**

```
Create a GitHub Actions workflow that:
1. On push to main: run tests, build Docker image, push to ECR
2. On release tag: deploy to production via Terraform
3. All failures: post to Slack with error details
4. Track deployment status

Include Azure authentication, secret management, conditional steps.
```

---

## Extra C: Common Pitfalls & Anti-Patterns

### 1. The "Trust Everything" Trap 🚫

**Problem**: AI generates confident-looking code with subtle bugs.

**Examples:**

- Terraform resource without proper error handling or destroy prevention
- Kubernetes manifest with overly permissive RBAC
- SQL queries with N+1 problems
- Bash scripts that fail on spaces in filenames
- React component without error boundaries

**Solution:**

- Always review generated code
- Run tests before merging
- For infrastructure: `terraform plan` before apply
- For Kubernetes: validate against your security policies
- For scripts: test in dev/staging first
- For frontend: test in staging with real data

**Mantra**: "It compiled" ≠ "It's correct"

### 2. The "Prompt and Pray" Pattern 🚫

**Problem**: Vague prompt, hope the AI reads your mind.

**Example:**

```
❌ "make it better"
✅ "this function processes 10k records synchronously.
    Refactor to use async/await with batching for 10x throughput.
    Keep error handling and logging."
```

**Solution**: Be specific. Include context. Iterate.

### 3. The "Context Dump" Overload 🚫

**Problem**: Paste 5,000 lines of code and a 1,000-line log file.

**Solution:**

- Paste the RELEVANT snippet (50-100 lines)
- Describe what you're trying to do
- Include the exact error message or expected vs. actual
- If logs are huge, paste the relevant part (first error, last 50 lines)
- Use `@file:` or `#selection` to reference without pasting

### 4. Copy-Paste Without Understanding 🚫

**Problem**: Ship code you don't understand. It breaks; you can't debug.

**Example**: Using an AI-generated Helm chart without understanding the pod security context changes it made.

**Solution**: Read the code. Understand what it does. If you can't explain it to someone, you can't ship it.

### 5. Ignoring the Budget 🚫

**Problem**: Burning through premium requests on simple tasks.

**Example**: Using Agent mode to rename a variable (Chat mode would suffice).

**Solution:**

- Match the tool to the task
- Simple questions: Chat mode (often free)
- Small refactors: Chat with selection (cheap)
- Complex features: Agent mode (expensive, use wisely)

### 6. Fighting the AI Instead of Guiding It 🚫

**Problem**: Repeating the same prompt expecting different results.

**Solution:**

- If the first try is wrong, don't repeat the prompt
- Add context: "That's wrong because [specific reason]"
- Try a different approach: "Can you use [alternative method]?"
- Switch modes or models if available
- Update your AGENTS.md if it's a project pattern issue

### 7. Skipping the Instruction Files 🚫

**Problem**: Every session starts from zero. AI gives generic suggestions that don't match your project.

**Solution**: Invest 30 minutes in a good AGENTS.md. Saves hours downstream.

### 8. The "AI Should Write All Tests" Misconception 🚫

**Problem**: AI generates tests that mirror the implementation (not useful).

**Solution:**

- You define the test cases (what should happen)
- AI can scaffold the test structure
- You verify the test actually tests behavior, not just code

### 9. Using AI for Security Code Without Expert Review 🚫

**Problem**: AI generates auth flows, encryption, access control. You ship it. It fails an audit.

**Solution:**

- AI can help draft security code
- MUST have expert human review
- For: auth, encryption, secrets, access control, compliance code
- Test in staging with threat modeling

### 10. Not Keeping Up With Your Tools 🚫

**Problem**: These tools update weekly. Features you tried 3 months ago now work better.

**Solution:**

- Follow release notes
- Revisit tools quarterly
- Try new features on small tasks first
- Learn from others: Twitter, blogs, communities
- Note: Edit Mode is deprecated as of VS Code 1.111; start using Chat mode with selection

---

# Resources & Further Reading

### Official Documentation

- [GitHub Copilot Docs](https://docs.github.com/en/copilot) — Start here
- [VS Code 1.111 Release Notes](https://github.com/microsoft/vscode/releases) — Agent Mode, Edit Mode deprecation
- [Copilot in VS Code](https://code.visualstudio.com/docs/copilot/overview)
- [Prompt Engineering Guide](https://docs.github.com/en/copilot/using-github-copilot/prompt-engineering-for-github-copilot)
- [Custom Instructions for Copilot](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot)

### AI Coding Tools & Frameworks

- [GitHub Copilot](https://github.com/features/copilot) — VS Code, JetBrains, Neovim
- [ChatGPT](https://chat.openai.com) — Web interface, Codex agent
- [Claude.ai](https://claude.ai) — Anthropic's interface, Claude Code agent
- [Cursor](https://cursor.sh) — AI-first IDE
- [OpenCode](https://github.com/opencode/opencode) — Open-source agent framework
- [Aider](https://aider.chat) — Git-aware terminal agent
- [GitHub Copilot CLI](https://docs.github.com/en/copilot/github-copilot-cli) — Terminal integration

### Emerging Standards

- [Model Context Protocol (MCP)](https://modelcontextprotocol.io) — Agent interoperability standard

### Community & Learning

- [GitHub Copilot Community](https://github.com/github-copilot)
- [Prompt Engineering for Developers](https://www.deeplearning.ai/) (free course)
- [Anthropic Research](https://www.anthropic.com/research) — AI reasoning and safety

### Best Practices by Domain

- [Terraform Best Practices](https://www.terraform.io/language/best-practices)
- [Kubernetes Security](https://kubernetes.io/docs/concepts/security/)
- [React Best Practices](https://react.dev)
- [Python Coding Standards](https://pep8.org)
- [SQL Performance Tips](https://use-the-index-luke.com)

---

# Changelog

| Version | Date | Changes |
|---------|------|---------|
| 0.2.0 | 2026-03-15 | Extended to 120 min, broadened audience to all developers, updated AI landscape (VS Code 1.111, Edit Mode deprecation, MCP standard), added AI subscriptions comparison, added Skills section, removed co-presenter names |
| 0.1.0 | 2026-02-18 | Initial draft — 90 min agenda, platform engineer focus, complete examples, hands-on exercises |

---

**Last updated**: 2026-03-15  
**Status**: Ready for delivery  
**Feedback**: Share suggestions via GitHub Issues or direct communication

---

*"Your AI pair programmer is here. The interface has changed. Execution is the new frontier. Now go build something great."*
