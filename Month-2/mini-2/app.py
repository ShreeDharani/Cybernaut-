from flask import Flask, render_template, request
import joblib
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

app = Flask(__name__)

# Load Model
model = joblib.load("models/phishing_model.pkl")

# Dashboard Counters
total_scans = 0
spam_count = 0
ham_count = 0

# History
scan_history = []


def find_keywords(message):

    keywords = [
        "bank",
        "verify",
        "password",
        "urgent",
        "click",
        "login",
        "account",
        "winner",
        "prize",
        "offer",
        "suspended",
        "delivery",
        "crypto",
        "bitcoin"
    ]

    found = []

    for word in keywords:

        if word in message.lower():
            found.append(word)

    return found


def threat_category(message):

    msg = message.lower()

    if (
        "bank" in msg or
        "account" in msg or
        "credit card" in msg
    ):
        return "🏦 Banking Phishing"

    elif (
        "password" in msg or
        "login" in msg or
        "verify" in msg
    ):
        return "🔐 Credential Theft"

    elif (
        "winner" in msg or
        "prize" in msg or
        "lottery" in msg
    ):
        return "🎁 Lottery Scam"

    elif (
        "delivery" in msg or
        "package" in msg or
        "courier" in msg
    ):
        return "📦 Fake Delivery Scam"

    elif (
        "investment" in msg or
        "bitcoin" in msg or
        "crypto" in msg
    ):
        return "💰 Investment Scam"

    else:
        return "⚠ General Spam"


@app.route("/", methods=["GET", "POST"])
def home():

    global total_scans
    global spam_count
    global ham_count
    global scan_history

    result = None
    confidence = None
    risk = None
    category = None
    keywords = []

    graph_html = None
    gauge_html = None

    if request.method == "POST":

        message = request.form["message"]

        result = model.predict([message])[0]

        probability = model.predict_proba([message])[0]

        confidence = round(
            max(probability) * 100,
            2
        )

        # Risk Level
        if confidence >= 80:
            risk = "HIGH"

        elif confidence >= 50:
            risk = "MEDIUM"

        else:
            risk = "LOW"

        # Category
        category = threat_category(message)

        # Counters
        total_scans += 1

        if result == "spam":
            spam_count += 1
        else:
            ham_count += 1

        # Keywords
        keywords = find_keywords(message)

        # Save History
        scan_history.append({

            "time": datetime.now().strftime(
                "%d-%m-%Y %I:%M %p"
            ),

            "message": message[:50],

            "prediction": result,

            "confidence": confidence,

            "risk": risk

        })

        # Dynamic Pie Chart
        pie_chart = px.pie(
            names=[
                "Spam Messages",
                "Safe Messages"
            ],

            values=[
                spam_count,
                ham_count
            ],

            hole=0.5,

            title="Real Time Detection Statistics",

            color_discrete_sequence=[
                "#ef4444",
                "#22c55e"
            ]
        )

        pie_chart.update_layout(
            paper_bgcolor="#1e293b",
            plot_bgcolor="#1e293b",
            font_color="white",
            height=450
        )

        graph_html = pie_chart.to_html(
            full_html=False
        )

        # Live Gauge Meter
        gauge = go.Figure(

            go.Indicator(

                mode="gauge+number",

                value=confidence,

                number={
                    "suffix": "%"
                },

                title={
                    "text": "Live Risk Meter"
                },

                gauge={

                    "axis": {
                        "range": [0, 100]
                    },

                    "bar": {
                        "color": "cyan"
                    },

                    "steps": [

                        {
                            "range": [0, 40],
                            "color": "green"
                        },

                        {
                            "range": [40, 70],
                            "color": "yellow"
                        },

                        {
                            "range": [70, 100],
                            "color": "red"
                        }

                    ]
                }
            )
        )

        gauge.update_layout(
            paper_bgcolor="#1e293b",
            font_color="white",
            height=450
        )

        gauge_html = gauge.to_html(
            full_html=False
        )

    return render_template(
        "index.html",

        result=result,

        confidence=confidence,

        risk=risk,

        category=category,

        keywords=keywords,

        graph_html=graph_html,

        gauge_html=gauge_html,

        total_scans=total_scans,

        spam_count=spam_count,

        ham_count=ham_count,

        scan_history=scan_history
    )


if __name__ == "__main__":
     app.run(host="0.0.0.0", port=5000)