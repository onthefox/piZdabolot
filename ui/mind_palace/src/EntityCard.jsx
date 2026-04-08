import React from "react";

export default function EntityCard({ entity }) {
  return (
    <div
      style={{
        background: "#1a1a2e",
        border: "1px solid #4fc3f7",
        borderRadius: 8,
        padding: 16,
      }}
    >
      <h3 style={{ color: "#4fc3f7", marginBottom: 8 }}>Сущность: {entity.name}</h3>
      <div style={{ color: "#aaa" }}>ID: {entity.id}</div>
    </div>
  );
}
