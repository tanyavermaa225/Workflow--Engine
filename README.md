🚀 Workflow Engine – Assignment Project

A graph-based workflow execution engine built using FastAPI, designed to run modular tasks (“nodes”) in sequence, manage state across nodes, and support looping logic until a specific condition is reached.
This project fully implements the assignment requirements for building a custom workflow orchestration engine.

📘 Project Overview

The purpose of this project is to create a simple but functional workflow engine that:

. Represents workflows as graphs (nodes + edges)
. Runs nodes sequentially according to the graph structure
. Maintains a shared state throughout execution
. Supports looping until conditions are met
. Stores and retrieves the final state of each run
. Provides a clean REST API for interacting with the engine

A sample workflow (“Code Review Mini-Agent”) is included to demonstrate how the system processes input, analyzes it, and iteratively improves results until a threshold is reached.

🧩 Key Concepts

1. Workflows as Graphs

A workflow is modeled as:

Nodes → individual operations (tools)

Edges → define execution order

Start Node → always the first in the list

Loop Condition → stops when a rule is satisfied

Example graph structure:
{
  "nodes": ["extract_functions", "check_complexity", "detect_issues", "suggest_improvements"],
  "edges": {
    "extract_functions": "check_complexity",
    "check_complexity": "detect_issues",
    "detect_issues": "suggest_improvements",
    "suggest_improvements": "suggest_improvements"
  }
}


The engine stores these workflows in memory and executes them dynamically.

2. State Management

Each node receives the same mutable state dictionary.
state = {
    "code": "def x(): pass",
    "quality_score": 0,
    "issues": []
}

Nodes read, write, or update values inside this state.

The final state after execution is saved and can be retrieved later using a unique run_id.

3. Node Execution
Example node registration (illustrative only):
@tool_registry.register("extract_functions")
def extract_functions(state):
    ...
    return state

5. Looping Behaviour
 The assignment requires a looping step:
if current_node == "suggest_improvements":
    if state["quality_score"] < 70:
        # loop again

📡 REST API Endpoints

All interactions happen through the FastAPI-powered REST interface.

✔ Create a Workflow
POST /graph/create

Saves a workflow (nodes + edges) in memory and returns a unique graph_id.

✔ Run a Workflow
POST /graph/run

Executes the graph with an initial state.

The response includes:

1. run_id (unique identifier)
2. final_state
3. log (all execution steps)
  Example output: 
   {
  "run_id": "123abc...",
  "final_state": {
    "quality_score": 70,
    "issues": 3,
    "functions": ["func1", "func2", "func3"]
  },
  "log": [
    "Ran: extract_functions",
    "Ran: check_complexity",
    "Ran: detect_issues",
    "Ran: suggest_improvements",
    "Loop ended: threshold reached"
  ]
}


✔ Retrieve Run State
GET /graph/state/{run_id}

Returns the last known state of that run.

🧪 Sample Workflow Implemented

The included demo workflow is a Code Review Mini-Agent, consisting of nodes that:

1. Extract function information
2. Check complexity
3. Detect issues
4. Suggest improvements
5. Automatically repeat improvements until quality is acceptable

This example showcases how the engine handles sequential steps and looping behaviour.

🛠 How to Run the Project
1. Install dependencies:
pip install -r requirements.txt

2. Launch the server:
uvicorn app.main:app --reload

3. Use the interactive API:
Open:

http://127.0.0.1:8000/docs


Here you can:

1. Create workflows
2. Run workflows
3. Inspect run results
4. Everything is fully testable through Swagger UI.

🏁 Conclusion

This workflow engine demonstrates a clean, modular, and extensible design suitable for orchestrating sequential and iterative tasks. With node registration, state passing, looping logic, and full API control, it forms a solid foundation for building lightweight agent systems and automated pipelines.


