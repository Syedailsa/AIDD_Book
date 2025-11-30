---
id: 001
title: Created Architectural Plan for Robotics Textbook
stage: plan
date: 2025-11-29
surface: agent
model: claude-sonnet-4-5-20250929
feature: robotics-textbook
branch: 001-robotics-textbook
user: User
command: /sp.plan create the plan to implement the following detailed technical roadmap:

Technical Implementation Plan
1. Technological Stack & Architecture
Frontend: Docusaurus v3 (React) with swizzled components for OpenAI ChatKit integration.
Backend Runtime: Python 3.12+ managed via uv (Astral).

API Framework: FastAPI (Async/Await) with WebSockets support.

Intelligence Layer:

Orchestrator: OpenAI Agents SDK.

Translation Tool: Google Gemini API (gemini-2.5-flash).

Embeddings: OpenAI text-embedding-3-small.                                            Data Persistence:

Vector Store: Qdrant Cloud (Free Tier).

Relational DB: Neon Serverless Postgres (Free Tier).

Authentication: Better-Auth (Python) with custom schema extensions.

Deployment: GitHub Actions (Frontend) and Localhost/Render (Backend).

Phase 1: Environment, Security & Foundation
Goal: Establish a secure, documented, and modular project environment.

1.1 Repository Initialization: Initialize the Git repository and configure .gitignore to strictly exclude .env, __pycache__, and node_modules.                                                                               1.2 Secure Environment Setup:

Create a .env file containing strictly sensitive credentials: OPENAI_API_KEY, GEMINI_API_KEY, QDRANT_URL, QDRANT_API_KEY, DATABASE_URL, and BETTER_AUTH_SECRET.

Initialize the backend environment using uv inside the backend/ directory.

Context Task: Use context7 MCP to read documentation for Docusaurus, FastAPI, OpenAI Agents SDK, openai ChatKit, Qdrant, Better-Auth, and Neon.

1.3 Docusaurus Scaffold:

Initialize the Docusaurus project in docs-frontend/.                                     Configure docusaurus.config.js with the url and baseUrl specifically for GitHub Pages deployment.

1.4 Syllabus Content Generation: Populate docs-frontend/docs/ with structured Markdown content covering only Weeks 1-4 (Physical AI Intro, Hardware, ROS 2, Bridge) as defined in the specification add a slide bar for topics and chapters easy navigation.

Phase 2: RAG Pipeline & Vector Ingestion
Goal: Transform the book content into a retrievable vector format.

2.1 Qdrant Client Service: Create backend/core/qdrant_client.py. Implement a singleton pattern to manage the connection to Qdrant Cloud, loading credentials securely from os.environ.                              2.2 Ingestion Engine (ingest.py):

Implement a script to recursively scan docs-frontend/docs/.

