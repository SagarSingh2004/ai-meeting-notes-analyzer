from models import llm
from state import MeetingState
from schemas import SummaryOutput
from prompts.summary_prompt import SUMMARY_PROMPT


def summary_agent(state: MeetingState):

    structured_llm = llm.with_structured_output(SummaryOutput)

    prompt = SUMMARY_PROMPT.format(
        transcript=state["transcript"]
    )

    response = structured_llm.invoke(prompt)

    return {
        "summary": response.summary
    }