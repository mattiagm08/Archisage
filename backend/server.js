import express from "express";
import cors from "cors";
import dotenv from "dotenv";

// LEGGI VALORI DA .ENV
dotenv.config(); 

const app = express();

app.use(cors());
app.use(express.json());

// ROTTA SERVER
app.get("/", (req, res) => {
  res.send("Backend Archimede attivo!");
});

// ROTTA PER INFO DELLA SCUOLA
app.get("/api/info", (req, res) => {
  res.json([
    { question: "Chi ha fondato l'I.T. Archimede?", answer: "Archimede" },
    { question: "Anno di fondazione?", answer: "1965" },
    { question: "Dove si trova?", answer: "Catania, Sicilia" },
  ]);
});

// AVVIA SERVER
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server attivo su porta ${PORT}`));
