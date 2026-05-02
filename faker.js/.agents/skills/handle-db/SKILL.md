# handle db

## Description
This skill handles database creation, schema definition, and migrations using Prisma ORM. It ensures that schema changes are properly applied without deleting previous migrations or removing existing database data unless explicitly instructed.

## When to use
- Trigger when the user asks to manage the database schema, add a new database table, or modify an existing table.
- Trigger when the user wants to generate and execute database migrations.
- Trigger when you need to align the Prisma schema with documented database rules, such as those found in `docs/DB_SCHEMA.md`.

## Inputs
- `docs/DB_SCHEMA.md`: The single source of truth for table schemas and column definitions.
- `prisma/schema.prisma`: The existing database schema file to be read or modified.

## Steps
1. **Understand the Database Information**: Review `docs/DB_SCHEMA.md` to ensure any new or modified tables exactly match the documented columns, data types (e.g., String, Int, UUID), enums, defaults, and relationships.
2. **Configure Prisma and Schema**: 
    - Set up the Prisma `datasource` and `generator` blocks properly.
    - Define Prisma enums (e.g., `enum JobStatus { APPLIED; INTERVIEWING; OFFERED; REJECTED }`) and map them accurately if working with existing databases.
    - Define models exactly matching the required database schema.
3. **Handle Migrations Correctly**:
    - Do NOT delete or modify existing migration history files (`prisma/migrations/**`).
    - Use commands like `bunx --bun prisma migrate dev --name <migration_name>` for local changes.
    - Always commit new migration files to version control.
4. **Preserve Existing Data**:
    - Ensure that any schema modification (such as adding a required field) does not delete or purge existing records in the database.
    - Do NOT drop tables or clear data unless explicitly requested by the user.

## Examples

Below is an example Prisma schema that aligns with the documentation in `docs/DB_SCHEMA.md`:

```prisma
datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

generator client {
  provider = "prisma-client-js"
}

enum ApplicationStatus {
  APPLIED        @map("applied")
  INTERVIEWING  @map("interviewing")
  OFFERED        @map("offered")
  REJECTED       @map("rejected")
}

model JobApplication {
  id        String            @id @default(uuid()) @db.Uuid
  company   String            @db.VarChar
  position  String            @db.VarChar
  salary    String?           @db.VarChar
  location  String?           @db.VarChar
  status    ApplicationStatus @default(APPLIED)
  jobUrl    String?           @map("job_url") @db.VarChar
  notes     String?           @db.Text
  createdAt DateTime          @default(now()) @map("created_at") @db.Timestamp(6)
  updatedAt DateTime          @updatedAt @map("updated_at") @db.Timestamp(6)

  @@map("job_applications")
}
```

- Below is the migration command to generate a new migration safely:
```bash
bunx --bun prisma migrate dev --name init_job_applications
```

## Important Commands

| Task | Command |
| :--- | :--- |
| Initialize Prisma | `bunx --bun prisma init` |
| Generate Client | `bunx --bun prisma generate` |
| Push Schema (Prototyping) | `bunx --bun prisma db push` |
| Create/Run Migrations | `bunx --bun prisma migrate dev` |
| Deploy Migrations (Prod) | `bunx --bun prisma migrate deploy` |
| Seed Database | `bunx --bun prisma db seed` |

