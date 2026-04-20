# DevOps Test Project - Effective Mobile

## 📌 Project Description

This project demonstrates a simple containerized web application using Docker and an Nginx reverse proxy.

The system consists of:

- Backend service (Python HTTP server)
- Nginx reverse proxy
- Docker Compose for orchestration

---

## 🏗 Architecture

Client → Nginx → Backend (Python HTTP Server)

---

## 📦 Requirements

Before running the project, make sure you have installed:

- Docker
- Docker Compose
- Git

---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository

Open terminal (CMD / PowerShell) and run:

```bash
git clone https://github.com/beriidzze/devops-test.git
```

### 2️⃣ Enter Project Folder

```bash
cd devops-test
```

### 3️⃣ Run the Project

```bash
docker compose up --build
```

Wait until containers start.

---

### 4️⃣ Open in Browser

After startup, open your browser and go to:

```
http://localhost
```

---

### 5️⃣ Test via Terminal (Optional)

You can also test using curl:

```bash
curl http://localhost
```

---

## 📤 Expected Output

```
Hello from Effective Mobile!
```

---

## 🛑 Stop the Project

```bash
docker compose down
```

## 🧠 How It Works

- Nginx listens on port 80
- Nginx forwards requests to backend
- Backend runs on port 8080 (internal only)