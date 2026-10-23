# generate_dataset.py

import pandas as pd
import random

spam_messages = [
    "Verify your account immediately",
    "Click here to claim your reward",
    "Your bank account is suspended",
    "Confirm your payment details",
    "Security alert login now",
    "Win a free smartphone today",
    "Lottery winner claim prize",
    "Urgent password reset required",
    "Account verification needed",
    "Limited time investment opportunity"
]

ham_messages = [
    "Let's meet tomorrow",
    "Project discussion at 2 PM",
    "Can you send the report",
    "Thank you for your support",
    "Happy birthday",
    "Meeting has been rescheduled",
    "Lunch at noon",
    "Assignment submission reminder",
    "See you in class",
    "Good luck for your interview"
]

data = []

for _ in range(2500):
    data.append(["spam", random.choice(spam_messages)])

for _ in range(2500):
    data.append(["ham", random.choice(ham_messages)])

random.shuffle(data)

df = pd.DataFrame(data, columns=["label", "message"])

df.to_csv("dataset/phishing_data.csv", index=False)

print("5000 records created successfully!")