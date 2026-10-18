from langgraph.graph import StateGraph , START,END
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.checkpoint.memory import InMemorySaver
from langchain_core.messages import BaseMessage
from langgraph.graph.message import Annotated, add_messages
from typing import TypedDict
from dotenv import load_dotenv

load_dotenv()

llm=ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
) 

class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage],add_messages]

def chat_node(state:ChatState):
    message=state['messages']
    response=llm.invoke(message)
    return {"messages":[response]}

graph=StateGraph(ChatState)
graph.add_node("chat_node",chat_node)

graph.add_edge(START,"chat_node")
graph.add_edge("chat_node",END)

checkpointer=InMemorySaver()

chatbot=graph.compile(checkpointer=checkpointer)