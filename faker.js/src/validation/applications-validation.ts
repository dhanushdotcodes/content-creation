import { z } from "zod";

export const CreateApplicationSchema = z.object({
  company: z.string().min(1, { message: "Company is required" }),
  position: z.string().min(1, { message: "Position is required" }),
  salary: z.string().optional().nullable(),
  location: z.string().optional().nullable(),
  status: z.enum(["APPLIED", "INTERVIEWING", "OFFERED", "REJECTED"]).optional(),
  jobUrl: z.string().optional().nullable(),
  notes: z.string().optional().nullable(),
});

export const UpdateApplicationSchema = z.object({
  company: z.string().min(1, { message: "Company cannot be empty" }).optional(),
  position: z.string().min(1, { message: "Position cannot be empty" }).optional(),
  salary: z.string().optional().nullable(),
  location: z.string().optional().nullable(),
  status: z.enum(["APPLIED", "INTERVIEWING", "OFFERED", "REJECTED"]).optional(),
  jobUrl: z.string().optional().nullable(),
  notes: z.string().optional().nullable(),
});
