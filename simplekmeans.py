from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
x, _ = load_iris(return_X_y=True)
kmeans = KMeans(n_clusters=3)
kmeans.fit(x)
print("Centers:", kmeans.cluster_centers_)
