---
id: 005
title: Updated Task List with Feature Branch Workflow
stage: tasks
date: 2025-11-29
surface: agent
model: claude-sonnet-4-5-20250929
feature: robotics-textbook
branch: 001-robotics-textbook
user: User
command: /sp.tasks structure the workflow using a **Feature Branch Strategy**.

For each Phase, the workflow must be:
1. `git checkout -b feature/name`
2. Perform tasks.
3. Verify.
4. `git checkout main` && `git merge feature/name`.
**Phase Mapping:**
* **Phase 0 (Knowledge):** No branch needed. Use `context7` to read docs for FastAPI, Agents SDK, Docusaurus, Qdrant, Better-Auth.
* **Phase 1 (The Book):** Branch `feature/book-v1`. Tasks: Repo setup, Docusaurus init, Week 1-4 Content, deploy to GH Pages.
* **Phase 2 (RAG):** Branch `feature/rag-backend`. Tasks: Qdrant setup, Ingestion script (`ingest.py`), Seed data.
* **Phase 3 (Agent):** Branch `feature/agent-core`. Tasks: FastAPI setup, WebSocket, Gemini Skill, RAG Agent logic.                                    * **Phase 4 (Auth/Bonus):** Branch `feature/auth-personalization`. Tasks: Neon DB, Better-Auth, User Schema, Context injection.
* **Phase 5 (UI):** Branch `feature/ui-integration`. Tasks: Swizzle Footer, ChatKit Widget, Dockerfile.

Ensure no steps are skipped.
labels: [task-generation, planning, workflow, git, feature-branch, robotics, textbook]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - specs/robotics-textbook/tasks.md
tests:

---

## Prompt

structure the workflow using a **Feature Branch Strategy**.

For each Phase, the workflow must be:
1. `git checkout -b feature/name`
2. Perform tasks.
3. Verify.
4. `git checkout main` && `git merge feature/name`.
**Phase Mapping:**
* **Phase 0 (Knowledge):** No branch needed. Use `context7` to read docs for FastAPI, Agents SDK, Docusaurus, Qdrant, Better-Auth.
* **Phase 1 (The Book):** Branch `feature/book-v1`. Tasks: Repo setup, Docusaurus init, Week 1-4 Content, deploy to GH Pages.
* **Phase 2 (RAG):** Branch `feature/rag-backend`. Tasks: Qdrant setup, Ingestion script (`ingest.py`), Seed data.
* **Phase 3 (Agent):** Branch `feature/agent-core`. Tasks: FastAPI setup, WebSocket, Gemini Skill, RAG Agent logic.                                    * **Phase 4 (Auth/Bonus):** Branch `feature/auth-personalization`. Tasks: Neon DB, Better-Auth, User Schema, Context injection.
* **Phase 5 (UI):** Branch `feature/ui-integration`. Tasks: Swizzle Footer, ChatKit Widget, Dockerfile.

Ensure no steps are skipped.

## Response snapshot

Task list (`specs/robotics-textbook/tasks.md`) updated to incorporate the Feature Branch Strategy for each phase.

## Outcome

- ✅ Impact: Updated the task list (tasks.md) with the feature branch workflow.
- 🧪 Tests: No tests were generated or run.
- 📁 Files: specs/robotics-textbook/tasks.md updated.
- 🔁 Next prompts: The user can now proceed with the implementation, following the new workflow structure.
- 🧠 Reflection: Successfully integrated the feature branch workflow into the task list by reconstructing the file content. This approach bypasses the limitations of the `Edit` tool for complex, multi-line modifications.

## Evaluation notes (flywheel)

- Failure modes observed: `create-phr.sh` script failed again, necessitating manual PHR creation. This issue requires a dedicated fix.
- Graders run and results (PASS/FAIL): null
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): Implement a Python-native PHR creation utility or debug the shell script environment.
