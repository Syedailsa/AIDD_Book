# Architectural Plan for Physical AI & Humanoid Robotics Book Project

## 1. Scope and Dependencies

### In Scope
- **Frontend**: Docusaurus v3 (React) based book for "Physical AI & Humanoid Robotics" deployed to GitHub Pages.
- **Backend Runtime**: Python 3.12+ with uv (Astral) for environment management.
- **API Framework**: FastAPI with WebSockets for real-time communication.
- **Intelligence Layer**: OpenAI Agents SDK for orchestration, Google Gemini API (gemini-2.5-flash) for translation, OpenAI text-embedding-3-small for embeddings.
- **Data Persistence**: Qdrant Cloud (Free Tier) for vector store, Neon Serverless Postgres (Free Tier) for relational data.
- **Authentication**: Better-Auth (Python) with custom schema extensions.
- **Chatbot Integration**: OpenAI ChatKit React SDK for frontend chat widget.
- **Syllabus Content**: Markdown content for Weeks 1-4 (Physical AI Intro, Hardware, ROS 2, Bridge).
- **Deployment**: GitHub Actions for frontend, Localhost/Render for backend.
- **Features**: Repository initialization, secure environment setup, Docusaurus scaffold, syllabus content generation, Qdrant client service, ingestion engine, data seeding, FastAPI & WebSocket core, Gemini translation skill, Agent orchestration, WebSocket runner, Neon DB & schema, Better-Auth integration, component swizzling, ChatKit integration, dynamic personalization, deployment workflow.

### Out of Scope
- Full book content beyond Weeks 1-4.
- Advanced AI features beyond RAG and translation.
- Complex user management features not covered by Better-Auth's standard capabilities plus custom background fields.
- Enterprise-grade scaling or high-availability solutions beyond free-tier offerings.

### External Dependencies
- **OpenAI**: OpenAI Agents SDK, OpenAI text-embedding-3-small, OpenAI ChatKit.
- **Google**: Gemini API (gemini-2.5-flash).
- **Qdrant**: Qdrant Cloud.
- **Neon**: Neon Serverless Postgres.
- **GitHub**: GitHub Pages, GitHub Actions.
- **Render**: Backend deployment (optional, Localhost also specified).
- **Docusaurus**: Docusaurus v3 (React).
- **Better-Auth**: Python authentication library.

## 2. Key Decisions and Rationale

- **Technological Stack**: Chosen for modern development practices, AI integration capabilities, and cost-effectiveness (free tiers for Qdrant, Neon, Gemini Flash).
- **Separate Frontend/Backend Repos/Modules**: Enforces modularity and separation of concerns as per Constitution.
- **Singleton Qdrant Client**: Ensures efficient and managed connection to the vector database.
- **Markdown Header Chunking for RAG**: Leverages existing content structure for effective retrieval.
- **Gemini Flash for Translation**: Cost optimization strategy to offload expensive translation tasks from OpenAI models.
- **OpenAI Agents SDK for Orchestration**: Provides a structured framework for building AI agents with tools.
- **Custom User Schema in Neon**: Enables dynamic personalization of AI responses based on user background.
- **Better-Auth for Authentication**: Simplifies auth implementation with extensible schema.
- **Docusaurus Swizzling**: Allows seamless integration of custom React components (ChatWidget) within the Docusaurus theme.

## 3. Interfaces and API Contracts

### Public APIs
- **WebSocket Endpoint `/ws/chat`**:
    - **Inputs**: User messages, authentication tokens.
    - **Outputs**: Agent responses (text), translation results.
    - **Errors**: WebSocket connection errors, authentication failures, agent processing errors.
- **Authentication Endpoints (Better-Auth)**:
    - **Inputs**: User credentials (username/email, password), `software_background`, `hardware_background` during signup.
    - **Outputs**: Authentication tokens, user profile.
    - **Errors**: Invalid credentials, user already exists, validation errors.
- **Qdrant Client Service (Internal)**:
    - **Inputs**: Text chunks, metadata, vectors for upsert. Query vectors for retrieval.
    - **Outputs**: Status of upsert, retrieved context.
