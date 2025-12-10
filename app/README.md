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

The engine stores these workflows in memory and executes them dynamically.

2. State Management

Each node receives the same mutable state dictionary.
Nodes read, write, or update values inside this state.

The final state after execution is saved and can be retrieved later using a unique run_id.

3. Node Execution

Each node performs a specific function, such as:

1. Extracting data
2. Analyzing or transforming state
3. Calculating metrics
4. Improving quality scores
5. Detecting issues

These tasks are registered automatically inside the system as “tools,” making them reusable and modular.

4. Looping Behaviour

One of the assignment’s key requirements is demonstrated through a loop:

The engine continues to run a particular node multiple times until a stopping condition is reached.

Example behaviour (conceptually):

Run suggest_improvements
→ quality below threshold → loop again
→ quality below threshold → loop again
→ quality >= threshold → stop


This replicates common workflow AI/agent logic where results improve over iterations.

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
