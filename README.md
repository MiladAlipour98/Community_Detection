## Community Detection - Empirical Study

In this project, we will compare different community detection algorithms using multiple real-world social networks. The following tasks need to be completed:

### Preparation
- Download and read the following graphs:
  - Karate Club network
  - Dolphins social network
  - Jazz musicians network

### Dataset Statistics
- Number of nodes (n)
- Number of edges (m)
- Average path length (d)
- Average clustering coefficient (C)

### Betweenness-Based Clustering (Girvan-Newman algorithm)
A program that computes betweenness-based clustering using the Girvan-Newman algorithm. The code should be properly commented. Submit the program via GitHub with the filename "problem3b.py". Include the repository name of your team in your written submission.

### Modularity-Based Clustering (Modularity Maximization)
A program that computes modularity-based clustering using modularity maximization. Comment the code appropriately. Submit the program via GitHub with the filename "problem3c.py". Include the repository name of your team in your written submission.

### Spectral Clustering (Graph Laplacian)
A program that computes spectral clustering using the graph Laplacian. Provide proper code comments. Submit the program via GitHub with the filename "problem3d.py". Include the repository name of your team in your written submission.

### Quantitative Comparison
Run all three methods (betweenness-based, modularity-based, and spectral clustering) on the three datasets (Karate, Dolphins, Jazz). For each method and dataset, report the following:
- Number of clusters found
- Modularity score for the clustering
- Runtime of the algorithm (take the mode runtime by executing the computation multiple times)
- Visualize the clusters using Gephi, an open-source graph visualization and analysis tool. Experiment with different layouts, node and edge coloring, sizes, etc. Provide a careful description of the visualization and explain what it shows.
Based on the findings, analyze which algorithm performs the best in terms of both efficiency and quality.

#### Dolphins Dataset

![Dolphins](https://github.com/MiladAlipour98/Community_Detection/assets/105122009/ccfbf3ae-02a8-4a14-9681-217681d71088)

![DC](https://github.com/MiladAlipour98/Community_Detection/assets/105122009/52c1f3da-642e-4d0f-93e3-c05005ef33d6)

#### Karate Dataset
![karate](https://github.com/MiladAlipour98/Community_Detection/assets/105122009/251cf955-ead9-400e-b22c-73e5c0fdffed)

![KC](https://github.com/MiladAlipour98/Community_Detection/assets/105122009/4a600caa-ba0f-4977-abc2-438cc4354cb6)

#### Jazz Dataset
![jazz](https://github.com/MiladAlipour98/Community_Detection/assets/105122009/cf9836c3-a5c4-4170-9a54-94d1fb42e473)

![jco](https://github.com/MiladAlipour98/Community_Detection/assets/105122009/47de8198-3890-4d91-9fab-4258d38c41ce)

### Representative Network
Create and visualize the representative network for one community detection method for each dataset. The representative network should have one node per cluster, with node size representing the community size. Edges between clusters should reflect the number of cross-community edges between nodes in the respective clusters. Submit the program for creating the representative networks and the visualization via GitHub with the filename "problem3BONUS.py". Include the repository name of your team in your submission.


