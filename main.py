import networkx as nx
from networkx.algorithms.community.quality import modularity
from networkx.algorithms.community import greedy_modularity_communities
from networkx.algorithms.community.centrality import girvan_newman
from networkx import edge_betweenness_centrality
from sklearn.cluster import SpectralClustering
import matplotlib.pyplot as plt
import numpy as np
from random import random
import time



def read_gmldataset(path):
    # Reading given dataset for drawing graph
    g = nx.read_gml(path, label='id')
    n = len(g.nodes)
    m = len(g.edges)
    d = nx.average_shortest_path_length(g)
    c = nx.average_clustering(g)
    return g, n, m, d, c



def read_netdataset(path):
    # Reading given dataset for drawing graph
    g = nx.read_weighted_edgelist(path, nodetype = int)
    n = len(g.nodes)
    m = len(g.edges)
    d = nx.average_shortest_path_length(g)
    c = nx.average_clustering(g)

    return g, n, m, d, c

def most_central_edge(g):
    centrality = edge_betweenness_centrality(g)
    max_cent = max(centrality.values())
    centrality = {e: c / max_cent for e, c in centrality.items()}
    centrality = {e: c + random() for e, c in centrality.items()}
    return max(centrality, key=centrality.get)


def adjacency__matrix(G):
    W = nx.adjacency_matrix(G)
    print('adjacancy matrix:')
    print(W.todense())
    return W


def degree_matrix(W):
    D = np.diag(np.sum(np.array(W.todense()), axis=1))
    print('degree matrix:')
    print(D)
    return D


def eigen__vector(L):
    e, v = np.linalg.eig(L)
    # eigenvectors
    print('eigenvectors:')
    #print(v)
    v = v[np.argsort(e)]
    print(v)
    return v


def spectural_clustering(W):
    sc = SpectralClustering(n_clusters=2, affinity='precomputed', random_state=0)
    sc_clustering = sc.fit(W)
    print('spectral clustering:')
    print(sc.labels_)
    return sc.labels_


def find_clustering(sc_labels, G):
    cluster1 = []
    cluster2 = []
    for i in range(len(sc_labels)):
        if sc_labels[i] == 0:
            cluster1.append(list(G.nodes)[i])
        else:
            cluster2.append(list(G.nodes)[i])
    print('community 1: \n', cluster1)
    print('community 2: \n', cluster2)
    clusters = [cluster1, cluster2]
    return clusters


def spectural(G):
    Runtime = []
    for i in range(8):
        import timeit

        start = timeit.default_timer()
        W = adjacency__matrix(G)
        D = degree_matrix(W)
        L = D - W
        print('laplacian matrix:')
        print(L)
        v = eigen__vector(L)
        sc_labels = spectural_clustering(W)
        clusters = find_clustering(sc_labels, G)

        stop = timeit.default_timer()
        Runtime.append(stop - start)
    print('RunTime : ', sum(Runtime) / len(Runtime))
    print('modularity:', modularity(G, clusters))

def main():
    #a

    #g, n, m, d, c = read_gmldataset("karate.gml")
    g, n, m, d, c = read_netdataset("jazz.net")
    nx.draw(g, with_labels=False, node_size=15, width=0.14, node_color='blue')
    plt.show()
    print("Number of Nodes for Jazz network dataset", n)
    print("Number of Edges for Jazz network dataset:", m)
    print("Average Path Lengths for Jazz network dataset: ",d)
    print("Average Clustering Coefficient for Karate Club network dataset:", c)

    #b
    start_time = time.time()
    for i in range(8):
        comm = girvan_newman(g,most_valuable_edge=most_central_edge)
        clusters = tuple(sorted(c) for c in next(comm))
        print("Communities for Jazz network dataset:\n", clusters)
        print("Number of Communities for Jazz network dataset :", len(clusters))
    print('Modularity for Jazz network dataset:', modularity(g, clusters))
    t = (time.time() - start_time)
    print("--- %s seconds ---" % (t/8))

    communities = girvan_newman(g, most_valuable_edge=most_central_edge)
    node_groups = []
    for com in next(communities):
        node_groups.append(list(com))

    color_map = []
    for node in g:
        if node in node_groups[0]:
            color_map.append('blue')
        else:
            color_map.append('green')
    nx.draw(g, node_color=color_map, with_labels=True)
    plt.show()

    #c
    start_time = time.time()

    for i in range(8):
        communities = list(greedy_modularity_communities(g))
        for i in communities :
            node_groups.append(list(i))
        print('Communities for Jazz network dataset:\n', node_groups)
        print('Number of Communities for Jazz network dataset:', len(communities))
    print('modularity:', modularity(g, communities))
    t = (time.time() - start_time)
    print("--- %s seconds ---" % (t / 8))

    #d
    start_time = time.time()
    for i in range(8):

        W = adjacency__matrix(g)
        D = degree_matrix(W)
        L = D - W
        print('laplacian matrix:')
        print(L)
        sc_labels = spectural_clustering(W)
        clusters = find_clustering(sc_labels, g)

    print('modularity:', modularity(g, clusters))
    t = (time.time() - start_time)
    print("--- %s seconds ---" % (t / 8))


if __name__ == '__main__':
    main()



