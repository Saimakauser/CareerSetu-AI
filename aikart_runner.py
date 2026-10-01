import json
import os
from agent import run_career_agent


INPUT_PATH = "/aikart/input.json"
OUTPUT_PATH = "/aikart/output.json"


def main():
    with open(INPUT_PATH, "r", encoding="utf-8-sig") as f:
        data = json.load(f)

    target_role = data.get("target_role", "")
    current_skills = data.get("current_skills", [])
    daily_hours = data.get("daily_hours", 2)

    if isinstance(current_skills, str):
        current_skills = [
            skill.strip()
            for skill in current_skills.split(",")
            if skill.strip()
        ]

    result = run_career_agent(
        target_role=target_role,
        current_skills=current_skills,
        daily_hours=float(daily_hours)
    )

    response = f"""# CareerSetu AI Career Analysis

## Target Role
{result["target_role"]}

## Readiness
{result["readiness"]}%

## Matched Skills
{", ".join(result["matched_skills"]) if result["matched_skills"] else "None"}

## Skill Gaps
{", ".join(result["skill_gaps"]) if result["skill_gaps"] else "No major skill gaps identified"}

## Agent Reasoning
**Priority Skill:** {result["reasoning"]["priority_skill"]}

**Why:** {result["reasoning"]["reason"]}

**Strategy:** {result["reasoning"]["strategy"]}

**Expected Outcome:** {result["reasoning"]["outcome"]}

## Next Action
{result["next_action"]}

## Personalized Roadmap
"""

    for item in result["roadmap"]:
        response += f"""
### {item["skill"]} — {item["priority"]}
**Action:** {item["action"]}

**Assessment:**
1. {item["assessment"][0]}
2. {item["assessment"][1]}
3. {item["assessment"][2]}
"""

    response += f"""
## Recommended Portfolio Project
{result["recommended_project"]}

## Agent Status
{result["agent_status"]}
"""

    os.makedirs("/aikart", exist_ok=True)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(
            {
                "format": "markdown",
                "response": response
            },
            f,
            ensure_ascii=False,
            indent=2
        )


if __name__ == "__main__":
    main()