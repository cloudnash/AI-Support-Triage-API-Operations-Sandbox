# 🤖 AI Support Triage API & Operations Sandbox

AI Product DevOps Toolkit is an operational excellence platform designed specifically for AI SaaS teams. It provides real-time health monitoring, API troubleshooting, deployment automation, and incident management workflows—helping you maintain 99.9% uptime for AI coding agent applications and microservices


## AI-Support-Triage-API-Operations-Sandbox

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104-009688.svg)
![Docker](https://img.shields.io/badge/docker-ready-2496ED.svg)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF.svg)
![License](https://img.shields.io/badge/license-MIT-green)

A lightweight, robust API service designed to bridge the gap between AI coding agents and technical end-users. This project demonstrates how incoming technical support tickets can be automatically triaged using AI, streamlining debugging workflows, and improving the developer experience.

## 🎯 Purpose & Scope
This project was built to demonstrate core competencies in **AI Product Support, API debugging, and Cloud Operations**. It simulates an environment where developers are building applications with autonomous AI agents and require fast, reliable operational support. 

It highlights the ability to:
* Handle technical customer support workflows.
* Build and debug APIs and SaaS tools.
* Implement CI/CD pipelines and containerized deployments.
* Write clear technical documentation for L1/L2 escalation.

---

## ✨ Core Features

* **🧠 AI-Simulated Triage:** Analyzes incoming technical support queries and routes them intelligently (e.g., API Integration, DevOps/Infrastructure, General Usage).
* **🛠️ API & SaaS Debugging Ready:** Built with FastAPI, exposing clean JSON endpoints, comprehensive HTTP error handling, and automated Swagger UI documentation.
* **📊 DevOps & Observability:** Integrated structured Python logging for tracking request times, AI agent latency, and system errors. Includes a dedicated `/health` endpoint for cloud load balancers and monitoring tools (e.g., Prometheus).
* **⚙️ Automated CI/CD:** GitHub Actions pipeline validates dependencies and Docker builds on every push to the `main` branch to ensure deployment reliability.
* **🐳 Containerized Architecture:** Fully Dockerized for seamless, reproducible deployments across any cloud provider (AWS EC2, ECS, Kubernetes).

---

## 🏗️ Architecture & Workflow

1. **User Submission:** A technical user submits an issue via the `/api/v1/triage` endpoint.
2. **AI Processing:** The API passes the issue description to the AI Triage Agent.
3. **Categorization:** The agent analyzes keywords and context to categorize the ticket.
4. **Actionable Output:** The system returns a structured JSON response with the category, a suggested debugging action, and processing latency.
5. **Observability Logging:** Every step is logged to standard output for infrastructure monitoring.

---

## 🚀 Quick Start Guide

### Prerequisites
* Python 3.9+ (For local development)
* Docker & Docker Compose (For containerized deployment)
* Git

### Local Installation

1. **Clone the repository:**
   ```
   git clone [https://github.com/cloudnash/ai-support-triage-api.git](https://github.com/cloudnash/ai-support-triage-api.git)
   cd ai-support-triage-api
   ```
2. **Set up a virtual environment (Optional but recommended):**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```
   pip install -r app/requirements.txt
   ```
5. Run the application:
   
   ```
   uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
   ```

### Docker Deployment

To run the service in an isolated container:

```
# Build the Docker image
docker build -t ai-triage-api:latest .

# Run the container mapping port 8000
docker run -d -p 8000:8000 --name support-api ai-triage-api
```
---


## 📖 API Documentation

Once the application is running, you can interact with the API using the automatically generated Swagger UI at:
👉 http://localhost:8000/docs

Main Endpoint: POST /api/v1/triage
Request Body Example:

```
{
  "user_id": "dev_123",
  "issue_description": "My deployment crashed after the AI agent committed new infrastructure code."
}
```

Response Body Example (200 OK):

```
{
  "status": "success",
  "category": "DevOps / Infrastructure",
  "suggested_action": "Review container logs and CI/CD pipeline status.",
  "processing_time_ms": 142.5
}
```
Health Endpoint: GET /health
Used by Kubernetes or AWS Application Load Balancers to verify container health

---

## 🛠️ Operations & Troubleshooting

As an AI Product Experience Specialist, maintaining operational clarity is critical.

Please refer to the Operations & Troubleshooting Runbook (docs/TROUBLESHOOTING.md) for detailed protocols on:

- L1/L2 Support Escalation Workflows
- Log Querying for SaaS Debugging
- Managing CI/CD Pipeline Failures
- Customer Communication Templates

---

## 🔄 CI/CD Pipeline
This repository utilizes GitHub Actions for continuous integration. The pipeline (.github/workflows/ci.yml) automatically triggers on push and pull requests to the main branch, executing the following jobs:

- Provisions an Ubuntu runner.
- Sets up Python 3.9.
- Installs dependencies.
- Performs a dry-run Docker build to ensure the image compiles successfully without broken dependencies.

---

