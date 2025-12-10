from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.engine.graph import create_graph, graph_store
from app.engine.runner import run_graph, run_store

app = FastAPI(title="Workflow Engine")


# ----- MODELS -----
class GraphCreateRequest(BaseModel):
    nodes: list[str]
    edges: dict


class GraphRunRequest(BaseModel):
    graph_id: str
    initial_state: dict


# ----- ENDPOINTS -----

@app.post("/graph/create")
def create_graph_endpoint(req: GraphCreateRequest):
    graph_id = create_graph(req.nodes, req.edges)
    return {"graph_id": graph_id}


@app.post("/graph/run")
def run_graph_endpoint(req: GraphRunRequest):
    if req.graph_id not in graph_store:
        raise HTTPException(status_code=404, detail="Graph not found")

    final_state, log, run_id = run_graph(req.graph_id, req.initial_state)
    return {"run_id": run_id, "final_state": final_state, "log": log}


@app.get("/graph/state/{run_id}")
def get_state_endpoint(run_id: str):
    if run_id not in run_store:
        raise HTTPException(status_code=404, detail="Run ID not found")

    return {"state": run_store[run_id]}
