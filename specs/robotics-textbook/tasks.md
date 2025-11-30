# Robotics Textbook Project Tasks

## Phase 0: Knowledge Acquisition (CRITICAL)
- [X] T001 Context Gathering (Core): Use `context7` to read and summarize documentation for FastAPI (WebSockets & Async). Save summary to `tech_specs/core_docs.md`
- [X] T002 Context Gathering (Core): Use `context7` to read and summarize documentation for OpenAI Agents SDK (Python). Save summary to `tech_specs/core_docs.md`
- [X] T003 Context Gathering (Core): Use `context7` to read and summarize documentation for OpenAI ChatKit (React component integration). Save summary to `tech_specs/core_docs.md`
- [X] T004 Context Gathering (Core): Use `context7` to read and summarize documentation for Docusaurus v3 (Swizzling and Client Modules and side bar for chapters and sub topics). Save summary to `tech_specs/core_docs.md`
- [X] T005 Context Gathering (Core): Use `context7` to read and summarize documentation for Qdrant Client (Python). Save summary to `tech_specs/core_docs.md`
- [X] T006 Context Gathering (Core): Use `context7` to read and summarize documentation for Better-Auth (Python authentication library). Save summary to `tech_specs/core_docs.md`
- [X] T007 Context Gathering (Core): Use `context7` to read and summarize documentation for SQLAlchemy (Asyncio). Save summary to `tech_specs/core_docs.md`
- [X] T008 Context Gathering (Core): Use `context7` to read and summarize documentation for Neon Serverless Driver. Save summary to `tech_specs/core_docs.md`

## Phase 1: The Book (Frontend Foundation) - `feature/book-v1`
- [X] T009 Repo Setup: Run `git init` to initialize the repository. Create `.gitignore` (excluding node_modules, __pycache__, .env) and the `.env` template and add remote origin: `git remote add origin https://github.com/Syedailsa/AIDD_Book.git`.
- [X] T010 Branch Setup: Create the main branch first (`git branch -M main`), then create and switch to the feature branch (`git checkout -b feature/book-v1`).
- [X] T011 Docusaurus Init: Initialize Docusaurus project in `docs-frontend/`. Configure `docusaurus.config.js` for GitHub Pages deployment.
- [X] T012 Content Generation: Create Markdown files for Weeks 1-4 ONLY (Physical AI, Hardware, ROS 2, Bridge) in `docs-frontend/docs/`.
- [X] T013 Build Check: Run `npm run build` locally to verify the book renders correctly.
- [X] T014 Verify Phase 1: Manually verify all tasks in Phase 1 are complete and functional.
- [X] T015 Git Merge: `git checkout main && git merge feature/book-v1`

## Phase 2: The Brain (Backend & Memory) - `feature/rag-backend`
- [X] T016 Git Checkout: `git checkout -b feature/rag-backend`
- [X] T017 Backend Init: Initialize Python environment in `backend/` using `uv`. Install `fastapi`, `uvicorn`, `qdrant-client`, `openai-agents`, `openai`, `google-generativeai`, `passlib`, `python-jose`, `sqlalchemy`, `asyncpg`.
- [X] T018 Qdrant Client: Implement `backend/core/qdrant_client.py` (Singleton pattern to manage connection to Qdrant Cloud).
- [X] T019 Ingestion Script: Create `backend/ingest.py` to recursively scan `docs-frontend/docs/`, chunk text based on Markdown headers, generate vector embeddings, and upsert payloads (Text + Metadata + Vector) into a dedicated Qdrant collection.
- [X] T020 Seed Data: Execute `backend/ingest.py` to seed the vector database with the Week 1-4 content.
- [X] T021 Verify Phase 2: Manually verify all tasks in Phase 2 are complete and functional.
- [X] T022 Git Merge: `git checkout main && git merge feature/rag-backend`
 
## Phase 3: The Intelligence (Agents & Skills) - `feature/agent-core`
- [X] T023 Git Checkout: `git checkout -b feature/agent-core`
- [X] T024 FastAPI Core: Create `backend/main.py` and define the root application and specific WebSocket endpoint `/ws/v1/chat` for real-time bidirectional communication.
- [X] T025 Gemini Skill: Create `backend/skills/translator.py`. Implement `translate_to_urdu(text: str)` utilizing the Gemini 2.5 Flash model.
- [X] T026 RAG Agent: Create `backend/agents/rag_agent.py` using the OpenAI Agents SDK. Define the RAG Tool (queries Qdrant) and the Translation Tool (registers the Gemini function). Construct the System Prompt to enforce the persona of a "Helpful Robotics Professor."
- [X] T027 WebSocket Runner: Implement the runner loop in FastAPI (`backend/main.py`) that instantiates the Agent, handles the message stream, and maintains the immediate session context.
- [X] T028 Verify Phase 3: Manually verify all tasks in Phase 3 are complete and functional.
- [ ] T029 Git Merge: `git checkout main && git merge feature/agent-core`

## Phase 4: Identity & Personalization (Bonus) - `feature/auth-personalization`
- [ ] T030 Git Checkout: `git checkout -b feature/auth-personalization`
- [ ] T031 Context Gathering (Auth): Use `context7` to read and summarize documentation for SQLAlchemy 2.0 Asyncio and Better-Auth Python. Save summaries to `tech_specs/auth_docs.md`
- [ ] T032 DB Setup: Configure `backend/core/db.py` to connect to Neon Postgres using SQLAlchemy (Async) engine.
- [ ] T033 Auth Schema: Define the User Schema in `backend/core/db.py` to include standard fields plus `software_background` (Text) and `hardware_background` (Text).
- [ ] T034 Auth Endpoints: Implement Better-Auth logic in FastAPI (`backend/main.py`) to handle signup and signin routes, ensuring the Signup flow accepts and stores the custom background fields in Neon.
- [ ] T035 Context Injection: Modify the Backend Agent Runner (in `backend/main.py` or `backend/agents/rag_agent.py`) to retrieve the authenticated user's profile from Neon on connection and inject `software_background` and `hardware_background` into the Agent's instructions dynamically.
- [ ] T036 Verify Phase 4: Manually verify all tasks in Phase 4 are complete and functional.
- [ ] T037 Git Merge: `git checkout main && git merge feature/auth-personalization`

## Phase 5: Integration & Deployment - `feature/ui-integration`
- [ ] T038 Git Checkout: `git checkout -b feature/ui-integration`
- [ ] T039 Swizzle Footer: Run the Docusaurus swizzle command on the Footer or Root component in `docs-frontend/` to allow the injection of the Global Chat Provider.
- [ ] T040 Chat Widget: Create `docs-frontend/src/components/ChatWidget.ts` using the OpenAI ChatKit React SDK. Connect the widget to the backend via the `/ws/v1/chat` WebSocket.
- [ ] T041 Docker Setup: Create a `backend/Dockerfile` for Render deployment to ensure environment consistency.
- [ ] T042 GitHub Actions: Create a `.github/workflows/deploy.yml` file to build the Docusaurus static site and deploy it to the `gh-pages` branch.
- [ ] T043 Final Test: Verify the live site, login flow, and chat translation functionality work as expected.
- [ ] T044 Verify Phase 5: Manually verify all tasks in Phase 5 are complete and functional.
- [ ] T045 Git Merge: `git checkout main && git merge feature/ui-integration`

