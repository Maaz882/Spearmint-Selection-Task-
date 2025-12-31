import { useState } from "react";
import { getRecommendations } from "./api";
import "./App.css";

function App() {
  const [query, setQuery] = useState("");
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");
  const [products, setProducts] = useState([]);

  const handleSearch = async () => {
    if (!query.trim()) return;

    setLoading(true);
    setMessage("");
    setProducts([]);

    try {
      const data = await getRecommendations(query);
      setMessage(data.message);
      setProducts(data.recommendations);
    } catch (error) {
      setMessage("Something went wrong. Try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>🛒 AI Product Recommendation</h1>

      <input
        type="text"
        placeholder="e.g. I want a phone under $500"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />


      <button onClick={handleSearch} disabled={loading || !query.trim()}>
        {loading ? "Searching..." : "Get Recommendations"}
      </button>

      {message && <p className="message">{message}</p>}

      <div className="products">
        {products.map((item) => (
          <div key={item.id} className="card">
            <h3>{item.name}</h3>
            <p>Category: {item.category}</p>
            <p>Price: ${item.price}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;