from models import llm
from state import MeetingState
from schemas import PriorityOutput
from prompts.priority_prompt import PRIORITY_PROMPT

structured_llm = llm.with_structured_output(PriorityOutput)


def priority_agent(state: MeetingState):

    prompt = PRIORITY_PROMPT.format(
        transcript=state["transcript"],
        action_items=state["action_items"]
    )

    response = structured_llm.invoke(prompt)

    return {
        "priority": response.priority
    }