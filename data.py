# ==================================================
# CAREERSETU AI - ROLE SKILL DATABASE
# ==================================================

ROLE_SKILLS = {

    "Software Engineer": [
        "Python",
        "SQL",
        "Git",
        "Data Structures & Algorithms",
        "REST APIs",
        "Testing",
        "System Design"
    ],

    "Full Stack Developer": [
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Node.js",
        "REST APIs",
        "SQL",
        "Git"
    ],

    "Data Analyst": [
        "Python",
        "SQL",
        "Excel",
        "Statistics",
        "Data Visualization",
        "Power BI"
    ],

    "Data Scientist": [
        "Python",
        "SQL",
        "Statistics",
        "Machine Learning",
        "Pandas",
        "Data Visualization",
        "Model Evaluation"
    ],

    "AI / ML Engineer": [
        "Python",
        "Statistics",
        "Machine Learning",
        "Deep Learning",
        "SQL",
        "Model Deployment",
        "APIs"
    ],

    "Cybersecurity Analyst": [
        "Linux",
        "Networking",
        "Python",
        "SIEM",
        "Threat Detection",
        "Vulnerability Management",
        "Incident Response"
    ],

    "Cloud Engineer": [
        "Linux",
        "Networking",
        "AWS",
        "Cloud Security",
        "Docker",
        "Python",
        "Terraform"
    ],

    "DevOps Engineer": [
        "Linux",
        "Git",
        "Docker",
        "CI/CD",
        "Kubernetes",
        "Cloud",
        "Python"
    ],

    "UI/UX Designer": [
        "Figma",
        "User Research",
        "Wireframing",
        "Prototyping",
        "Visual Design",
        "Usability Testing"
    ],

    "Product Manager": [
        "Product Strategy",
        "User Research",
        "Market Analysis",
        "Roadmapping",
        "Analytics",
        "Communication"
    ],

    "Business Analyst": [
        "Excel",
        "SQL",
        "Business Analysis",
        "Data Visualization",
        "Requirements Gathering",
        "Communication"
    ],

    "Financial Analyst": [
        "Excel",
        "Financial Modeling",
        "Accounting",
        "Statistics",
        "Data Analysis",
        "Financial Reporting"
    ],

    "Digital Marketing Specialist": [
        "SEO",
        "Content Marketing",
        "Google Analytics",
        "Social Media",
        "Email Marketing",
        "Copywriting"
    ]
}


# ==================================================
# LEARNING RESOURCES
# ==================================================

RESOURCES = {

    "Python":
        "Practice Python fundamentals, functions, data structures and problem solving.",

    "SQL":
        "Practice SELECT, JOIN, GROUP BY, subqueries and database queries.",

    "Git":
        "Practice repositories, commits, branches, pull requests and collaboration.",

    "Data Structures & Algorithms":
        "Practice arrays, strings, hash maps, recursion and basic algorithms.",

    "REST APIs":
        "Learn HTTP methods, JSON, authentication and build a REST API.",

    "Testing":
        "Learn unit testing and write tests for a Python project.",

    "System Design":
        "Learn APIs, databases, caching and scalable application architecture.",

    "HTML":
        "Build semantic web pages using modern HTML.",

    "CSS":
        "Practice responsive layouts using Flexbox and Grid.",

    "JavaScript":
        "Learn modern JavaScript, DOM manipulation and asynchronous programming.",

    "React":
        "Build reusable components and a small React application.",

    "Node.js":
        "Learn backend development using Node.js and build a small API.",

    "Excel":
        "Practice formulas, pivot tables, charts and data cleaning.",

    "Statistics":
        "Learn probability, distributions, averages and hypothesis testing.",

    "Data Visualization":
        "Build dashboards using charts, KPIs and business datasets.",

    "Power BI":
        "Create an interactive dashboard using a business dataset.",

    "Machine Learning":
        "Learn supervised learning, feature engineering and model evaluation.",

    "Deep Learning":
        "Study neural networks, CNNs and transformer fundamentals.",

    "Pandas":
        "Practice data cleaning, transformation and analysis using Pandas.",

    "Model Evaluation":
        "Learn accuracy, precision, recall, F1-score and ROC-AUC.",

    "Model Deployment":
        "Learn how to expose machine learning models through APIs and deploy them.",

    "APIs":
        "Learn API architecture, requests, responses, authentication and integration.",

    "Linux":
        "Practice shell commands, permissions, processes and system administration.",

    "Networking":
        "Learn TCP/IP, DNS, HTTP, routing and network troubleshooting.",

    "SIEM":
        "Practice log analysis, alert correlation and security monitoring.",

    "Threat Detection":
        "Study common attack patterns and create detection rules.",

    "Vulnerability Management":
        "Learn vulnerability identification, prioritization and remediation.",

    "Incident Response":
        "Practice detection, investigation, containment and recovery.",

    "AWS":
        "Learn cloud compute, storage, networking and AWS fundamentals.",

    "Cloud Security":
        "Learn identity, access control, encryption and cloud security fundamentals.",

    "Docker":
        "Containerize a small application and learn images, containers and volumes.",

    "Terraform":
        "Learn infrastructure as code and provision basic cloud resources.",

    "CI/CD":
        "Build an automated pipeline that tests and deploys an application.",

    "Kubernetes":
        "Learn containers, pods, deployments and basic orchestration.",

    "Cloud":
        "Learn cloud computing fundamentals, compute, storage and networking.",

    "Figma":
        "Create wireframes, prototypes and a small responsive design.",

    "User Research":
        "Practice interviews, surveys and identifying user pain points.",

    "Wireframing":
        "Create low-fidelity layouts for a digital product.",

    "Prototyping":
        "Build interactive prototypes and test user flows.",

    "Visual Design":
        "Practice typography, layout, hierarchy and visual consistency.",

    "Usability Testing":
        "Test designs with users and identify usability problems.",

    "Product Strategy":
        "Learn product vision, goals, prioritization and market positioning.",

    "Market Analysis":
        "Study customers, competitors, market size and business opportunities.",

    "Roadmapping":
        "Create product roadmaps using goals, priorities and timelines.",

    "Analytics":
        "Use product metrics to understand user behavior and outcomes.",

    "Communication":
        "Practice structured communication, presentations and stakeholder updates.",

    "Business Analysis":
        "Learn business processes, analysis frameworks and decision making.",

    "Requirements Gathering":
        "Practice collecting, documenting and validating stakeholder requirements.",

    "Financial Modeling":
        "Build financial models using assumptions, formulas and forecasts.",

    "Accounting":
        "Learn financial statements, accounting principles and basic reporting.",

    "Data Analysis":
        "Practice cleaning, analyzing and interpreting business datasets.",

    "Financial Reporting":
        "Learn how to prepare and interpret financial reports.",

    "SEO":
        "Learn keyword research, on-page SEO and search performance.",

    "Content Marketing":
        "Create useful content strategies for a target audience.",

    "Google Analytics":
        "Learn web analytics, traffic sources, events and conversion metrics.",

    "Social Media":
        "Learn social media strategy, engagement and campaign measurement.",

    "Email Marketing":
        "Learn email campaigns, segmentation and performance metrics.",

    "Copywriting":
        "Practice writing clear, persuasive and audience-focused content."
}


def get_roles():
    """
    Return all supported career roles.
    """
    return list(ROLE_SKILLS.keys())