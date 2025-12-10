from app.engine.nodes import (
    extract_functions,
    check_complexity,
    detect_issues,
    suggest_improvements
)

# Registry of tool/node functions
tool_registry = {
    "extract_functions": extract_functions,
    "check_complexity": check_complexity,
    "detect_issues": detect_issues,
    "suggest_improvements": suggest_improvements,
}

