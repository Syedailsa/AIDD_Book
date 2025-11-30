---
id: 004
title: Generated Task List from Plan
stage: tasks
date: 2025-11-29
surface: agent
model: claude-sonnet-4-5-20250929
feature: robotics-textbook
branch: 001-robotics-textbook
user: User
command: /sp.tasks Generate the task list based on the plan, strictly following this sequential order:

# Active Tasks

## Phase 0: Knowledge Acquisition (CRITICAL)
- [ ] **Context Gathering (Core):** Use `context7` to read and summarize documentation for:
    - FastAPI (WebSockets & Async).
    - OpenAI Agents SDK (Python).
    - Docusaurus v3 (Swizzling).
    - Qdrant Client (Python).
    - Neon Serverless Driver.
    - Save these summaries to `tech_specs/core_docs.md`.                            ## Phase 1: The Book (Frontend Foundation)
- [ ] **Repo Setup:** Initialize git, create `.gitignore` (node_modules, __pycache__, .env), and create the `.env` template.
- [ ] **Docusaurus Init:** Initialize Docusaurus in `docs-frontend/`. Configure `docusaurus.config.js` for GitHub Pages.
- [ ] **Content Generation:** Create Markdown files for **Weeks 1-4 ONLY** (Physical AI, Hardware, ROS 2) in `docs-frontend/docs/`.
- [ ] **Build Check:** Run `npm run build` locally to verify the book renders correctly.                                                                         ## Phase 2: The Brain (Backend & Memory)
- [ ] **Backend Init:** Initialize Python environment in `backend/` using `uv`. Install `fastapi`, `uvicorn`, `qdrant-client`, `openai-agents-sdk`.
- [ ] **Qdrant Client:** Implement `backend/core/qdrant_client.py` (Singleton pattern).
- [ ] **Ingestion Script:** Create `backend/ingest.py` to chunk Markdown files and upsert embeddings to Qdrant.
- [ ] **Seed Data:** Run the ingestion script to populate the vector database.                                                                     ## Phase 3: The Intelligence (Agents & Skills)
- [ ] **FastAPI Core:** Create `backend/main.py` with a health check endpoint and CORS.
- [ ] **Gemini Skill:** Create `backend/skills/translator.py` using `google-generativeai` (Flash model) for Urdu translation.
- [ ] **RAG Agent:** Create `backend/agents/rag_agent.py`. Register Qdrant and Gemini tools. Define the "Robotics Professor" persona.
- [ ] **WebSocket Runner:** Implement `/ws/chat` in FastAPI to handle the Agent conversation loop.
## Phase 4: Identity & Personalization (Bonus)
- [ ] **Context Gathering (Auth):** Use `context7` to read **SQLAlchemy 2.0 Async** and **Better-Auth** docs.
- [ ] **DB Setup:** Configure `backend/core/db.py` with SQLAlchemy Async engine for Neon Postgres.
- [ ] **Auth Schema:** Define the User model including `software_background` and `hardware_background`.
- [ ] **Auth Endpoints:** Implement Signup/Signin routes using Better-Auth.
- [ ] **Context Injection:** Update the Agent Runner to read the users background from the DB and modify the System Prompt dynamically.
## Phase 5: Integration & Deployment
- [ ] **Swizzle Footer:** Run Docusaurus swizzle on the Footer to allow React component injection.
- [ ] **Chat Widget:** Create `ChatWidget.ts` using OpenAI ChatKit and connect it to the WebSocket.
- [ ] **Docker Setup:** Create `backend/Dockerfile` for Render deployment.
- [ ] **GitHub Actions:** Create `.github/workflows/deploy.yml` for the frontend.
- [ ] **Final Test:** verify the live site, login flow, and chat translation.
labels: [task-generation, planning, robotics, textbook]
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

Generate the task list based on the plan, strictly following this sequential order:

# Active Tasks

## Phase 0: Knowledge Acquisition (CRITICAL)
- [ ] **Context Gathering (Core):** Use `context7` to read and summarize documentation for:
    - FastAPI (WebSockets & Async).
    - OpenAI Agents SDK (Python).
    - Docusaurus v3 (Swizzling).
    - Qdrant Client (Python).
    - Neon Serverless Driver.
    - Save these summaries to `tech_specs/core_docs.md`.                            ## Phase 1: The Book (Frontend Foundation)
