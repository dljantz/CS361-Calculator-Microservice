const express = require("express");
const app = express();
const PORT = process.env.PORT ||3000;

const calculate = (params) => {
  const m1 = params.m1 !== undefined ? parseFloat(params.m1) : null;
  const m2 = params.m2 !== undefined ? parseFloat(params.m2) : null;
  const d1 = params.d1 !== undefined ? parseFloat(params.d1) : null;
  const d2 = params.d2 !== undefined ? parseFloat(params.d2) : null;

  let operation = "";
  if (m1 !== null) operation += "m1";
  if (m2 !== null) operation += "m2";
  if (d1 !== null) operation += "d1";
  if (d2 !== null) operation += "d2";

  switch (operation) {
    case "m1m2":
      return m1 * m2;

    case "d1d2":
      if (d2 === 0) throw new Error("Division by zero not allowed");
      return d1 / d2;

    case "m1d1d2":
      if (d2 === 0) throw new Error("Division by zero not allowed");
      return m1 * (d1 / d2);

    default:
      throw new Error("Invalid parameters.");
  }
};

app.get("/calculate", (req, res) => {
  try {
    const { m1, m2, d1, d2 } = req.query;
    const result = calculate({
      m1,
      m2,
      d1,
      d2,
    });
    res.status(200).json({ success: true, result });
  } catch (err) {
    res.status(400).json({ success: false, error: err.message });
  }
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
