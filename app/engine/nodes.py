def extract_functions(state):
    code = state.get("code", "")
    # Fake extraction logic:
    state["functions"] = ["func1", "func2", "func3"]
    state["quality_score"] = 10
    return state


def check_complexity(state):
    functions = state.get("functions", [])
    # Fake complexity check:
    state["complexity"] = len(functions) * 5
    return state


def detect_issues(state):
    # Fake issue detection:
    state["issues"] = max(0, 5 - state["quality_score"] // 5)
    return state


def suggest_improvements(state):
    # Fake improvement logic:
    state["quality_score"] += 15

    # Cap score
    if state["quality_score"] > 100:
        state["quality_score"] = 100

    return state

