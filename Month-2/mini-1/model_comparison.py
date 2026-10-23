import matplotlib.pyplot as plt

models = ["Naive Bayes", "SVM", "Logistic Regression", "Random Forest"]
accuracy = [98.3, 98.0, 97.8, 96.5]

plt.figure(figsize=(8,5))
plt.barh(models, accuracy)

plt.title("Machine Learning Model Comparison")
plt.xlabel("Accuracy (%)")

plt.savefig("model_comparison.png", dpi=300, bbox_inches="tight")
plt.show()