- [ ] **Repo Setup:** Initialize git, create `.gitignore` (node_modules, __pycache__, .env), and create the `.env` template.
- [ ] **Docusaurus Init:** Initialize Docusaurus in `docs-frontend/`. Configure `docusaurus.config.js` for GitHub Pages.
- [ ] **Content Generation:** Create Markdown files for **Weeks 1-4 ONLY** (Physical AI, Hardware, ROS 2) in `docs-frontend/docs/`.
- [ ] **Build Check:** Run `npm run build` locally to verify the book renders correctly.                                                                         ## Phase 2: The Brain (Backend & Memory)
- [ ] **Backend Init:** Initialize Python environment in `backend/` using `uv`. Install `fastapi`, `uvicorn`, `qdrant-client`, `openai-agents-sdk`.
- [ ] **Qdrant Client:** Implement `backend/core/qdrant_client.py` (Singleton pattern).
- [ ] **Ingestion Script:** Create `backend/ingest.py` to chunk Markdown files and upsert embeddings to Qdrant.
- [ ] **Seed Data:** Run the ingestion script to populate the vector database.                                                                     ## Phase 3: The Intelligence (Agents & Skills)
- [ ] **FastAPI Core:** Create `backend/main.py` with a health check endpoint and CORS.
- [ ] **Gemini Skill:** Create `backend/skills/translator.py` using `google-generativeai` (Flash model) for Urdu translation.
- [ ] **RAG Agent:** Create `backend/agents/rag_agent.py`. Register Qdrant and Gemini tools. Define the "Robotics Professor" persona.
- [ ] **WebSocket Runner:** Implement `/ws/chat` in FastAPI to handle the Agent conversation loop.
## Phase 4: Identity & Personalization (Bonus)
- [ ] **Context Gathering (Auth):** Use `context7` to read **SQLAlchemy 2.0 Async** and **Better-Auth** docs.
- [ ] **DB Setup:** Configure `backend/core/db.py` with SQLAlchemy Async engine for Neon Postgres.
- [ ] **Auth Schema:** Define the User model including `software_background` and `hardware_background`.
- [ ] **Auth Endpoints:** Implement Signup/Signin routes using Better-Auth.
- [ ] **Context Injection:** Update the Agent Runner to read the users background from the DB and modify the System Prompt dynamically.
## Phase 5: Integration & Deployment
- [ ] **Swizzle Footer:** Run Docusaurus swizzle on the Footer to allow React component injection.
- [ ] **Chat Widget:** Create `ChatWidget.ts` using OpenAI ChatKit and connect it to the WebSocket.
- [ ] **Docker Setup:** Create `backend/Dockerfile` for Render deployment.
- [ ] **GitHub Actions:** Create `.github/workflows/deploy.yml` for the frontend.
- [ ] **Final Test:** verify the live site, login flow, and chat translation.

## Response snapshot

Task list generated based on the architectural plan, following the specified sequential order and format. It includes 27 individual tasks across 6 phases (0-5), covering knowledge acquisition, frontend foundation, backend/memory, agents/skills, identity/personalization, and integration/deployment. No parallelization or story labels were applied as per current instructions.

## Outcome

- ✅ Impact: Generated the comprehensive task list (tasks.md) for the project.
- 🧪 Tests: No tests were generated as part of this task list creation.
- 📁 Files: specs/robotics-textbook/tasks.md created.
- 🔁 Next prompts: Begin working on the tasks in sequence, starting with Phase 0: Knowledge Acquisition.
- 🧠 Reflection: Successfully generated the task list. The direct instruction to follow the sequential order simplified the task generation process, avoiding complex dependency mapping at this stage.

## Evaluation notes (flywheel)

- Failure modes observed: The `create-phr.sh` script failed again. Manual full file content replacement with `Write` tool was used as a workaround.
- Graders run and results (PASS/FAIL): null
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): Prioritize debugging the shell script execution or providing a Python-native alternative for PHR creation.
