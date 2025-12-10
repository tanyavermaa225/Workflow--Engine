import uuid
from app.engine.graph import graph_store
from app.engine.registry import tool_registry

run_store = {}   # stores current state of each run


def run_graph(graph_id, initial_state):
    graph = graph_store[graph_id]
    nodes = graph["nodes"]
    edges = graph["edges"]

    log = []
    state = initial_state.copy()
    run_id = str(uuid.uuid4())

    current_node = nodes[0]  # first node

    while True:
        if current_node not in tool_registry:
            log.append(f"Node {current_node} not found in registry.")
            break

        # Run node
        func = tool_registry[current_node]
        state = func(state)
        log.append(f"Ran: {current_node}")

        # Save current state
        run_store[run_id] = state

        # Loop condition for suggest_improvements
        if current_node == "suggest_improvements":
            score = state.get("quality_score", 0)

            if score < 70:
                log.append(f"Looping: quality_score={score}, below threshold. Running again.")
                continue  # repeat same node
            else:
                log.append(f"Loop ended: quality_score={score}, threshold reached.")
                break

        # Move to next node
        if current_node in edges:
            current_node = edges[current_node]
        else:
            log.append("No next node found. Workflow complete.")
            break

    return state, log, run_id
