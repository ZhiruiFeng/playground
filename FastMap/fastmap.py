from random import choice
C = 3
def fastmap(N, Distance, K, epsilon):
    embedding = {}
    obj_list = list(range(N))
    for node in obj_list:
        embedding[node] = []
    for r in range(K):
        node_a = choice(obj_list)
        node_b = node_a
        # Find the farthest nodes a, b
        for t in range(C):
            length = 0
            for j in obj_list:
                dis = Distance.getdis(node_a, j)
                if dis > length:
                    node_c = j
                    length = dis
            if node_c == node_b:
                break
            else:
                node_b = node_a
                node_a = node_c
        dis_ab = Distance.getdis(node_a, node_b)
        if dis_ab < epsilon:
            break
        # Calcute the embedding
        for node in obj_list:
            dis_na = Distance.getdis(node_a, node)
            dis_nb = Distance.getdis(node_b, node)
            p_nr = float(dis_na**2 + dis_ab**2 - dis_nb **2)/(2 * dis_ab)
            embedding[node].append(p_nr)
        
        # Update the weight of the graph
        for i in range(N):
            for j in range(i+1, N):
                Distance.changedis(i, j, embedding[i][r], embedding[j][r])
        