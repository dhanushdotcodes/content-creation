import { PrismaClient } from "@prisma/client";

// Singleton Prisma Client
const prisma = new PrismaClient();

export default prisma;
