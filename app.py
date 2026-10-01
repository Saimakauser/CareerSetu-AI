import streamlit as st

from data import get_roles
from agent import run_career_agent
from tools import adaptive_recommendation


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="CareerSetu AI",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CLEAN PROFESSIONAL UI
# ============================================================

st.markdown(
    """
    <style>

    /* ======================================================
       GLOBAL
    ====================================================== */

    .stApp {
        background: #f6f8fc;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1250px;
    }

    h1, h2, h3, h4 {
        color: #172033 !important;
    }

    p, li {
        color: #374151;
    }

    /* ======================================================
       SIDEBAR
    ====================================================== */

    [data-testid="stSidebar"] {
        background: #111827;
        border-right: 1px solid #1f2937;
    }

    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] label {
        color: #f9fafb !important;
    }

    [data-testid="stSidebar"] .stMarkdown {
        color: #f9fafb !important;
    }

    /* Sidebar inputs */

    [data-testid="stSidebar"] input,
    [data-testid="stSidebar"] textarea {
        background: #1f2937 !important;
        color: #ffffff !important;
        border: 1px solid #374151 !important;
    }

    [data-testid="stSidebar"] input::placeholder,
    [data-testid="stSidebar"] textarea::placeholder {
        color: #9ca3af !important;
    }

    [data-testid="stSidebar"] [data-baseweb="select"] {
        background: #1f2937 !important;
    }

    [data-testid="stSidebar"] [data-baseweb="select"] * {
        color: #ffffff !important;
    }

    /* Sidebar button */

    [data-testid="stSidebar"] .stButton button {
        background: #6366f1 !important;
        color: #ffffff !important;
        border: none !important;
        font-weight: 700 !important;
        border-radius: 10px !important;
    }

    [data-testid="stSidebar"] .stButton button:hover {
        background: #4f46e5 !important;
    }


    /* ======================================================
       MAIN HEADER
    ====================================================== */

    .main-title {
        font-size: 44px;
        font-weight: 800;
        color: #172033 !important;
        margin-bottom: 4px;
        letter-spacing: -1px;
    }

    .subtitle {
        font-size: 18px;
        color: #667085 !important;
        margin-bottom: 25px;
    }

    .hero-line {
        height: 4px;
        width: 90px;
        background: #6366f1;
        border-radius: 10px;
        margin-bottom: 25px;
    }


    /* ======================================================
       INFORMATION CARDS
    ====================================================== */

    .info-card {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 14px;
        padding: 18px;
        margin-bottom: 14px;
        box-shadow: 0 2px 8px rgba(15, 23, 42, 0.04);
    }

    .info-card-title {
        color: #172033 !important;
        font-size: 17px;
        font-weight: 700;
        margin-bottom: 7px;
    }

    .info-card-text {
        color: #667085 !important;
        font-size: 14px;
        line-height: 1.5;
    }


    /* ======================================================
       AGENT CARDS
    ====================================================== */

    .agent-card {
        background: #eef2ff;
        border: 1px solid #c7d2fe;
        border-left: 5px solid #6366f1;
        border-radius: 12px;
        padding: 18px;
        margin: 10px 0 16px 0;
    }

    .agent-card-title {
        color: #3730a3 !important;
        font-weight: 800;
        font-size: 16px;
        margin-bottom: 8px;
    }

    .agent-card-text {
        color: #374151 !important;
        line-height: 1.55;
    }


    /* ======================================================
       WORKFLOW
    ====================================================== */

    .workflow-step {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 12px;
        padding: 14px 8px;
        text-align: center;
        min-height: 85px;
        box-shadow: 0 2px 6px rgba(15, 23, 42, 0.03);
    }

    .workflow-number {
        color: #6366f1 !important;
        font-size: 13px;
        font-weight: 800;
    }

    .workflow-label {
        color: #172033 !important;
        font-size: 14px;
        font-weight: 700;
        margin-top: 5px;
    }


    /* ======================================================
       METRICS
    ====================================================== */

    [data-testid="stMetric"] {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 12px;
        padding: 14px;
        box-shadow: 0 2px 6px rgba(15, 23, 42, 0.03);
    }

    [data-testid="stMetricLabel"] {
        color: #667085 !important;
    }

    [data-testid="stMetricValue"] {
        color: #172033 !important;
    }


    /* ======================================================
       PROGRESS BAR
    ====================================================== */

    [data-testid="stProgress"] > div > div {
        background: #6366f1 !important;
    }


    /* ======================================================
       EXPANDERS
    ====================================================== */

    [data-testid="stExpander"] {
        background: #ffffff !important;
        border: 1px solid #e5e7eb !important;
        border-radius: 12px !important;
        margin-bottom: 10px;
    }

    [data-testid="stExpander"] summary {
        color: #172033 !important;
        font-weight: 600 !important;
    }

    [data-testid="stExpander"] p,
    [data-testid="stExpander"] li {
        color: #374151 !important;
    }


    /* ======================================================
       MAIN INPUTS
    ====================================================== */

    [data-baseweb="select"] {
        background: #ffffff !important;
    }

    [data-baseweb="select"] * {
        color: #172033 !important;
    }

    input,
    textarea {
        background: #ffffff !important;
        color: #172033 !important;
        border-color: #d1d5db !important;
    }

    input::placeholder,
    textarea::placeholder {
        color: #9ca3af !important;
    }


    /* ======================================================
       BUTTONS
    ====================================================== */

    .stButton button {
        border-radius: 9px !important;
        font-weight: 600 !important;
        border: 1px solid #d1d5db !important;
        background: #ffffff !important;
        color: #172033 !important;
    }

    .stButton button:hover {
        border-color: #6366f1 !important;
        color: #4f46e5 !important;
    }


    /* ======================================================
       SLIDER
    ====================================================== */

    [data-testid="stSlider"] {
        color: #172033 !important;
    }


    /* ======================================================
       ALERTS
    ====================================================== */

    [data-testid="stAlert"] {
        border-radius: 10px !important;
    }


    /* ======================================================
       DIVIDER
    ====================================================== */

    hr {
        border-color: #e5e7eb !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">🎯 CareerSetu AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="subtitle">
    Your agentic career navigator — identify skill gaps,
    build a personalized roadmap, assess progress and take the next action.
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    '<div class="hero-line"></div>',
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.markdown("## 🎯 CareerSetu AI")
st.sidebar.caption("Personalized Career Intelligence")

st.sidebar.markdown("---")

st.sidebar.markdown("### 👤 Student Profile")

student_name = st.sidebar.text_input(
    "Your Name",
    value="Student"
)

roles = get_roles()

target_role = st.sidebar.selectbox(
    "Target Career",
    roles
)

skills_text = st.sidebar.text_area(
    "Current Skills",
    value="Python, SQL, Git",
    height=100,
    help="Enter skills separated by commas."
)

daily_hours = st.sidebar.number_input(
    "Daily Learning Time (hours)",
    min_value=0.5,
    max_value=12.0,
    value=2.0,
    step=0.5
)

st.sidebar.markdown("")

analyze_button = st.sidebar.button(
    "🚀 Analyze My Career",
    use_container_width=True
)


# ============================================================
# SESSION STATE
# ============================================================

if "result" not in st.session_state:
    st.session_state.result = None

if "assessment_score" not in st.session_state:
    st.session_state.assessment_score = 0

if "assessment_skill" not in st.session_state:
    st.session_state.assessment_skill = None


# ============================================================
# RUN AGENT
# ============================================================

if analyze_button:

    current_skills = [
        skill.strip()
        for skill in skills_text.split(",")
        if skill.strip()
    ]

    if not current_skills:

        st.error("Please enter at least one current skill.")

    else:

        with st.spinner(
            "CareerSetu is analyzing your career profile..."
        ):

            result = run_career_agent(
                target_role=target_role,
                current_skills=current_skills,
                daily_hours=daily_hours
            )

            st.session_state.result = result
            st.session_state.assessment_score = 0
            st.session_state.assessment_skill = None

        st.success("Career analysis completed.")


# ============================================================
# LANDING PAGE
# ============================================================

if st.session_state.result is None:

    st.info(
        "👈 Add your profile details in the sidebar and click "
        "**Analyze My Career** to start."
    )

    st.header("Supported Career Paths")

    cols = st.columns(3)

    for index, role in enumerate(roles):

        with cols[index % 3]:

            st.markdown(
                f"""
                <div class="info-card">
                    <div class="info-card-title">🎯 {role}</div>
                    <div class="info-card-text">
                        Personalized skills, learning roadmap and
                        portfolio guidance.
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("")

    st.header("How the CareerSetu Agent Works")

    workflow = [
        ("01", "Understand"),
        ("02", "Analyze"),
        ("03", "Prioritize"),
        ("04", "Plan"),
        ("05", "Adapt"),
        ("06", "Deliver")
    ]

    workflow_cols = st.columns(6)

    for col, (number, label) in zip(
        workflow_cols,
        workflow
    ):

        with col:

            st.markdown(
                f"""
                <div class="workflow-step">
                    <div class="workflow-number">{number}</div>
                    <div class="workflow-label">{label}</div>
                </div>
                """,
                unsafe_allow_html=True
            )


# ============================================================
# RESULTS
# ============================================================

if st.session_state.result is not None:

    result = st.session_state.result

    st.header(
        f"Career Analysis — {student_name}"
    )

    st.caption(
        f"Target career: {result['target_role']}  •  "
        f"Daily learning time: {result['daily_hours']} hour(s)"
    )


    # ========================================================
    # READINESS
    # ========================================================

    st.subheader("📊 Career Readiness")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Readiness",
            f"{result['readiness']}%"
        )

    with col2:
        st.metric(
            "Matched Skills",
            len(result["matched_skills"])
        )

    with col3:
        st.metric(
            "Skill Gaps",
            len(result["skill_gaps"])
        )

    st.progress(
        result["readiness"] / 100
    )


    # ========================================================
    # PROFILE ANALYSIS
    # ========================================================

    st.subheader("🔎 Profile Analysis")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### ✅ Matched Skills")

        if result["matched_skills"]:

            for skill in result["matched_skills"]:
                st.write(f"✓ {skill}")

        else:

            st.caption("No required skills matched yet.")

    with col2:

        st.markdown("### ⚠️ Skill Gaps")

        if result["skill_gaps"]:

            for skill in result["skill_gaps"]:
                st.write(f"• {skill}")

        else:

            st.caption("No major skill gaps identified.")


    # ========================================================
    # AGENT REASONING
    # ========================================================

    st.subheader("🧠 Agent Reasoning")

    reasoning = result["reasoning"]

    st.markdown(
        f"""
        <div class="agent-card">
            <div class="agent-card-title">
                CareerSetu Decision
            </div>
            <div class="agent-card-text">
                {reasoning["agent_summary"]}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    with st.expander("View detailed agent decision"):

        st.write(
            f"**Priority Skill:** {reasoning['priority_skill']}"
        )

        st.write(
            f"**Priority Level:** {reasoning['priority']}"
        )

        st.write("**Why this skill?**")
        st.write(reasoning["reason"])

        st.write("**7-Day Strategy**")
        st.write(reasoning["strategy"])

        st.write("**Measurable Outcome**")
        st.write(reasoning["outcome"])


    # ========================================================
    # NEXT ACTION
    # ========================================================

    st.subheader("🚀 Agent's Next Action")

    st.markdown(
        f"""
        <div class="agent-card">
            <div class="agent-card-title">
                Recommended Next Step
            </div>
            <div class="agent-card-text">
                {result["next_action"]}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


    # ========================================================
    # PERSONALIZED ROADMAP
    # ========================================================

    st.subheader("🗺️ Personalized Skill Roadmap")

    if result["roadmap"]:

        for index, item in enumerate(
            result["roadmap"],
            start=1
        ):

            with st.expander(
                f"{index}. {item['skill']}  •  {item['priority']} Priority"
            ):

                st.write("**Learning Action**")
                st.write(item["action"])

                st.write("**Assessment Questions**")

                for question in item["assessment"]:
                    st.write(f"• {question}")

    else:

        st.success(
            "🎉 All required skills are currently matched."
        )


    # ========================================================
    # ADAPTIVE ASSESSMENT
    # ========================================================

    st.subheader("🧪 Adaptive Agent Assessment")

    if result["skill_gaps"]:

        assessment_skill = st.selectbox(
            "Choose a skill to assess",
            result["skill_gaps"],
            key="assessment_skill_select"
        )

        st.write(
            "Use the roadmap questions to assess your understanding, "
            "then enter your estimated score."
        )

        score = st.slider(
            "Assessment Score",
            min_value=0,
            max_value=100,
            value=50,
            step=5,
            key="assessment_slider"
        )

        if st.button(
            "🤖 Get Agent Recommendation",
            key="assessment_button"
        ):

            recommendation = adaptive_recommendation(
                assessment_skill,
                score
            )

            st.session_state.assessment_score = score
            st.session_state.assessment_skill = assessment_skill

            st.success(
                "Assessment processed successfully."
            )

            st.markdown(
                f"""
                <div class="agent-card">
                    <div class="agent-card-title">
                        Adaptive Recommendation
                    </div>
                    <div class="agent-card-text">
                        {recommendation}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

    else:

        st.success(
            "🎉 No current skill gaps. "
            "The agent recommends advanced projects and assessments."
        )


    # ========================================================
    # PORTFOLIO PROJECT
    # ========================================================

    st.subheader("💼 Agent-Recommended Portfolio Project")

    st.markdown(
        f"""
        <div class="info-card">
            <div class="info-card-title">
                {result["recommended_project"]}
            </div>
            <div class="info-card-text">
                This project is selected according to the target role
                and identified skill gaps.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


    # ========================================================
    # AGENT WORKFLOW
    # ========================================================

    st.subheader("⚙️ Agent Workflow")

    workflow = [
        ("🧠", "Understand"),
        ("🔍", "Analyze"),
        ("⚖️", "Prioritize"),
        ("🗺️", "Plan"),
        ("🔄", "Adapt"),
        ("📦", "Deliver")
    ]

    workflow_cols = st.columns(6)

    for col, (icon, label) in zip(
        workflow_cols,
        workflow
    ):

        with col:

            st.markdown(
                f"""
                <div class="workflow-step">
                    <div style="font-size:22px;">{icon}</div>
                    <div class="workflow-label">{label}</div>
                </div>
                """,
                unsafe_allow_html=True
            )


    # ========================================================
    # RESET
    # ========================================================

    st.markdown("---")

    if st.button(
        "🔄 Start New Career Analysis",
        key="reset_analysis"
    ):

        st.session_state.result = None
        st.session_state.assessment_score = 0
        st.session_state.assessment_skill = None

        st.rerun()