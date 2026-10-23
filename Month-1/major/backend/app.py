from flask import Flask, request, jsonify
import scraper
from textblob import TextBlob

app = Flask(__name__)

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

@app.route("/reviews")
def get_reviews():
    product_url = request.args.get("product")
    reviews = scraper.scrape_reviews(product_url)
    results = [{"review": r, "sentiment": analyze_sentiment(r)} for r in reviews]
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
