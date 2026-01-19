const API = "http://127.0.0.1:5000";

async function predictWaste() {
  const item = document.getElementById("itemInput").value.trim();

  if (!item) {
    alert("Please enter a waste item!");
    return;
  }

  // show loading
  document.getElementById("uiCategory").textContent = "Loading...";
  document.getElementById("uiDisposal").textContent = "Loading...";
  document.getElementById("uiExplanation").textContent = "Loading...";
  document.getElementById("uiImpact").textContent = "Loading...";
  document.getElementById("rawPredict").innerText = "{}";

  document.getElementById("predValue").textContent = "—";
  document.getElementById("co2Value").textContent = "—";
  document.getElementById("actionValue").textContent = "—";
  document.getElementById("categoryPill").textContent = "Loading";

  try {
    const res = await fetch(`${API}/predict`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ item })
    });

    const data = await res.json();

    // ✅ update summary cards
    document.getElementById("predValue").textContent = data.category?.toUpperCase() || "—";
    document.getElementById("co2Value").textContent = (data.impact?.co2_saved ?? "—") + " kg";
    document.getElementById("actionValue").textContent = data.disposal || "—";
    document.getElementById("categoryPill").textContent = data.category ? data.category.toUpperCase() : "Ready";

    // ✅ clean output section
    document.getElementById("uiCategory").textContent = data.category || "—";
    document.getElementById("uiDisposal").textContent = data.disposal || "—";
    document.getElementById("uiExplanation").textContent = data.explanation || "—";

    const impactText =
      (data.impact?.note ? data.impact.note : "") +
      (data.impact?.co2_saved != null ? ` (CO₂ saved: ${data.impact.co2_saved} kg)` : "");

    document.getElementById("uiImpact").textContent = impactText || "—";

    // ✅ pretty multiline JSON
    document.getElementById("rawPredict").innerText = JSON.stringify(data, null, 2);

  } catch (err) {
    console.error(err);
    alert("Backend not reachable. Make sure Flask server is running on port 5000.");
  }
}

async function askAssistant() {
  const query = document.getElementById("queryInput").value.trim();

  if (!query) {
    alert("Please enter a question!");
    return;
  }

  // loading
  document.getElementById("uiAnswer").textContent = "Loading...";
  document.getElementById("rawAsk").innerText = "{}";

  try {
    const res = await fetch(`${API}/ask`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query })
    });

    const data = await res.json();

    document.getElementById("uiAnswer").textContent = data.answer || "—";

    // ✅ pretty multiline JSON
    document.getElementById("rawAsk").innerText = JSON.stringify(data, null, 2);

  } catch (err) {
    console.error(err);
    alert("Backend not reachable. Make sure Flask server is running on port 5000.");
  }
}