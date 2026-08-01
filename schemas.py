from pydantic import BaseModel
from typing import Literal

class TopicOutput(BaseModel):
    topics : list[str]

class SummaryOutput(BaseModel):
    summary: str

class ActionItem(BaseModel):
    task: str
    owner: str

class ActionOutput(BaseModel):
    action_items: list[ActionItem]

class PriorityOutput(BaseModel):
    priority: Literal["High", "Medium", "Low"]