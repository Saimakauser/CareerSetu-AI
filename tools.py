from data import ROLE_SKILLS, RESOURCES


# --------------------------------------------------
# TOOL 1: ANALYZE SKILL GAP
# --------------------------------------------------

def analyze_skill_gap(target_role, current_skills):
    required = ROLE_SKILLS.get(target_role, [])

    current = {
        skill.strip().lower()
        for skill in current_skills
    }

    matched = [
        skill
        for skill in required
        if skill.lower() in current
    ]

    gaps = [
        skill
        for skill in required
        if skill.lower() not in current
    ]

    return matched, gaps


# --------------------------------------------------
# TOOL 2: CALCULATE CAREER READINESS
# --------------------------------------------------

def calculate_readiness(target_role, current_skills):
    required = ROLE_SKILLS.get(target_role, [])

    if not required:
        return 0

    matched, _ = analyze_skill_gap(
        target_role,
        current_skills
    )

    readiness = (
        len(matched) / len(required)
    ) * 100

    return round(readiness)


# --------------------------------------------------
# TOOL 3: PRIORITIZE SKILL GAPS
# --------------------------------------------------

def prioritize_gaps(gaps):

    priorities = {}

    for index, skill in enumerate(gaps):

        if index < 2:
            priorities[skill] = "HIGH"

        elif index < 4:
            priorities[skill] = "MEDIUM"

        else:
            priorities[skill] = "LOW"

    return priorities


# --------------------------------------------------
# TOOL 4: GENERATE LEARNING ACTION
# --------------------------------------------------

def get_learning_action(skill):

    return RESOURCES.get(
        skill,
        (
            f"Learn the fundamentals of {skill}, "
            f"practice the concepts, and complete "
            f"a small practical project."
        )
    )


# --------------------------------------------------
# TOOL 5: CREATE ASSESSMENT
# --------------------------------------------------

def create_assessment(skill):

    return [
        f"What are the core concepts of {skill}?",

        f"Give one practical example of using {skill}.",

        (
            f"How would you apply {skill} "
            f"in a real-world project?"
        )
    ]


# --------------------------------------------------
# TOOL 6: ADAPTIVE RECOMMENDATION
# --------------------------------------------------

def adaptive_recommendation(skill, score):

    if score < 50:

        return (
            f"Your assessment score is {score}%. "
            f"The agent recommends revisiting {skill} "
            f"before moving to the next skill."
        )

    elif score < 80:

        return (
            f"Your assessment score is {score}%. "
            f"The agent recommends additional practice "
            f"in {skill}."
        )

    return (
        f"Your assessment score is {score}%. "
        f"The agent considers {skill} sufficiently strong "
        f"for the next learning stage."
    )


# --------------------------------------------------
# TOOL 7: RECOMMEND PORTFOLIO PROJECT
# --------------------------------------------------

def recommend_project(target_role, skill_gaps):

    projects = {

        "Software Engineer":
            "Build a Job Application Tracker with authentication, REST APIs and SQL.",

        "Full Stack Developer":
            "Build a student placement portal with React, APIs and a database.",

        "Data Analyst":
            "Build an Indian retail analytics dashboard using sales data.",

        "Data Scientist":
            "Build a customer churn prediction system with model evaluation.",

        "AI / ML Engineer":
            "Build an AI document classification system with an API.",

        "Cybersecurity Analyst":
            "Build a security log monitoring and suspicious-login detection dashboard.",

        "Cloud Engineer":
            "Deploy a containerized web application with monitoring.",

        "DevOps Engineer":
            "Build a CI/CD pipeline that automatically tests and deploys an application.",

        "UI/UX Designer":
            "Design and prototype a mobile-first student career planning application.",

        "Product Manager":
            "Create a product discovery and roadmap case study for a Bharat-focused app.",

        "Business Analyst":
            "Build a business KPI dashboard and requirements analysis case study.",

        "Financial Analyst":
            "Build a financial performance dashboard with forecasting metrics.",

        "Digital Marketing Specialist":
            "Create a campaign analytics dashboard with SEO and engagement metrics."
    }

    return projects.get(
        target_role,
        (
            "Build a practical portfolio project "
            "demonstrating the missing skills."
        )
    )