Use available Qdrant logic to chunk text based on Markdown headers (#, ##).

Generate vector embeddings using OpenAI text-embedding-3-small.

Upsert payloads (Text + Metadata + Vector) into a dedicated Qdrant collection.

2.3 Data Seeding: Execute ingest.py to seed the vector database with the Week 1-4 content.

Phase 3: Agent Backend & Skills Integration
Goal: Build the reasoning engine and cost-effective sub-agents.

3.1 FastAPI & WebSocket Core:

Create backend/main.py.

Define the root application and specific WebSocket endpoint /ws/chat for real-time bidirectional communication.

3.2 Gemini Translation Skill (Cost Optimization):

Create backend/skills/translator.py.                                      Implement translate_to_urdu(text: str) utilizing the Gemini 2.5 Flash model. This offloads translation tasks to a free-tier model to save OpenAI tokens.

3.3 Agent Orchestration:

Create backend/agents/rag_agent.py using the OpenAI Agents SDK.

Define the RAG Tool: A function that queries Qdrant and returns context.

Define the Translation Tool: Register the Gemini function as an Agent Tool.

Construct the System Prompt to enforce the persona of a "Helpful Robotics Professor."

3.4 WebSocket Runner: Implement the runner loop in FastAPI that instantiates the Agent, handles the message stream, and maintains the immediate session context.                                               Phase 4: Frontend Integration & Bonus Features
Goal: Deliver the UI, Authentication, and Personalization logic.

4.1 Neon DB & Schema:

Configure backend/core/db.py to connect to Neon Postgres.

Define the User Schema to include standard fields plus software_background (Text) and hardware_background (Text).

4.2 Better-Auth Integration:

Implement Better-Auth logic in FastAPI to handle signup and signin routes.

Ensure the Signup flow accepts and stores the custom background fields in Neon.

4.3 Component Swizzling: Run the Docusaurus swizzle command on the Footer or Root component to allow the injection of the Global Chat Provider.

4.4 ChatKit Integration:                                                           Create docs-frontend/src/components/ChatWidget.js using the OpenAI ChatKit React SDK.

Connect the widget to the backend via the /ws/chat WebSocket.

4.5 Dynamic Personalization:

Modify the Backend Agent Runner (Phase 3.4).

On connection, retrieve the authenticated users profile from Neon.

Inject the software_background and hardware_background into the Agents instructions (e.g., "The user is a Python Expert but new to Electronics. Adjust explanations accordingly.").                                                                     4.6 Deployment Workflow: Create a .github/workflows/deploy.yml file to build the Docusaurus static site and deploy it to the gh-pages branch.
labels: [architecture, planning, robotics, textbook]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - specs/robotics-textbook/plan.md
tests:

---

## Prompt

create the plan to implement the following detailed technical roadmap:

Technical Implementation Plan
1. Technological Stack & Architecture
Frontend: Docusaurus v3 (React) with swizzled components for OpenAI ChatKit integration.
Backend Runtime: Python 3.12+ managed via uv (Astral).

API Framework: FastAPI (Async/Await) with WebSockets support.

Intelligence Layer:

Orchestrator: OpenAI Agents SDK.

Translation Tool: Google Gemini API (gemini-2.5-flash).

Embeddings: OpenAI text-embedding-3-small.                                            Data Persistence:

Vector Store: Qdrant Cloud (Free Tier).

Relational DB: Neon Serverless Postgres (Free Tier).

Authentication: Better-Auth (Python) with custom schema extensions.

Deployment: GitHub Actions (Frontend) and Localhost/Render (Backend).

Phase 1: Environment, Security & Foundation
Goal: Establish a secure, documented, and modular project environment.

1.1 Repository Initialization: Initialize the Git repository and configure .gitignore to strictly exclude .env, __pycache__, and node_modules.                                                                               1.2 Secure Environment Setup:

Create a .env file containing strictly sensitive credentials: OPENAI_API_KEY, GEMINI_API_KEY, QDRANT_URL, QDRANT_API_KEY, DATABASE_URL, and BETTER_AUTH_SECRET.

Initialize the backend environment using uv inside the backend/ directory.

Context Task: Use context7 MCP to read documentation for Docusaurus, FastAPI, OpenAI Agents SDK, openai ChatKit, Qdrant, Better-Auth, and Neon.

1.3 Docusaurus Scaffold:

Initialize the Docusaurus project in docs-frontend/.                                     Configure docusaurus.config.js with the url and baseUrl specifically for GitHub Pages deployment.

1.4 Syllabus Content Generation: Populate docs-frontend/docs/ with structured Markdown content covering only Weeks 1-4 (Physical AI Intro, Hardware, ROS 2, Bridge) as defined in the specification add a slide bar for topics and chapters easy navigation.

Phase 2: RAG Pipeline & Vector Ingestion
Goal: Transform the book content into a retrievable vector format.

2.1 Qdrant Client Service: Create backend/core/qdrant_client.py. Implement a singleton pattern to manage the connection to Qdrant Cloud, loading credentials securely from os.environ.                              2.2 Ingestion Engine (ingest.py):

Implement a script to recursively scan docs-frontend/docs/.

Use available Qdrant logic to chunk text based on Markdown headers (#, ##).

Generate vector embeddings using OpenAI text-embedding-3-small.

Upsert payloads (Text + Metadata + Vector) into a dedicated Qdrant collection.

2.3 Data Seeding: Execute ingest.py to seed the vector database with the Week 1-4 content.

Phase 3: Agent Backend & Skills Integration
Goal: Build the reasoning engine and cost-effective sub-agents.

3.1 FastAPI & WebSocket Core:

Create backend/main.py.

Define the root application and specific WebSocket endpoint /ws/chat for real-time bidirectional communication.

3.2 Gemini Translation Skill (Cost Optimization):

Create backend/skills/translator.py.                                      Implement translate_to_urdu(text: str) utilizing the Gemini 2.5 Flash model. This offloads translation tasks to a free-tier model to save OpenAI tokens.

3.3 Agent Orchestration:

Create backend/agents/rag_agent.py using the OpenAI Agents SDK.

Define the RAG Tool: A function that queries Qdrant and returns context.

Define the Translation Tool: Register the Gemini function as an Agent Tool.

Construct the System Prompt to enforce the persona of a "Helpful Robotics Professor."

3.4 WebSocket Runner: Implement the runner loop in FastAPI that instantiates the Agent, handles the message stream, and maintains the immediate session context.                                               Phase 4: Frontend Integration & Bonus Features
Goal: Deliver the UI, Authentication, and Personalization logic.

4.1 Neon DB & Schema:

Configure backend/core/db.py to connect to Neon Postgres.

Define the User Schema to include standard fields plus software_background (Text) and hardware_background (Text).

4.2 Better-Auth Integration:

Implement Better-Auth logic in FastAPI to handle signup and signin routes.

Ensure the Signup flow accepts and stores the custom background fields in Neon.

4.3 Component Swizzling: Run the Docusaurus swizzle command on the Footer or Root component to allow the injection of the Global Chat Provider.

4.4 ChatKit Integration:                                                           Create docs-frontend/src/components/ChatWidget.js using the OpenAI ChatKit React SDK.

Connect the widget to the backend via the /ws/chat WebSocket.

4.5 Dynamic Personalization:

Modify the Backend Agent Runner (Phase 3.4).

On connection, retrieve the authenticated users profile from Neon.

Inject the software_background and hardware_background into the Agents instructions (e.g., "The user is a Python Expert but new to Electronics. Adjust explanations accordingly.").                                                                     4.6 Deployment Workflow: Create a .github/workflows/deploy.yml file to build the Docusaurus static site and deploy it to the gh-pages branch.

## Response snapshot

Architectural plan for the Physical AI & Humanoid Robotics Book Project created. The plan details scope, dependencies, key decisions, API contracts, NFRs, data management, operational readiness, risk analysis, and evaluation. It follows the constitution and identifies points for further clarification. The plan addresses all phases of the technical roadmap, from environment setup to frontend integration and deployment.

## Outcome

- ✅ Impact: Created the architectural plan (plan.md) for the project.
- 🧪 Tests: No tests were run in this planning phase.
- 📁 Files: specs/robotics-textbook/plan.md created.
- 🔁 Next prompts: Ask the user to run /sp.adr if they want to document the architectural decision.
- 🧠 Reflection: Successfully generated the architectural plan based on the detailed technical roadmap and project constitution. Identified areas requiring further clarification.

## Evaluation notes (flywheel)

- Failure modes observed: The `setup-plan.ps1` and `create-phr.sh` scripts failed due to `command not found`. Agent-native tool usage was successful.
- Graders run and results (PASS/FAIL): null
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): Improve error handling for missing shell commands, or provide a clearer fallback mechanism description for the `sp.plan` tool.
