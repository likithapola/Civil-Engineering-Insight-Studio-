# Civil-Engineering-Insight-Studio-

AI-powered multimodal analysis tool built using Google Cloud Vertex AI (Gemini Vision) to automatically analyze images of civil engineering structures and generate detailed technical descriptions.

📌 Problem Statement

Civil engineers often manually describe structures based on site images, which is time-consuming and subjective. There is a need for an automated system that can:

Identify construction materials

Analyze structural components

Generate professional project documentation

Assist in structural assessment

This project solves that problem using Generative AI.

🚀 Features

✔ Image-based material identification
✔ Automated project progress documentation
✔ Bridge structural component analysis
✔ Structured AI-generated reports
✔ Downloadable PDF reports
✔ Clean Streamlit interface
✔ Cloud-based AI processing

🧠 Tech Stack

Frontend: Streamlit

Backend: Python

Cloud Platform: Google Cloud Platform

AI Model: Gemini 1.5 Pro (Vision) via Vertex AI

PDF Generation: ReportLab

🏗️ System Architecture
User → Streamlit UI → Backend (Python)
        ↓
   Vertex AI (Gemini Vision Model)
        ↓
 Structured JSON Output
        ↓
  Formatted Civil Engineering Report

📂 Project Structure
civil-engineering-insight-studio/
│
├── app.py
├── requirements.txt
├── config.py
├── utils/
│   ├── gemini_helper.py
│   ├── prompts.py
│
├── reports/
└── README.md

🔍 Scenarios Implemented
🔹 Scenario 1 – Material Identification

Detects construction materials

Identifies location within structure

Suggests functional usage

🔹 Scenario 2 – Project Documentation

Documents completed structural elements

Lists materials used

Describes construction methods

Identifies planned phases

🔹 Scenario 3 – Bridge Structural Analysis

Identifies beams, columns, trusses

Highlights engineering challenges

Provides structural observations

⚙️ Setup Instructions
1️⃣ Clone Repository
git clone https://github.com/your-username/civil-engineering-insight-studio.git
cd civil-engineering-insight-studio

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run App
streamlit run app.py
