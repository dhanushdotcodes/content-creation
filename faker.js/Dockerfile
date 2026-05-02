# --- Base ---
FROM oven/bun:1.2-alpine AS base
WORKDIR /app

# --- Development ---
FROM base AS development
# Install dependencies using cache mounts for speed
RUN --mount=type=cache,target=/root/.bun/install/cache \
    --mount=type=bind,source=package.json,target=package.json \
    --mount=type=bind,source=bun.lockb,target=bun.lockb \
    bun install --frozen-lockfile

COPY . /app
RUN bunx prisma generate

EXPOSE 3000
# Ensure migrations are applied, seeding runs, and the app starts
CMD ["sh", "-c", "bunx prisma db push && bunx prisma db seed && bun run dev"]

# --- Production Builder ---
FROM base AS builder
RUN --mount=type=cache,target=/root/.bun/install/cache \
    --mount=type=bind,source=package.json,target=package.json \
    --mount=type=bind,source=bun.lockb,target=bun.lockb \
    bun install --frozen-lockfile --production

COPY . /app
RUN bunx prisma generate

# --- Production Final ---
FROM oven/bun:1.2-alpine AS production
WORKDIR /app

# Copy node_modules and code
COPY --from=builder /app/node_modules /app/node_modules
COPY . /app

EXPOSE 3000
CMD ["sh", "-c", "bunx prisma db push && bun run start"]