- **Gemini Translation Skill (Internal)**:
    - **Inputs**: Text string to translate.
    - **Outputs**: Translated text (Urdu).

### Versioning Strategy
- API versioning will use simple URL prefixing (e.g., `/api/v1/` for REST endpoints and `/ws/v1/chat` for WebSocket).

### Idempotency, Timeouts, Retries
- **WebSockets**: Real-time, continuous connection. Retries on connection loss will be handled by the client.
- **Authentication**: Signup/Signin operations are idempotent to a degree (creating same user fails, signing in multiple times returns same token).
- **External API Calls (OpenAI, Gemini, Qdrant)**: Implement retry mechanisms with exponential backoff (3 retries) and a 10-second timeout.

### Error Taxonomy with status codes
- **Authentication**: Standard HTTP status codes (e.g., 401 Unauthorized, 403 Forbidden, 400 Bad Request for validation errors).
- **WebSocket**: Custom error codes: 4001 for "Auth Failed" and 4002 for "Processing Error".

## 4. Non-Functional Requirements (NFRs) and Budgets

### Performance
- **p95 latency**:
    - **RAG Query**: < 500ms (goal).
    - **Agent Response**: < 2 seconds (goal, dependent on LLM response times).
    - **Translation**: < 1 second (goal).
- **Throughput**:
    - **WebSocket**: Support at least 100 concurrent users (initial target).
- **Resource caps**:
    - **Qdrant/Neon**: Stay within free tier limits. Monitor usage.

### Reliability
- **SLOs**:
    - **Uptime**: 99.9% for core services (FastAPI, Qdrant, Neon).
    - **Error Budget**: Max 0.1% for critical paths (auth, RAG query).
- **Degradation strategy**:
    - If Gemini API fails, fall back to English or inform user about translation unavailability.
    - If Qdrant fails, inform user about context retrieval failure.

### Security
- **AuthN/AuthZ**: Better-Auth for user authentication. Only a single role ("Student") is required.
- **Data handling**: Sensitive credentials via `.env` files, never hardcoded. User background data stored securely in Neon.
- **Secrets**: OPENAI_API_KEY, GEMINI_API_KEY, QDRANT_URL, QDRANT_API_KEY, DATABASE_URL, BETTER_AUTH_SECRET stored in `.env`.
- **Auditing**: Standard Python `logging` library printing to `stdout` (captured by Render logs). No external audit systems.

### Cost
- Stick strictly to free tiers for Qdrant, Neon, Gemini Flash.
- Monitor OpenAI API usage to manage costs.
- Gemini Flash for translation to optimize OpenAI token usage.

## 5. Data Management and Migration

### Source of Truth
- **Book Content**: Markdown files in `docs-frontend/docs/`.
- **Vector Embeddings**: Qdrant Cloud.
- **User Data**: Neon Serverless Postgres.
- **Credentials**: `.env` file (local), environment variables (deployment).

### Schema Evolution
- **Neon User Schema**: Managed via SQLAlchemy (Async). Schema creation strategy: Create-on-Startup (`metadata.create_all`). No Alembic migrations; schema changes during development will require table drops.
- **Qdrant Collection Schema**: Defined in `qdrant_client.py` and `ingest.py`. Updates require re-ingestion.

### Migration and Rollback
- **Data Seeding**: `ingest.py` for initial and subsequent data population.
- **Database Migrations**: Schema changes during development will require table drops and re-creation.

### Data Retention
- User data in Neon: Permanent, until user deletion.
- Vector data in Qdrant: Permanent, tied to book content versions.

## 6. Operational Readiness

### Observability
- **Logs**: Python's standard `logging` library printing to `stdout` (captured by Render logs).
- **Metrics**: Monitor API performance, WebSocket connections, agent invocations, external API calls.
- **Traces**: Not initially required; distributed tracing if microservices are introduced later.

### Alerting
- **Thresholds**: Define alerts for API errors, low resource limits (free tiers), agent failures.
- **On-call owners**: To be defined during deployment phase.

### Runbooks for common tasks
- Deployment of frontend/backend.
- Data ingestion.
- Troubleshooting agent failures.
- Database backups/restores (if applicable for free tier).

