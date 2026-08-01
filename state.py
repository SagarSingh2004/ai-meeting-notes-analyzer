"""
state.py
---
Defines the shared state object that flows through every node in the LangGraph workflow.
Every agent reads from and and writes to the state
"""

from typing import TypedDict
from schemas import ActionItem

class MeetingState(TypedDict):
    transcript : str
    topics : list[str]
    summary : str
    action_items : list[ActionItem]
    priority : str
    report : dict