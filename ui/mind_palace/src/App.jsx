import React, { useEffect, useState } from "react";
import { getEntities, getLinks, sendIntent } from "./api";
import Graph from "./Graph";
import EntityCard from "./EntityCard";

export default function App() {
  const [entities, setEntities] = useState([]);
  const [links, setLinks] = useState([]);
  const [selected, setSelected] = useState(null);
  const [intent, setIntent] = useState("");
  const [resp, setResp] = useState(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const [ents, lnks] = await Promise.all([getEntities(), getLinks()]);
      setEntities(ents);
      setLinks(lnks);
    } catch (err) {
      console.error("Failed to fetch data:", err);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!intent.trim()) return;
    setLoading(true);
    try {
      const r = await sendIntent(intent);
      setResp(r);
      setIntent("");
      await fetchData();
    } catch (err) {
      setResp({ error: err.message });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ display: "flex", height: "100vh", background: "#0a0a0a", color: "#e0e0e0" }}>
      {/* Left panel */}
      <div style={{ flex: 1, padding: 16, borderRight: "1px solid #333", overflowY: "auto" }}>
        <h2 style={{ color: "#4fc3f7", marginBottom: 16 }}>MindPalace</h2>

        <h3 style={{ marginBottom: 8 }}>Намерение</h3>
        <form onSubmit={handleSubmit} style={{ marginBottom: 16 }}>
          <input
            value={intent}
            onChange={(e) => setIntent(e.target.value)}
            placeholder='напр: "создать Грядка"'
            style={{ width: "80%", padding: 8, background: "#1a1a2e", border: "1px solid #444", color: "#e0e0e0", borderRadius: 4 }}
          />
          <button
            type="submit"
            disabled={loading}
            style={{ padding: "8px 12px", background: "#4fc3f7", border: "none", borderRadius: 4, cursor: "pointer", color: "#000", fontWeight: "bold" }}
          >
            {loading ? "..." : "Отправить"}
          </button>
        </form>

        {resp && (
          <>
            <h4 style={{ marginBottom: 4 }}>Ответ</h4>
            <pre
              style={{
                background: "#1a1a2e",
                padding: 8,
                borderRadius: 4,
                fontSize: 12,
                maxHeight: 150,
                overflow: "auto",
                marginBottom: 16,
              }}
            >
              {JSON.stringify(resp, null, 2)}
            </pre>
          </>
        )}

        <h3 style={{ marginBottom: 8 }}>Сущности ({entities.length})</h3>
        <ul style={{ listStyle: "none", padding: 0 }}>
          {entities.map((e) => (
            <li key={e.id} style={{ marginBottom: 4 }}>
              <button
                onClick={() => setSelected(e)}
                style={{
                  background: selected?.id === e.id ? "#4fc3f7" : "#1a1a2e",
                  color: selected?.id === e.id ? "#000" : "#e0e0e0",
                  border: "1px solid #444",
                  borderRadius: 4,
                  padding: "4px 12px",
                  cursor: "pointer",
                }}
              >
                {e.name}
              </button>
            </li>
          ))}
        </ul>
      </div>

      {/* Center: Graph */}
      <div style={{ flex: 2, padding: 16 }}>
        <Graph nodes={entities} links={links} onSelect={setSelected} />
      </div>

      {/* Right panel */}
      <div style={{ flex: 1, borderLeft: "1px solid #333", padding: 16, overflowY: "auto" }}>
        {selected ? <EntityCard entity={selected} /> : <p style={{ color: "#666" }}>Выберите сущность</p>}
      </div>
    </div>
  );
}