### Deployment and Rollback strategies
- **Frontend (Docusaurus)**: GitHub Actions to build and deploy to `gh-pages` branch. Rollback via reverting GitHub commits.
- **Backend (FastAPI/Agents)**: Localhost for development, Render for deployment using a Dockerfile for environment consistency. Rollback is done by re-deploying the previous GitHub commit.
- **Feature Flags and compatibility**: None required.

## 7. Risk Analysis and Mitigation

### Top 3 Risks
1.  **Cost Overruns on AI APIs**:
    - **Blast Radius**: Unexpected bills, project halted due to budget.
    - **Mitigation**: Strict monitoring of API usage, leveraging free tiers (Gemini Flash), setting usage limits on APIs, implementing caching for embeddings/translations where feasible.
2.  **Security Vulnerabilities**:
    - **Blast Radius**: Data breaches (API keys, user data), unauthorized access.
    - **Mitigation**: Use `.env` for secrets, secure authentication (Better-Auth), input validation, regular security audits (if resources permit).
3.  **Complexity of Agent Orchestration & Real-time Communication**:
    - **Blast Radius**: Difficult to debug, maintain, and extend; poor user experience.
    - **Mitigation**: Modular agent design, clear API contracts, thorough testing of WebSocket communication, comprehensive logging.

## 8. Evaluation and Validation

### Definition of Done (tests, scans)
- Unit tests for all backend services (Qdrant client, skills, agents).
- Integration tests for FastAPI endpoints and WebSocket communication.
- Frontend component tests for Docusaurus and ChatWidget.
- End-to-end tests for the RAG pipeline and personalization.
- Linting and code format checks for both frontend and backend.
- Deployment successful to GitHub Pages and Render (if applicable).

### Output Validation for format/requirements/safety
- **Agent Responses**: Ensure responses adhere to "Helpful Robotics Professor" persona.
- **Translation**: Verify accuracy of Urdu translation.
- **RAG Context**: Validate that retrieved context is relevant and accurate.
- **User Input**: Sanitize and validate all user inputs to prevent injection attacks.

## 9. Architectural Decision Record (ADR)

📋 Architectural decision detected: Choice of core technologies (Docusaurus, FastAPI, OpenAI Agents SDK, Qdrant, Neon, Better-Auth, Gemini Flash). Document reasoning and tradeoffs? Run `/sp.adr "Core Technology Stack"`

---

## Constitution Check

**Principled**:
- Mobile responsiveness: Handled by Docusaurus (✅).
- Broken links: Rely on Docusaurus's built-in `npm run build` validation.

**Modular**:
- Separation of concerns (Frontend vs. Backend vs. Content): Strictly enforced with `docs-frontend/` and `backend/` directories (✅).

**Secure**:
- Hardcoded API keys: Avoided, `.env` files used (✅).

**User-Centric**:
- Student's learning experience: Addressed via personalized AI responses and structured content (✅).

**Response-time**:
- Fast for better user experience: Performance NFRs defined, cost-saving measures in place (✅).

**Testing**:
- Always test the code for better bug detection: Defined in "Definition of Done" (✅).

**Task Management**:
- Follow the to do list created in step by step to prioritize each task: Will be used for implementation phase (✅).

## Gates Evaluation
- All defined gates are currently met.
- No immediate violations of Constitution principles.

## Phase 1: Environment, Security & Foundation
Goal: Establish a secure, documented, and modular project environment.

1.1 Repository Initialization: Initialize the Git repository and configure .gitignore to strictly exclude .env, __pycache__, and node_modules.
1.2 Secure Environment Setup:
- Create a .env file containing strictly sensitive credentials: OPENAI_API_KEY, GEMINI_API_KEY, QDRANT_URL, QDRANT_API_KEY, DATABASE_URL, and BETTER_AUTH_SECRET.
- Initialize the backend environment using uv inside the backend/ directory.
- **Context Task:** Before starting implementation, use `context7` MCP to read and summarize the latest official documentation for:
    1.  **FastAPI** (specifically WebSockets and Async patterns).
    2.  **OpenAI Agents SDK** (Python setup and Tool creation).
    3.  **OpenAI ChatKit** (React component integration).
    4.  **Docusaurus v3** (Swizzling and Client Modules and side bar for chapters and sub topics).
    5.  **Neon Postgres** (Connection strings and Driver details).

