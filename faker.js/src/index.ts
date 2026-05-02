import express from "express";
import { config } from "./lib/config";
import healthRoutes from "./routes/health-routes";

const app = express();
const port = config.port;

app.use(express.json());

// Routes
app.use("/", healthRoutes);

// Fallback Not Found
app.use((req, res) => {
  res.status(404).send("Not Found");
});

app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});

export default app;
