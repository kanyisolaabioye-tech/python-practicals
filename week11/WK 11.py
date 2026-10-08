import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Iris.csv")

print(data.head())
print(data.info())
print(data.describe())
print(data["Species"].value_counts())

# Histogram
data.hist(figsize=(10, 8))
plt.show()

# Scatter plot
plt.scatter(data["SepalLengthCm"], data["SepalWidthCm"])
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("Sepal Length vs Sepal Width")
plt.show()

# Box plot
data.boxplot(column="PetalLengthCm", by="Species")
plt.show()