import prisma from "../lib/prisma";

export async function checkHealth() {
  // Service layer interacts with database
  await prisma.$queryRaw`SELECT 1`;
  return {
    status: "ok",
    database: "healthy",
    timestamp: new Date().toISOString()
  };
}
