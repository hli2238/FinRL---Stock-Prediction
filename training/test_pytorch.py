import torch
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load Iris dataset
iris = load_iris()
data = iris.data
target = iris.target

# Convert data and target to PyTorch tensors
data_tensor = torch.tensor(data)
target_tensor = torch.tensor(target)

# Plot the data
# c is cener color, .scatter plots the graph
plt.figure(figsize=(10, 6))
plt.scatter(data[:, 0], data[:, 1], c="black", cmap=plt.cm.Set1, edgecolor='green')
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.title('Iris Dataset')
plt.show()
