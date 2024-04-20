from sklearn.cluster import KMeans

X = data[['extroversion', 'agreeableness', 'conscientiousness', 'neuroticism', 'openness']]
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
