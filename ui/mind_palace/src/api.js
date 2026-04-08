const API = "http://localhost:8000";

export async function getEntities() {
  const r = await fetch(API + "/entities");
  return await r.json();
}

export async function getLinks() {
  const r = await fetch(API + "/links");
  return await r.json();
}

export async function sendIntent(intent) {
  const r = await fetch(API + "/intent", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ intent }),
  });
  return await r.json();
}
