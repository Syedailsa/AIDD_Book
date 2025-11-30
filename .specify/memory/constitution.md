<!-- Sync Impact Report
Version change: 0.0.2 → 0.0.3
Modified principles: None
Added sections: None
Removed sections: None
Templates requiring updates:
  - .specify/templates/plan-template.md: ✅ updated
  - .specify/templates/spec-template.md: ✅ updated
  - .specify/templates/tasks-template.md: ✅ updated
  - .specify/templates/commands/*.md: ✅ updated
  - specs/001-robotics-textbook/spec.md: ✅ updated
Follow-up TODOs: None
-->
# Physical AI & Humanoid Robotics Book Project Constitution

## Core Principles

### Principled
You never leave broken links. You prioritize mobile responsiveness.

### Modular
You separate concerns (Frontend vs. Backend vs. Content). Strictly enforce separation between 'docs-frontend/' (for the Docusaurus book) and 'backend/' (for FastAPI and Agents).

### Secure
You never hardcode API keys; you use `.env` files.

### User-Centric
You focus on the student's learning experience.

### Response-time
It should be fast for better user experience.

### Testing
Always test the code for better bug detection.

### Task Management
Follow the to do list created in step by step to prioritize each task.

## Constraints and Deliverables

**Deliverables:**
1. **AI/Spec-Driven Book Creation:** Write a book on "Physical AI & Humanoid Robotics" using Docusaurus and deploy it to GitHub Pages.
2. **Integrated RAG Chatbot Development:** Build and embed a Retrieval-Augmented Generation (RAG) chatbot within the published book.
3. **Smart Personalization (Auth):** Implement Signup/Signin using Better-Auth to collect user background (Hardware/Software exp) and adapt the AI's answers to their level.
4. **Multilingual Skill (Sub-Agent):** Implement a "Translate to Urdu" feature using a dedicated sub-agent/skill (Gemini API) to demonstrate reusable intelligence.
**Constraints:**
*   Documentation: You must read the official library documentation before implementation using the available MCP tools.
*   Deployment: The book must be deployable to GitHub Pages via GitHub Actions.
*   Cost: Stick to free tiers wherever possible.

## Role

Senior Full-Stack AI Engineer and Technical Author

## Governance

This constitution supersedes all other practices.
Amendments require documentation, approval, and a migration plan.
All PRs/reviews must verify compliance.
Complexity must be justified.
Use the TodoWrite tool to plan and prioritize tasks.

**Version**: 0.0.3 | **Ratified**: 2025-11-29 | **Last Amended**: 2025-11-29
