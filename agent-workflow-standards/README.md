🤖 Agent-Workflow-Standards
A standardized framework to turn "unruly" AI chat sessions into disciplined, high-quality Agentic Workflows.

The Problem
Most AI coding tools fail when they lack context. They ignore your coding standards, hallucinate API endpoints, and create a "technical debt mess" that you have to clean up manually.

The Solution
By using a structured .agents/ hub and a standardized docs/ layer, you provide the AI with:

Rules: Strict boundaries on code quality and execution.

Skills: Pre-defined workflows for complex tasks (like DB migrations).

Context: A single source of truth for your architecture and product goals.

📂 Repository Structure
.agents/: The brain of your agent.

rules/: Core standards (naming, security, patterns).

skills/: Task-specific "resumes" for the AI to follow.

docs/: The roadmap for your project.

Standard templates for PRDs, API Specs, and Architecture.


🛠 Templates Included
PRD: Define the "Why" using a TodoApp example.

Architecture: Map out your tech stack layers.

Skills: Use the SKILL_TEMPLATE.md to teach your AI how to handle specific parts of your stack (e.g., SQLAlchemy, Docker, or AWS).


🚀 How to Implement

1. I would suggest you to not use AI as this is the base of any project, you should know how to do it manually.
2. Go throgh the files and understand why and what of each file.
3. After understanding the templates, copy them and try to improvise it and use it on your own project.
4. Try to do it for at least 2 to 3 projects, do it manually and you will automatically get hang of it.
5. Repeat.

Built for developers who want to spend more time shipping and less time fixing AI hallucinations.