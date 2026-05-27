import { useEffect, useState } from "react";

const API_URL = import.meta.env.VITE_API_URL ?? "http://localhost:8000";

type HealthStatus = "checking" | "ok" | "error";

export default function App() {
  const [status, setStatus] = useState<HealthStatus>("checking");

  useEffect(() => {
    fetch(`${API_URL}/health`)
      .then((res) => (res.ok ? res.json() : Promise.reject(res)))
      .then(() => setStatus("ok"))
      .catch(() => setStatus("error"));
  }, []);

  return (
    <main className="app">
      <h1>CX Agent Orchestration Platform</h1>
      <p>Backend status: <strong data-status={status}>{status}</strong></p>
      <p className="hint">
        This is the initial scaffold. Chat and dashboard pages will be added in
        upcoming phases — see <code>docs/architecture.md</code>.
      </p>
    </main>
  );
}
