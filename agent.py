from tools import (
    analyze_skill_gap,
    prioritize_gaps,
    get_learning_action,
    create_assessment,
    calculate_readiness,
    adaptive_recommendation,
    recommend_project
)


def generate_agent_reasoning(
    target_role,
    current_skills,
    matched,
    gaps,
    daily_hours
):
    """
    Free deterministic reasoning layer.
    No paid API or external LLM required.
    """

    if gaps:
        first_gap = gaps[0]
        priority = "HIGH"
        reason = (
            f"{first_gap} is the first priority because it is a "
            f"required skill for the {target_role} role and is currently "
            f"missing from the student's profile."
        )

        strategy = (
            f"Spend approximately {daily_hours} hour(s) per day on "
            f"{first_gap}. Start with fundamentals, practice small "
            f"problems, and finish with a practical task."
        )

        outcome = (
            f"By the end of 7 days, the student should be able to "
            f"explain the fundamentals of {first_gap} and demonstrate "
            f"it through a small practical implementation."
        )

    else:
        first_gap = None
        priority = "NONE"

        reason = (
            f"The student's listed skills currently cover the required "
            f"skills for the {target_role} role."
        )

        strategy = (
            "Move from skill acquisition toward advanced projects, "
            "role-specific assessments and portfolio development."
        )

        outcome = (
            "Complete an advanced role-specific project and demonstrate "
            "the required skills through an assessment."
        )

    return {
        "priority_skill": first_gap or "Advanced role-specific skills",
        "priority": priority,
        "reason": reason,
        "strategy": strategy,
        "outcome": outcome,
        "agent_summary": (
            f"CareerSetu analyzed the student's current skills against "
            f"the {target_role} skill requirements, identified "
            f"{len(gaps)} skill gap(s), prioritized them, and created "
            f"an adaptive learning path."
        )
    }


def run_career_agent(target_role, current_skills, daily_hours):

    # --------------------------------------------------
    # 1. UNDERSTAND
    # --------------------------------------------------
    matched, gaps = analyze_skill_gap(
        target_role,
        current_skills
    )

    # --------------------------------------------------
    # 2. REASON
    # --------------------------------------------------
    priorities = prioritize_gaps(gaps)

    # --------------------------------------------------
    # 3. PLAN
    # --------------------------------------------------
    readiness = calculate_readiness(
        target_role,
        current_skills
    )

    roadmap = []

    for skill in gaps:
        roadmap.append({
            "skill": skill,
            "priority": priorities[skill],
            "action": get_learning_action(skill),
            "assessment": create_assessment(skill)
        })

    # --------------------------------------------------
    # 4. AGENT DECISION
    # --------------------------------------------------
    reasoning = generate_agent_reasoning(
        target_role,
        current_skills,
        matched,
        gaps,
        daily_hours
    )

    if gaps:
        next_skill = gaps[0]

        next_action = (
            f"Start with {next_skill}. "
            f"It is currently the highest-priority skill gap."
        )
    else:
        next_action = (
            "Move to advanced projects and role-specific assessments."
        )

    # --------------------------------------------------
    # 5. RECOMMEND PROJECT
    # --------------------------------------------------
    project = recommend_project(
        target_role,
        gaps
    )

    # --------------------------------------------------
    # 6. DELIVER
    # --------------------------------------------------
    return {
        "target_role": target_role,
        "current_skills": current_skills,
        "matched_skills": matched,
        "skill_gaps": gaps,
        "roadmap": roadmap,
        "readiness": readiness,
        "daily_hours": daily_hours,
        "next_action": next_action,
        "reasoning": reasoning,
        "recommended_project": project,
        "agent_status": "Completed"
    }