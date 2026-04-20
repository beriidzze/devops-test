# DevOps Test Project - Effective Mobile

## 📌 Project Description

This project demonstrates a simple containerized web application using Docker and Nginx reverse proxy.

The architecture consists of:
- Backend service (Python HTTP server)
- Nginx as reverse proxy
- Docker Compose for orchestration

---

## 🏗 Architecture

Client → Nginx → Backend (Python)

---

## 🚀 How to Run the Project

### 1. Build and start containers

```bash
docker compose up --build