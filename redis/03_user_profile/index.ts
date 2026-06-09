import express from "express";
import Redis from "ioredis";

const app = express();
app.use(express.json());

const redis = new Redis(); // defaults to localhost:6379

// 1. POST route without using hash (using stringified JSON)
app.post("/user", async (req, res) => {
    const { email, name } = req.body;
    if (!email || !name) {
        return res.status(400).json({ error: "Email and name are required" });
    }
    
    const userProfile = { email, name };
    await redis.set(`user:${email}`, JSON.stringify(userProfile));
    
    res.json({ message: "User profile saved without hash", user: userProfile });
});

// 2. GET route without using hash
app.get("/user/:email", async (req, res) => {
    const { email } = req.params;
    const userData = await redis.get(`user:${email}`);
    
    if (!userData) {
        return res.status(404).json({ error: "User not found" });
    }
    
    res.json({ message: "User profile retrieved without hash", user: JSON.parse(userData) });
});

// 3. POST route using hash (hset)
app.post("/user-hash", async (req, res) => {
    const { email, name } = req.body;
    if (!email || !name) {
        return res.status(400).json({ error: "Email and name are required" });
    }
    
    await redis.hset(`user-hash:${email}`, { email, name });
    
    res.json({ message: "User profile saved using hash", email, name });
});

// 4. GET route using hash (hgetall)
app.get("/user-hash/:email", async (req, res) => {
    const { email } = req.params;
    const userData = await redis.hgetall(`user-hash:${email}`);
    
    // hgetall returns an empty object {} if the key does not exist
    if (!userData || Object.keys(userData).length === 0) {
        return res.status(404).json({ error: "User not found" });
    }
    
    res.json({ message: "User profile retrieved using hash", user: userData });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});