from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

def load_data(limit=20):
    """Load crypto data from CSV and return as list of dicts."""
    df = pd.read_csv("crypto_data.csv")
    return df.tail(limit).to_dict(orient="records")

@app.route("/")
def home():
    data = load_data(limit=20)
    return render_template("index.html", data=data)

@app.route("/chart-data")
def chart_data():
    df = pd.read_csv("crypto_data.csv")
    df = df.tail(50)  # last 50 points for chart

    return jsonify({
        "labels": df["Timestamp"].tolist(),
        "prices": df["Price"].str.replace("$", "").str.replace(",", "").astype(float).tolist(),
        "names": df["Name"].tolist()
    })

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(debug=True)
    