PRIORITY_PROMPT = """
You are an AI meeting assistant.

Determine the overall priority of the meeting action items.

Rules:
- High: contains urgent work, ASAP, today, tomorrow, before Friday, this week, critical deadlines.
- Medium: important but not immediately urgent.
- Low: informational or long-term tasks.

Return only one priority.

Meeting Transcript:
{transcript}

Action Items:
{action_items}
"""