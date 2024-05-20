# Personality Clustering and Input Form

This project includes a Python script for clustering customer data based on personality traits and an HTML form for inputting new personality data. The clustering is done using the K-Means algorithm, and the results are visualized using a bar chart.

## Features

- Loads and cleans customer data from a CSV file.
- Uses K-Means clustering to group customers based on five personality traits.
- Visualizes the clustering results with a bar chart.
- HTML form for user input of personality traits.

## Requirements

- Python 3.x
- pandas
- scikit-learn
- matplotlib

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Mohanraj2622/personality-clustering.git
    cd personality-clustering
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```bash
    pip install pandas scikit-learn matplotlib
    ```

## Usage

1. **Prepare the dataset**: Ensure you have a CSV file named `customer_data.csv` with the following columns:
    - extroversion
    - agreeableness
    - conscientiousness
    - neuroticism
    - openness

2. **Run the Python script**:
    ```bash
    python clustering.py
    ```

3. **View the HTML form**:
    Open the `form.html` file in your web browser to input new personality data.

## Files

- `clustering.py`: The main Python script for clustering and visualization.
- `customer_data.csv`: The CSV file containing customer personality data.
- `form.html`: The HTML file containing the form for user input.

## Python Script Details (`clustering.py`)

```python
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load and clean data
data = pd.read_csv('customer_data.csv')
data.dropna(inplace=True)

# Select features for clustering
X = data[['extroversion', 'agreeableness', 'conscientiousness', 'neuroticism', 'openness']]

# Perform K-Means clustering
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

# Visualize the clustering results
plt.bar(kmeans.labels_, kmeans.cluster_centers_[:, 0])
plt.xlabel('Cluster')
plt.ylabel('Extroversion')
plt.show()
```

### HTML Form Details (`form.html`)

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    form {
      max-width: 400px;
      margin: auto;
    }
    label {
      display: block;
      margin-top: 10px;
    }
    input[type="range"] {
      width: 100%;
    }
    input[type="submit"] {
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <form action="/submit" method="post">
    <label for="extroversion">Extroversion:</label><br>
    <input type="range" id="extroversion" name="extroversion" min="1" max="10"><br>

    <label for="agreeableness">Agreeableness:</label><br>
    <input type="range" id="agreeableness" name="agreeableness" min="1" max="10"><br>

    <label for="conscientiousness">Conscientiousness:</label><br>
    <input type="range" id="conscientiousness" name="conscientiousness" min="1" max="10"><br>

    <label for="neuroticism">Neuroticism:</label><br>
    <input type="range" id="neuroticism" name="neuroticism" min="1" max="10"><br>

    <label for="openness">Openness:</label><br>
    <input type="range" id="openness" name="openness" min="1" max="10"><br>

    <input type="submit" value="Submit">
  </form>
</body>
</html>
```

## Notes

- Ensure the CSV file (`customer_data.csv`) is correctly formatted and located in the same directory as the Python script.
- The HTML form is a simple interface for users to input personality traits, which can be submitted to a server endpoint (e.g., `/submit`).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by psychological and personality trait analysis methods.

