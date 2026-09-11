# Agriculture & Voice AI Advisory System

[![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-009688.svg?style=flat&logo=fastapi)](https://fastapi.tiangolo.com)
[![React](https://img.shields.io/badge/React-18-61DAFB.svg?style=flat&logo=react)](https://react.dev)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB.svg?style=flat&logo=python)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

> **Multilingual Voice Diagnostics & Localized Crop Health Advisory**

A voice-enabled agricultural advisory platform built for smallholder farmers. Supports speech inputs in Ethiopian national languages (Amharic/Oromo), performs automated crop disease diagnosis, and delivers tailored fertilizer/treatment recommendations.

---

## 🏛️ Clean Architecture Overview

This repository is built following **Clean Layered Architecture** standards:

```
apps/api/app/
├── api/          # Thin REST routers & Dependency Injection (deps.py)
├── schemas/      # Pydantic v2 validation DTOs (Request / Response)
├── models/       # SQLAlchemy 2.0 Async ORM models & Base declarative metadata
├── repositories/ # Dedicated async database access queries ONLY
├── services/     # Pure business logic, domain rules, & AI orchestrators
├── core/         # Settings (pydantic-settings), Async Database, JWT Security, & Exceptions
└── utils/        # Reusable helper utilities
```

---

## ✨ Key Features

- **Voice Advisory Engine**:  Amharic & English transcript analysis for crop diagnostics
- **Treatment Recommender**:  Disease-specific fungicide and fertilizer application protocols
- **Historical Diagnostics Log**:  Async database persistence of farmer query history
- **Farmer Portal UI**:  React 18 TypeScript dashboard with audio playback & diagnostic charts

---

## 🛠️ Tech Stack

- **Backend**: Python 3.12, FastAPI 0.110+, Async SQLAlchemy 2.0+, Pydantic v2
- **Frontend**: React 18, TypeScript, Tailwind CSS, Lucide Icons
- **Database & Cache**: PostgreSQL (Asyncpg), Redis, Elasticsearch
- **AI & RAG**: vLLM / Ollama, LangChain, LangGraph State Graphs
- **DevOps & Testing**: Docker, Docker Compose, Pytest, Pytest-Asyncio

---

## 🚀 Quick Start Guide

### 1. Prerequisites
- Docker & Docker Compose
- Python 3.12+
- Node.js 20+

### 2. Backend Setup
```bash
# Navigate to API directory
cd apps/api

# Install dependencies
pip install -r requirements.txt

# Run database migrations & start FastAPI app
python main.py
# API running at http://localhost:8000 (Swagger docs at http://localhost:8000/docs)
```

### 3. Frontend Setup
```bash
# Navigate to Web app directory
cd apps/web

# Install dependencies & start dev server
npm install
npm run dev
# Web app running at http://localhost:3000
```

### 4. Running via Docker Compose
```bash
docker-compose up --build
```

---

## 🧪 Testing

Run unit & integration tests using `pytest`:
```bash
cd apps/api
pytest tests/ -v
```

---

## 📜 API Documentation

Once started, interactive API documentation is available at:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

**Primary Endpoint Sample**:
`POST /api/v1/crop_advisory/diagnose`

---

## 👤 Author & Maintainer

Maintained with ❤️ by **[marituMegersa](https://github.com/marituMegersa)**.
