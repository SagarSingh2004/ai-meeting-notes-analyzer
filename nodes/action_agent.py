from models import llm
from state import MeetingState
from schemas import ActionOutput
from prompts.action_prompt import ACTION_PROMPT

structured_llm = llm.with_structured_output(ActionOutput)

def action_agent(state: MeetingState):

    prompt = ACTION_PROMPT.format(
        transcript=state["transcript"]
    )

    response = structured_llm.invoke(prompt)

    return {
        "action_items": [
            item.model_dump()
            for item in response.action_items
        ]
    }