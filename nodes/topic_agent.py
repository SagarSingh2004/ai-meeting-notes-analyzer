from models import llm
from prompts.topic_prompt import TOPIC_PROMPT
from state import MeetingState
from schemas import TopicOutput

def topic_agent(State):
    prompt = TOPIC_PROMPT.format(transcript=State['transcript'])
    structured_llm = llm.with_structured_output(TopicOutput)
    response = structured_llm.invoke(prompt)
    return {
        'topics': response.topics
    }