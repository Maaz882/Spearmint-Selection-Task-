const API_URL = "http://localhost:8000/recommend";

export async function getRecommendations(query) {
  const response = await fetch(API_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ query }),
  });

  if (!response.ok) {
    throw new Error("Failed to fetch recommendations");
  }

  return await response.json();
}