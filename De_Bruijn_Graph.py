def buildDeBruijnGraph(string, k):
    """ Return a list holding, for each k-mer, its left
        (k-1)-mer and its right (k-1)-mer in a pair """
    edges = []
    nodes = set()
    for i in range(len(string) - k + 1):
        curr_kmer = string[i:i+k]
        left = curr_kmer[:-1]
        right = curr_kmer[1:]
        edges.append((left, right))
        nodes.add(left)
        nodes.add(right)
    return nodes, edges


def visualize_De_Bruijn_Graph(st, k):
    """ Visualize a directed multigraph using graphviz """
    nodes, edges = buildDeBruijnGraph(st, k)
    dot_str = 'digraph "DeBruijn graph" {\n'
    for node in nodes:
        dot_str += '  %s [label="%s"] ;\n' % (node, node)
    for src, dst in edges:
        dot_str += '  %s -> %s ;\n' % (src, dst)
    return dot_str + '}\n'


