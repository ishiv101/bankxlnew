// backend/index.js
const express = require('express');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(express.json());

// Example: simple health check route
app.get('/', (req, res) => {
res.send('✅ BankXL backend is running!');
});

// Example: check a formula
app.post('/api/check-formula', (req, res) => {
const { formula } = req.body;

if (!formula || formula.length < 3) {
    return res.status(400).json({ hint: "Formula too short!" });
}

return res.json({ hint: `Formula received: ${formula}` });
});

const PORT = 5000;
app.listen(PORT, () => {
console.log(`🚀 Backend running at http://localhost:${PORT}`);
});