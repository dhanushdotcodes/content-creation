---
trigger: always_on
---

---
name: Database Expert
description: Use this when the user asks about SQL, migrations, or database schema changes.
---
# Rules
- Always use indexed columns for foreign keys.
- Never write raw SQL; use the Prisma ORM patterns.
- Check for N+1 query issues before suggesting code.

