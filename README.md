# Google Gemini 3 + Salesforce: Visual Service Agent 👁️

![Gemini 3](https://img.shields.io/badge/AI-Gemini%203%20Pro-purple)
![Salesforce](https://img.shields.io/badge/Cloud-Field%20Service-orange)
![Status](https://img.shields.io/badge/Release-Preview-blue)

**Repo Owner:** Burak Fenerci  
**Tech:** Gemini 3 Pro Preview, Python, Salesforce Field Service

## 🚀 The Upgrade (2026 Edition)
This project leverages **Gemini 3 Pro** (`gemini-3-pro-preview`), released in late 2025. 

## 🧠 Why Gemini 3 Pro?
Unlike previous models, Gemini 3 Pro provides **Deep Reasoning** capabilities required for industrial diagnostics. It doesn't just "see" rust; it infers structural integrity risks and maps them to JSON schemas for Salesforce automation.

## 🏗️ Architecture
1. **Salesforce Field Service:** Technician uploads a photo to a Work Order.
2. **Python Agent:** Intercepts the upload.
3. **Gemini 3 Pro:** performs visual analysis and returns a structured JSON diagnosis.
4. **Salesforce Update:** The agent auto-populates the "Recommended Action" field.

## 🛠️ Usage
```bash
pip install -r requirements.txt
export GOOGLE_API_KEY="AIza..."
python -m src.main