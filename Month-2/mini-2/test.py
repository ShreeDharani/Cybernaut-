import joblib

model = joblib.load(
    "models/phishing_model.pkl"
)

message = input("Enter message: ")

prediction = model.predict([message])[0]

print("Prediction:", prediction)
