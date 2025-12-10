import uuid

# Store all graphs
graph_store = {}

"""
Graph structure:
{
   graph_id: {
       "nodes": [...],
       "edges": {...}
   }
}
"""

def create_graph(nodes, edges):
    graph_id = str(uuid.uuid4())

    graph_store[graph_id] = {
        "nodes": nodes,
        "edges": edges
    }

    return graph_id
