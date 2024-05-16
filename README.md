# Depression-Detection-Using-Clustering

# Over View
This project aims to classify people into depressed and non-depressed groups using wearable sensor data collected from a group of individuals. The dataset consists of two groups: control and condition, with each group containing actigraph data collected over time. Additionally, MADRS scores are provided for each patient, which serve as labels for the classification task.

# Dataset Description
[The dataset details available here](https://datasets.simula.no/depresjon/#dataset-details)

# Methodology

## Data Preprocessing:

* Combined control and condition groups.
* Cleaned the data by handling missing values and encoding categorical variables.
## Clustering Analysis:
* Utilized K-Means and DBSCAN clustering algorithms to group individuals based on their wearable sensor data.
* Evaluated clustering performance using Calinski-Harabasz score.
* Visualization:
* Visualized clustering results using scatter plots and box plots to analyze the distribution of features within each cluster.
* Model Evaluation:
* Evaluated the performance of the clustering models using silhouette score and Calinski-Harabasz score.
## Results
K-Means Clustering:
Identified clusters based on wearable sensor data.
Visualized clusters using scatter plots.
DBSCAN Clustering:
Detected clusters based on density of data points.
Visualized clusters using scatter plots.

# Conclusion
The analysis of wearable sensor data combined with MADRS scores provides insights into the classification of individuals into depressed and non-depressed groups. Clustering algorithms offer a valuable approach to group individuals based on activity patterns and other features extracted from wearable sensor data.







