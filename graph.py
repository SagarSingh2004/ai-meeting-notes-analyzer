from langgraph.graph import StateGraph, END, START
from nodes.topic_agent import topic_agent
from nodes.summary_agent import summary_agent
from nodes.action_agent import action_agent
from state import MeetingState
from nodes.priority_agent import priority_agent
from nodes.output_node import output_node

def should_run_priority(state: MeetingState):

    if not state["action_items"]:
        return "skip"

    return "priority"

builder = StateGraph(MeetingState)

builder.add_node('topic_agent', topic_agent)
builder.add_node('summary_agent', summary_agent)
builder.add_node('action_agent', action_agent)
builder.add_node('priority_agent', priority_agent)
builder.add_node('output_node', output_node)

builder.add_edge(START, 'topic_agent')
builder.add_edge('topic_agent', 'summary_agent')
builder.add_edge("summary_agent", "action_agent")
builder.add_conditional_edges(
    "action_agent",
    should_run_priority,
    {
        "priority": "priority_agent",
        "skip": "output_node"
    }
)
builder.add_edge("priority_agent", "output_node")
builder.add_edge("output_node", END)

graph = builder.compile()
