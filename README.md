

# LangGraph Persistent Agent (FastAPI + SQLite)

A production-style **LangGraph Module 5 project** demonstrating **persistent agent state** using SQLite, exposed via **FastAPI** with a **ChatGPT-style web UI** and chat history.

This project shows how to build **stateful AI agents** that can resume conversations across server restarts.

---

## ✨ Features

- 🧠 **LangGraph single-agent workflow**
- 💾 **Persistent memory (SQLite checkpointing)**
- 🔁 Resume conversations using `thread_id`
- 🌐 **FastAPI backend**
- 💬 **ChatGPT-style UI** (HTML + CSS + JS)
- 📜 Chat history loaded from persisted state
- ⌨️ Enter-to-send (Shift+Enter for newline)

---

## 🏗️ Architecture

```

Frontend (HTML/CSS/JS)
↓
FastAPI (/chat, /history)
↓
LangGraph StateGraph
↓
SQLite Checkpointer (Module 5)

```

**No duplicate databases** — chat history is read directly from LangGraph’s persisted state.

---

## 📁 Project Structure

```

langgraph_persistent_agent/
│
├── app.py                 # FastAPI entrypoint
├── graph.py               # LangGraph definition
├── state.py               # Typed state
├── nodes/
│   └── agent_node.py      # LLM agent
│
├── templates/
│   └── index.html         # Chat UI
│
├── static/
│   ├── style.css          # ChatGPT-style UI
│   └── chat.js            # Frontend logic
│
├── storage/
│   └── memory.db          # SQLite persistence (gitignored)
│
├── requirements.txt
└── .gitignore

````

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repo
```bash
git clone https://github.com/82sanju/langgraph-persistent-agent.git
cd langgraph-persistent-agent
````

### 2️⃣ Create & activate virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Create `.env`

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## ▶️ Run the app

```bash
uvicorn app:api --reload
```

Open:

```
http://127.0.0.1:8000
```

---

## 🧪 How Persistence Works (Module 5)

* Each conversation is identified by a `thread_id`
* LangGraph stores state in SQLite via a checkpoint
* Restarting the server does **not** erase memory
* Chat history is retrieved using `get_state()`

Example:

```json
{
  "thread_id": "demo_1",
  "message": "My name is Sanju"
}
```

Restart server → ask again → memory is preserved.

---

## 🧠 Why LangGraph (not plain LangChain)?

* Explicit state transitions
* Durable, resumable workflows
* Production-ready persistence
* Designed for long-running agents

This project focuses on **correct architecture**, not demos.

---

## 🚀 Future Improvements

* Streaming responses
* Conversation sidebar
* User authentication
* HITL (Human-in-the-Loop) approval
* PostgreSQL backend
* React / Next.js frontend

---

## 📜 License

MIT License — free to use, modify, and extend.

---

## 👤 Author

**Sanju**
GitHub: [https://github.com/82sanju](https://github.com/82sanju)





