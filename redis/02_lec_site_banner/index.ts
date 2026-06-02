import express from "express";
import Redis from "ioredis";

const app = express();
app.use(express.json());

const redis = new Redis("redis://default:mypassword@localhost:6379/0");

const BANNER_KEY = "app:banner"

app.get("/", async (req, res) => {
  const response = await redis.ping();

  res.send(response);
});

app.get("/banner", async (req, res) => {
  const bannerText = await redis.get(BANNER_KEY);

  if (!bannerText) {
    return res.status(404).send("Banner not found");
  }

  res.send({bannerText})
})

app.post("/banner", async (req, res) => {
  const { bannerText } = req.body;

  await redis.set(BANNER_KEY, bannerText);

  res.send({bannerText});
})

app.delete("/banner", async (req, res) => {
  await redis.del(BANNER_KEY);

  res.send({bannerText: null});
})

app.get("/banner/exists", async (req, res) => {
  const exists = await redis.exists(BANNER_KEY);

  console.log("Exists: ", Boolean(exists))
  res.send({exists})
})

app.listen(3000, () => {
  console.log("Server is running on port 3000");
});