from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from state import AgentState

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

def agent_node(state: AgentState) -> AgentState:
    response = llm.invoke(state["messages"])
    return {
        "messages": state["messages"] + [response]
    }
