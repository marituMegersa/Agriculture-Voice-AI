# Agriculture & Voice AI Advisory System 🌾🗣️

[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black)](https://react.dev/)
[![Languages](https://img.shields.io/badge/Languages-Amharic%20%7C%20Afaan%20Oromo-teal?style=for-the-badge)]()

**Multilingual Voice-Enabled Speech-to-Text Crop Diagnostic & Soil Advisor for Smallholder Farmers**

---

## 🌟 Key Features

- **Voice Audio Intake**: Speech-to-Text processing for local languages (Amharic & Afaan Oromo).
- **Crop Disease Diagnostic Engine**: Identifies yellow rust, nitrogen deficiency, and blight from symptom descriptions.
- **Soil & Irrigation Advisory**: Computes optimal Urea/DAP fertilizer dosage and watering schedules.
- **Localized Audio Feedback**: Generates spoken diagnostic summaries for frontline agricultural extension agents.

---

## 📂 Monorepo Structure

```text
Agriculture-Voice-AI/
├── apps/
│   ├── api/                     # Python 3.12 FastAPI Backend
│   │   ├── app/domain/crop_advisory/
│   │   │   ├── models.py        # Farmer & Diagnostic ORM Models
│   │   │   ├── schemas.py       # Pydantic v2 Voice Intake Schemas
│   │   │   ├── service.py       # Disease Diagnostic Engine
│   │   │   └── router.py        # REST Endpoints
│   │   └── main.py
│   └── web/                     # React 18 Voice Dashboard
├── docker-compose.yml
└── README.md
```

---

## 🚀 Quick Start
```bash
# Backend
cd apps/api && pip install -r requirements.txt && python main.py

# Frontend
cd apps/web && npm install && npm run dev
```
