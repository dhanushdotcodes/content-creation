import Redis from "ioredis";
import express from "express";

const app = express();

const redis = new Redis("redis://default:mypassword@localhost:6379/0");

app.get("/", async (req, res) => {
  const response = await redis.ping();

  res.send(response);
});

app.listen(3000, () => {
  console.log("Server is running on port 3000");
});