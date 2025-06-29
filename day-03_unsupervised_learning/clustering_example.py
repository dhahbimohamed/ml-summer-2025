# 📊 K-Means Clustering Example

from sklearn.cluster import KMeans  # Import the clustering algorithm
import numpy as np                  # For numerical array operations
import matplotlib.pyplot as plt     # For visualizing the results

# -----------------------------------
# Step 1: Create a simple 2D dataset
# Each row is a data point (x, y)
# -----------------------------------
data = np.array([
    [1, 2], [1, 4], [1, 0],    # Group 1 (x ≈ 1)
    [4, 2], [4, 4], [4, 0]     # Group 2 (x ≈ 4)
])

# -----------------------------------
# Step 2: Apply K-Means clustering
# n_clusters = 2 → we want to group data into 2 clusters
# random_state = 0 → ensures reproducible results
# -----------------------------------
kmeans = KMeans(n_clusters=2, random_state=0).fit(data)

# -----------------------------------
# Step 3: View clustering results
# .labels_ → which cluster each point belongs to (0 or 1)
# .cluster_centers_ → coordinates of each cluster center
# -----------------------------------
print("Labels:", kmeans.labels_)
print("Centroids:", kmeans.cluster_centers_)

# -----------------------------------
# Step 4: Visualize the data and clusters
# Points are colored by their cluster label
# Red 'X' marks the cluster centers
# -----------------------------------
plt.scatter(data[:, 0], data[:, 1], c=kmeans.labels_)  # Data points
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],
            c='red', marker='x', s=100)               # Cluster centers
plt.title("K-Means Clustering Example")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()