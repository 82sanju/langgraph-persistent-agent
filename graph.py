# from langgraph.graph import StateGraph, END
# # from langgraph.checkpoint.sqlite import SQLiteSaver
# from langgraph.checkpoint.sqlite import SqliteSaver


# from state import AgentState
# from nodes.agent_node import agent_node

# # checkpointer = SQLiteSaver.from_conn_string(
# #     "storage/memory.db"
# # )

# checkpointer = SqliteSaver.from_conn_string(
#     "storage/memory.db"
# )


# graph = StateGraph(AgentState)

# graph.add_node("agent", agent_node)
# graph.set_entry_point("agent")
# graph.add_edge("agent", END)

# app = graph.compile(checkpointer=checkpointer)



from langgraph.graph import StateGraph, END
from langgraph.checkpoint.sqlite import SqliteSaver
from state import AgentState
from nodes.agent_node import agent_node

# IMPORTANT: enter the context manager
checkpointer_cm = SqliteSaver.from_conn_string("storage/memory.db")
checkpointer = checkpointer_cm.__enter__()

graph = StateGraph(AgentState)

graph.add_node("agent", agent_node)
graph.set_entry_point("agent")
graph.add_edge("agent", END)

app = graph.compile(checkpointer=checkpointer)
