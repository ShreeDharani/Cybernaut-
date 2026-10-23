import matplotlib.pyplot as plt

labels = ["Ham", "Spam"]
sizes = [4825, 747]

plt.figure(figsize=(6,6))
plt.pie(
    sizes,
    labels=labels,
    autopct="%1.1f%%",
    colors=["green", "red"]
)

plt.title("Spam vs Ham Distribution")

plt.savefig("spam_vs_ham.png", dpi=300, bbox_inches="tight")
plt.show()