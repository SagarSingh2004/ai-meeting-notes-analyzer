from state import MeetingState

def output_node(state: MeetingState):

    report = {
        "Meeting Summary": state["summary"],
        "Key Topics": state["topics"],
        "Action Items": state["action_items"],
        "Priority": state["priority"] if state["action_items"] else "No action items identified in this meeting."
    }

    return {
        "report": report
    }