import React, { useState } from "react";
import ReviewList from "./components/ReviewList";

function App() {
  const [url, setUrl] = useState("");
  const [reviews, setReviews] = useState([]);

  const fetchReviews = async () => {
    try {
      const response = await fetch(`http://127.0.0.1:5000/reviews?product=${url}`);
      const data = await response.json();
      setReviews(data);
    } catch (error) {
      console.error("Error fetching reviews:", error);
    }
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h1>Product Sentiment Analyzer</h1>
      <input
        type="text"
        placeholder="Enter product URL"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        style={{ width: "400px", marginRight: "10px", padding: "5px" }}
      />
      <button onClick={fetchReviews} style={{ padding: "5px 10px" }}>
        Analyze
      </button>
      <ReviewList reviews={reviews} />
    </div>
  );
}

export default App;
