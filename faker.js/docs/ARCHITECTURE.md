# Architecture

## High level components
- Bun server
- PostgreSQL DB
- Dockerized services

## Layering
---
```
├─────────────────────────────────┤
│        Server (Bun.js)           │
│    ├──────────────────────────┤  
│    │     API Routes           │
│    ├──────────────────────────┤
│    │     Services             │
│    └──────────────────────────┘
├─────────────────────────────────┤
│    Database (PostgreSQL)         │
├─────────────────────────────────┤
│       Infrastructure             │
│        Docker                  │
└─────────────────────────────────┘
```

## Principles
---
- Keep it minimal and clean.
- Keep it maintainable and scalable.
- Keep it simple.

## Data Flow
---
```
User -> API Route -> Service -> DB
```

## Key Decisions
---
| Decision | Choice | Reasoning |
| :--- | :--- | :--- |
| Bun server | Bun | High performance, built-in TypeScript support, easy to use, fast start-up time, minimal boilerplate. |
| PostgreSQL DB | PostgreSQL | Relational database with good performance and scalability, easy to use, widely adopted, good community support. |
| Dockerized services | Docker | Easy to manage |