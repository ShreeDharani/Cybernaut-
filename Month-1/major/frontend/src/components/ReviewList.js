import React from "react";

function ReviewList({ reviews }) {
  return (
    <div style={{ marginTop: "20px" }}>
      <h2>Reviews</h2>
      <ul style={{ listStyle: "none", padding: 0 }}>
        {reviews.map((r, index) => (
          <li key={index} style={{ marginBottom: "10px" }}>
            <strong>{r.sentiment}:</strong> {r.review}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ReviewList;
