import matplotlib.pyplot as plt

plt.bar(kmeans.labels_, kmeans.cluster_centers_[:, 0])
plt.xlabel('Cluster')
plt.ylabel('Extroversion')
plt.show()
