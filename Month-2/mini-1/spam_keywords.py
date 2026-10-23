import matplotlib.pyplot as plt

keywords = [
    "free","win","money","prize",
    "click","offer","bonus","urgent",
    "reward","cash"
]

counts = [250,220,210,195,185,170,150,130,120,100]

plt.figure(figsize=(8,5))
plt.barh(keywords, counts, color="red")

plt.title("Spam Keyword Frequency Analysis")
plt.xlabel("Frequency")

plt.savefig("spam_keywords.png", dpi=300, bbox_inches="tight")
plt.show()