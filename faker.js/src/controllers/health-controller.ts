import type { Request, Response } from "express";
import * as healthService from "../services/health-service";

export async function getHealthHandler(req: Request, res: Response) {
  try {
    const result = await healthService.checkHealth();
    
    return res.status(200).json({
      success: true,
      data: result
    });
  } catch (error: any) {
    console.error("Health check error:", error);
    
    return res.status(500).json({
      success: false,
      error: error.message || "Internal server error"
    });
  }
}
