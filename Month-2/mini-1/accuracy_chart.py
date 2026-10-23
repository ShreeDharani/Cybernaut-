import matplotlib.pyplot as plt

accuracy = 98.3

plt.figure(figsize=(6,4))
plt.bar(["Accuracy"], [accuracy], color="green")

plt.ylim(0,100)
plt.ylabel("Percentage")
plt.title("Spam Classifier Accuracy")

plt.savefig("accuracy.png", dpi=300, bbox_inches="tight")
plt.show()