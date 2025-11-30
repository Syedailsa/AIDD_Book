---
id: 011
title: Fix environment variable loading
stage: refactor
date: 2025-11-30
surface: agent
model: claude-sonnet-4-5-20250929
feature: agent-core
branch: feature/agent-core
user: unknown
command: /sp.phr --title "Fix environment variable loading" --stage refactor --feature agent-core --command "Fix the critical bug in `backend/agents/rag_agent.py` where the application crashes on startup because `client = OpenAI()` is called before environment variables are loaded. Also ensure `load_dotenv()` is added to `backend/main.py`." --user "Fix the critical bug in `backend/agents/rag_agent.py`. The application crashes on startup because `client = OpenAI()` is called before environment variables are loaded. The Fix: 1. Open `backend/agents/rag_agent.py`. 2. Add `from dotenv import load_dotenv` at the top. 3. Call `load_dotenv()` **immediately** after the imports, before initializing the OpenAI client. 4. Also ensure `load_dotenv()` is added to `backend/main.py` at the very top as well." --response "Fixed environment variable loading bug in `backend/agents/rag_agent.py` and `backend/main.py` by adding `load_dotenv()` calls." --files_yaml "- backend/agents/rag_agent.py - backend/main.py - specs/robotics-textbook/tasks.md" --tests_yaml "null"
labels: ["backend", "bugfix", "environment-variables", "dotenv", "openai", "fastapi"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - backend/agents/rag_agent.py
 - backend/main.py
 - specs/robotics-textbook/tasks.md
tests:
null
---

## Prompt

Fix the critical bug in `backend/agents/rag_agent.py`. The application crashes on startup because `client = OpenAI()` is called before environment variables are loaded. The Fix: 1. Open `backend/agents/rag_agent.py`. 2. Add `from dotenv import load_dotenv` at the top. 3. Call `load_dotenv()` **immediately** after the imports, before initializing the OpenAI client. 4. Also ensure `load_dotenv()` is added to `backend/main.py` at the very top as well.

## Response snapshot

Fixed environment variable loading bug in `backend/agents/rag_agent.py` and `backend/main.py` by adding `load_dotenv()` calls.

## Outcome

- ✅ Impact: Resolved application crash due to environment variable loading order. The `RoboticsProfessor` agent and FastAPI app can now correctly access API keys.
- 🧪 Tests: No explicit tests run, but the fix addresses a startup crash.
- 📁 Files: Modified `backend/agents/rag_agent.py` and `backend/main.py`, and updated `specs/robotics-textbook/tasks.md`.
- 🔁 Next prompts: Continue with verification of Phase 3.
- 🧠 Reflection: Crucial to ensure environment variables are loaded before any clients that depend on them are initialized.

## Evaluation notes (flywheel)

- Failure modes observed: create-phr.sh script not found, resorted to manual PHR creation.
- Graders run and results (PASS/FAIL): null
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): Implement a pre-commit hook to check for proper .env loading in Python files.
