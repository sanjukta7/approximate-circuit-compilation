from region_graph.region_graph import RegionGraph 
from region_graph.rg_node import RegionNode, PartitionNode


def CompiledTree(scope: set) -> RegionGraph: 
    root = RegionNode(scope)
    graph = RegionGraph()
    graph.add_node(root)
    partitionroot = PartitionNode(scope)
    graph.add_node(partitionroot)
    allnodes = []

    for var in scope:
        print(var)
        node = RegionNode(var)
        allnodes.append(node)
    for node in allnodes:
        graph.add_edge(partitionroot, node)
    return graph 
