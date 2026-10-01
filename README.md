🎯 CareerSetu AI

Agentic AI Career & Skill Development Platform

CareerSetu AI is an agentic career guidance platform that helps students understand their career readiness, identify skill gaps, prioritize what to learn, and create a personalized learning roadmap.

🌏 Problem Statement

Students often know which career they want, but they don't know:

Which skills are actually required for that career
Which skills they already have
Which skills they are missing
What they should learn first
How to measure their progress
What practical project they should build

Career guidance is often static and generic. Students need a system that can analyze their individual profile and turn it into an actionable learning plan.

💡 Our Solution

CareerSetu AI acts as a career and skill development agent.

It takes:

Target career
Current skills
Available daily learning time

and produces:

Career readiness percentage
Matched skills
Skill gaps
Prioritized learning areas
Personalized learning roadmap
Skill assessments
Adaptive recommendations
Portfolio project recommendation

🤖 Agentic Workflow

1. Understand

The agent receives the student's target career, current skills and available learning time.

2. Analyze

It compares the student's current skills with the skills required for the selected career.

3. Prioritize

The agent identifies missing skills and assigns priorities based on the learning sequence.

4. Plan

It generates learning actions and assessment questions for the identified skill gaps.

5. Assess & Adapt

The student can assess their understanding of a skill. Based on the score, the agent recommends revision, additional practice or progression.

6. Deliver

The agent delivers the final roadmap, next action and a practical portfolio project.

✨ Key Features

📊 Career Readiness

Calculates how many required career skills the student currently matches.

🔎 Skill Gap Analysis

Clearly separates matched skills from missing skills.

🧠 Agent Reasoning

Explains why a particular skill has been prioritized.

🗺️ Personalized Roadmap

Creates learning actions and assessment questions for each skill gap.

🧪 Adaptive Assessment

Uses assessment performance to recommend the next learning action.

💼 Portfolio Project Recommendation

Suggests a practical project aligned with the selected career.

🎯 Supported Career Paths

CareerSetu AI currently supports:

Software Engineer
Full Stack Developer
Data Analyst
Data Scientist
AI / ML Engineer
Cybersecurity Analyst
Cloud Engineer
DevOps Engineer
UI/UX Designer
Product Manager
Business Analyst
Financial Analyst
Digital Marketing Specialist

🏗️ System Architecture

                    ┌─────────────────────┐
                    │     Student Input   │
                    │ Career + Skills +   │
                    │ Learning Time       │
                    └──────────┬──────────┘
                               │
                               ↓
                    ┌─────────────────────┐
                    │    CareerSetu Agent │
                    └──────────┬──────────┘
                               │
                ┌──────────────┼──────────────┐
                ↓              ↓              ↓
          Skill Analysis   Prioritization   Readiness
                │              │              │
                └──────────────┼──────────────┘
                               ↓
                    ┌─────────────────────┐
                    │ Learning Roadmap    │
                    │ + Assessments       │
                    └──────────┬──────────┘
                               ↓
                    ┌─────────────────────┐
                    │ Adaptive Feedback    │
                    └──────────┬──────────┘
                               ↓
                    ┌─────────────────────┐
                    │ Next Action +        │
                    │ Portfolio Project    │
                    └─────────────────────┘


🛠️ Technology Stack

Python — Core application logic

Streamlit — Interactive web dashboard

Tool-Based Agent Architecture — Career analysis, prioritization and adaptive decision flow

Docker — Containerization

Git & GitHub — Version control and source code management

The current prototype uses a deterministic tool-based agent architecture and does not require a paid external LLM or API key.

📁 Project Structure

agent.py — Agent orchestration and career analysis workflow

app.py — Streamlit dashboard and user interface

data.py — Career skill requirements and learning resources

tools.py — Skill analysis, prioritization, assessment and recommendation tools

requirements.txt — Python dependencies

Dockerfile — Container configuration

README.md — Project documentation

🚀 How to Run Locally

Clone the repository:

git clone https://github.com/Saimakauser/CareerSetu-AI.git

Move into the project:

cd CareerSetu-AI

Create a virtual environment:

python -m venv .venv

Activate it on Windows:

.venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Run the application:

streamlit run app.py

The CareerSetu AI dashboard will open in your browser.

🐳 Docker

Build the Docker image:

docker build -t careersetu-ai .

Run the application:

docker run -p 8501:8501 careersetu-ai

Then open:

http://localhost:8501

💰 Cost & API Requirements

CareerSetu AI currently requires ₹0 external API cost.

The prototype does not require:

OpenAI API
Paid LLM APIs
External database
Paid authentication service

The core agent workflow runs using Python-based tools and logic.

🇮🇳 Bharat Impact

CareerSetu AI focuses on a practical challenge faced by students and early-career learners: converting a career goal into a clear, personalized and actionable skill-development path.

The platform can be extended for:

Students from different educational backgrounds
Regional and multilingual career guidance
Placement preparation
Institution-specific career pathways
Job-market skill requirements
Personalized project recommendations
Skill progress tracking

🔮 Future Scope

Future versions can include:

Conversational AI career guidance
Resume analysis
Job-description analysis
Real-time job-market skill analysis
Multilingual support
Student accounts and progress tracking
Institution dashboards
Personalized learning-resource recommendations
Advanced AI-generated assessments

🎥 Demo

The demo showcases:

1. Student profile input

2. Target career selection

3. Skill-gap analysis

4. Career readiness calculation

5. Agent reasoning

6. Personalized roadmap

7. Adaptive assessment

8. Portfolio project recommendation

👤 Project

Project Name: CareerSetu AI

Developer: Saima Kauser

GitHub Repository: https://github.com/Saimakauser/CareerSetu-AI

Domain: EdTech & Future Skills


📜 Project Status

Working Prototype

CareerSetu AI is currently implemented as a functional Streamlit prototype demonstrating an end-to-end agentic career and skill-development workflow.