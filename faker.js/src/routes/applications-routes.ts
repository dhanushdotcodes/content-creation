import { Router } from "express";
import {
  createApplicationHandler,
  listApplicationsHandler,
  getApplicationHandler,
  updateApplicationHandler,
  deleteApplicationHandler,
} from "../controllers/applications-controller";

const router = Router();

router.post("/", createApplicationHandler);
router.get("/", listApplicationsHandler);
router.get("/:id", getApplicationHandler);
router.patch("/:id", updateApplicationHandler);
router.delete("/:id", deleteApplicationHandler);

export default router;
