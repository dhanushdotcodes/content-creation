# Product Requirements Document

## JobTrail

JobTrail helps you track job applications, interview stages and follow-ups in one simple dashboard.

## Core Modules
- Job Application Management - Add, Edit, Delete Job Applications.
- Job Stage Management - Add, Edit, Delete Job Stages.
- Follow-up Management - Add, Edit, Delete Follow-ups.

## Success Metrics
- Successfully adding and managing applied Job Applications.
- Ability to track the stages of the application.
- Containerisation and successful deployment of the application.
- Successful generation of fake data for testing purposes using faker.js.

## User Flow
### Core loop
- User creates a job posting information.
- User updates the stage of the job application.
- User maintains notes about the Job application

## Milestones

| Milestone | Description |
| :--- | :--- |
| **M1** | Adding rules, agents, and specifications that help in creating the project instantly. |
| **M2** | Migrating schema to the DB and running a local PostgreSQL container using Docker. |
| **M3** | Creating CRUD operations based on the user flow and DB schema. |
| **M4** | Implementing faker.js with a script in a Docker Compose YAML that ups the server with a single command in the Makefile. |