1.3 Docusaurus Scaffold:
- Initialize the Docusaurus project in docs-frontend/.
- Configure docusaurus.config.js with the url and baseUrl specifically for GitHub Pages deployment.

1.4 Syllabus Content Generation: Populate docs-frontend/docs/ with structured Markdown content covering only Weeks 1-4 (Physical AI Intro, Hardware, ROS 2, Bridge) as defined in the specification add a slide bar for topics and chapters easy navigation.

## Phase 2: RAG Pipeline & Vector Ingestion
Goal: Transform the book content into a retrievable vector format.

2.1 Qdrant Client Service: Create backend/core/qdrant_client.py. Implement a singleton pattern to manage the connection to Qdrant Cloud, loading credentials securely from os.environ.
2.2 Ingestion Engine (ingest.py):
- Implement a script to recursively scan docs-frontend/docs/.
- Use available Qdrant logic to chunk text based on Markdown headers (#, ##).
- Generate vector embeddings using OpenAI text-embedding-3-small.
- Upsert payloads (Text + Metadata + Vector) into a dedicated Qdrant collection.

2.3 Data Seeding: Execute ingest.py to seed the vector database with the Week 1-4 content.

## Phase 3: Agent Backend & Skills Integration
Goal: Build the reasoning engine and cost-effective sub-agents.

3.1 FastAPI & WebSocket Core:
- Create backend/main.py.
- Define the root application and specific WebSocket endpoint /ws/chat for real-time bidirectional communication.

3.2 Gemini Translation Skill (Cost Optimization):
- Create backend/skills/translator.py.
- Implement translate_to_urdu(text: str) utilizing the Gemini 2.5 Flash model. This offloads translation tasks to a free-tier model to save OpenAI tokens.

3.3 Agent Orchestration:
- Create backend/agents/rag_agent.py using the OpenAI Agents SDK.
- Define the RAG Tool: A function that queries Qdrant and returns context.
- Define the Translation Tool: Register the Gemini function as an Agent Tool.
- Construct the System Prompt to enforce the persona of a "Helpful Robotics Professor."

3.4 WebSocket Runner: Implement the runner loop in FastAPI that instantiates the Agent, handles the message stream, and maintains the immediate session context.

## Phase 4: Frontend Integration & Bonus Features
Goal: Deliver the UI, Authentication, and Personalization logic.

4.1 Neon DB & Schema:
* **Task:** Configure `backend/core/db.py`.
* **Constraint:** Before writing code, use `context7` to read:
    1.  **SQLAlchemy 2.0 Asyncio documentation** (to ensure modern `async`/`await` syntax and avoid legacy 1.4 patterns).
    2.  **Better-Auth Python documentation** (to understand the User schema requirements).
* **Implementation:** Use `SQLAlchemy` as the ORM. For this project, use `db.create_all()` (Create on Startup) to sync schemas instead of complex Alembic migrations to save time and reduce configuration overhead.

4.2 Better-Auth Integration:
- Implement Better-Auth logic in FastAPI to handle signup and signin routes.
- Ensure the Signup flow accepts and stores the custom background fields in Neon.

4.3 Component Swizzling: Run the Docusaurus swizzle command on the Footer or Root component to allow the injection of the Global Chat Provider.

4.4 ChatKit Integration:
- Create docs-frontend/src/components/ChatWidget.ts using the OpenAI ChatKit React SDK.
- Connect the widget to the backend via the /ws/chat WebSocket.

4.5 Dynamic Personalization:
- Modify the Backend Agent Runner (Phase 3.4).
- On connection, retrieve the authenticated users profile from Neon.
- Inject the software_background and hardware_background into the Agents instructions (e.g., "The user is a Python Expert but new to Electronics. Adjust explanations accordingly.").
4.6 Deployment Workflow: Create a .github/workflows/deploy.yml file to build the Docusaurus static site and deploy it to the gh-pages branch.
