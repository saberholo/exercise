import random
import time


up = 20000
comp_nodes = random.randint(2, up)
comp_edges = random.randint(1, int(comp_nodes * 1.5))
nodes = [i+1 for i in range(comp_nodes)]
c_from = random.choices(nodes, k=comp_edges)
c_to = random.choices(nodes, k=comp_edges)


def minOperations(comp_nodes, comp_from, comp_to):

    assert len(comp_from) == len(comp_to)
    comp_edges = len(comp_from)
    if comp_edges < comp_nodes - 1:
        return -1, 0

    whole_nodes = [i + 1 for i in range(comp_nodes)]
    branches_num = 0
    edges = [(i, j) for i, j in zip(comp_from, comp_to)]

    start = time.time()

    while whole_nodes:
        branch = [whole_nodes.pop(0)]
        for tmp in branch:
            pop_list = []
            for i in range(len(edges)):
                if edges[i][0] != tmp and edges[i][1] != tmp:
                    continue
                elif edges[i][0] == tmp and edges[i][1] not in branch:
                    branch.append(edges[i][1])
                    whole_nodes.pop(whole_nodes.index(edges[i][1]))
                    pop_list.append(i)
                elif edges[i][1] == tmp and edges[i][0] not in branch:
                    branch.append(edges[i][0])
                    whole_nodes.pop(whole_nodes.index(edges[i][0]))
                    pop_list.append(i)
            for d, i in zip(range(len(pop_list)), pop_list):
                edges.pop(i - d)
        branches_num += 1

    end = time.time()
    return branches_num - 1, end - start


print('comp_nodes:\t', comp_nodes)
print(c_from)
print(c_to)
res, eclipse = minOperations(comp_nodes, c_from, c_to)
print('min operations:\t', res)
print('eclipse time:\t', eclipse)



