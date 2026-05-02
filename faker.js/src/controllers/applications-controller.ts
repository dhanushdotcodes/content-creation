import type { Request, Response } from "express";
import * as appService from "../services/applications-service";
import { CreateApplicationSchema, UpdateApplicationSchema } from "../validation/applications-validation";

export async function createApplicationHandler(req: Request, res: Response) {
  try {
    const parsed = CreateApplicationSchema.safeParse(req.body);
    if (!parsed.success) {
      const firstError = parsed.error.issues[0]?.message || "Validation failed";
      return res.status(400).json({
        data: null,
        error: "VALIDATION_ERROR",
        message: firstError,
      });
    }

    const application = await appService.createApplication(parsed.data);
    return res.status(201).json({
      data: application,
      error: null,
      message: "success",
    });
  } catch (error: any) {
    console.error("Create application error:", error);
    return res.status(500).json({
      data: null,
      error: "INTERNAL_ERROR",
      message: error.message || "Internal server error",
    });
  }
}

export async function listApplicationsHandler(req: Request, res: Response) {
  try {
    const applications = await appService.listApplications();
    return res.status(200).json({
      data: applications,
      error: null,
      message: "success",
    });
  } catch (error: any) {
    console.error("List applications error:", error);
    return res.status(500).json({
      data: null,
      error: "INTERNAL_ERROR",
      message: error.message || "Internal server error",
    });
  }
}

export async function getApplicationHandler(req: Request, res: Response) {
  try {
    const id = req.params.id as string;
    if (!id) {
      return res.status(400).json({
        data: null,
        error: "VALIDATION_ERROR",
        message: "ID is required",
      });
    }

    const application = await appService.getApplicationById(id);
    if (!application) {
      return res.status(404).json({
        data: null,
        error: "NOT_FOUND",
        message: "Job application not found",
      });
    }

    return res.status(200).json({
      data: application,
      error: null,
      message: "success",
    });
  } catch (error: any) {
    console.error("Get application error:", error);
    return res.status(500).json({
      data: null,
      error: "INTERNAL_ERROR",
      message: error.message || "Internal server error",
    });
  }
}

export async function updateApplicationHandler(req: Request, res: Response) {
  try {
    const id = req.params.id as string;
    if (!id) {
      return res.status(400).json({
        data: null,
        error: "VALIDATION_ERROR",
        message: "ID is required",
      });
    }

    const parsed = UpdateApplicationSchema.safeParse(req.body);
    if (!parsed.success) {
      const firstError = parsed.error.issues[0]?.message || "Validation failed";
      return res.status(400).json({
        data: null,
        error: "VALIDATION_ERROR",
        message: firstError,
      });
    }

    const application = await appService.updateApplication(id, parsed.data);
    return res.status(200).json({
      data: application,
      error: null,
      message: "success",
    });
  } catch (error: any) {
    console.error("Update application error:", error);
    if (error.message === "NOT_FOUND") {
      return res.status(404).json({
        data: null,
        error: "NOT_FOUND",
        message: "Job application not found",
      });
    }
    return res.status(500).json({
      data: null,
      error: "INTERNAL_ERROR",
      message: error.message || "Internal server error",
    });
  }
}

export async function deleteApplicationHandler(req: Request, res: Response) {
  try {
    const id = req.params.id as string;
    if (!id) {
      return res.status(400).json({
        data: null,
        error: "VALIDATION_ERROR",
        message: "ID is required",
      });
    }

    const application = await appService.deleteApplication(id);
    return res.status(200).json({
      data: { id: application.id },
      error: null,
      message: "success",
    });
  } catch (error: any) {
    console.error("Delete application error:", error);
    if (error.message === "NOT_FOUND") {
      return res.status(404).json({
        data: null,
        error: "NOT_FOUND",
        message: "Job application not found",
      });
    }
    return res.status(500).json({
      data: null,
      error: "INTERNAL_ERROR",
      message: error.message || "Internal server error",
    });
  }
}
