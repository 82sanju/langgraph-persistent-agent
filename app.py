from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from langchain_core.messages import HumanMessage
from graph import app as langgraph_app

api = FastAPI(title="LangGraph Persistent Agent")

api.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


class ChatRequest(BaseModel):
    thread_id: str
    message: str


@api.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@api.post("/chat")
def chat(req: ChatRequest):
    result = langgraph_app.invoke(
        {"messages": [HumanMessage(content=req.message)]},
        config={"thread_id": req.thread_id}
    )

    return {
        "response": result["messages"][-1].content
    }

@api.get("/history/{thread_id}")
def history(thread_id: str):
    state = langgraph_app.get_state(
    config={
        "configurable": {
            "thread_id": thread_id
        }
    }
)


    messages = []
    for m in state.values["messages"]:
        messages.append({
            "type": m.type,
            "content": m.content
        })

    return {"history": messages}
