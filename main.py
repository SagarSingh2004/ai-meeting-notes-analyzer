from graph import graph

state = {
    "transcript": """
Project Kickoff Meeting – AI Product Development

John (Project Manager): Good morning, everyone. Thanks for joining. Today we need to review the current progress of our AI-powered customer support platform and decide what needs to be completed before the beta release.

Sarah (Frontend Developer): From the UI side, we've completed around 80% of the dashboard. However, users have reported that the dashboard takes almost six seconds to load, which is much slower than expected.

David (Backend Developer): I checked the logs yesterday. Most of the delay is caused by inefficient database queries and repeated API calls. I will optimize the database queries this week and also introduce caching for frequently requested data.

Emily (UI/UX Designer): While reviewing the feedback, I noticed that many users found the navigation menu confusing. I will redesign the dashboard navigation and update the homepage layout before Friday.

Michael (QA Engineer): During testing, I found several bugs in the login module. Some users are unable to reset their passwords. This issue should be fixed ASAP because it directly affects user access.

John: Agreed. The login issue is critical. David, can you also investigate the authentication service after optimizing the database?

David: Sure. I'll review the authentication service and resolve the password reset issue by tomorrow evening.

Sarah: I'll also improve the responsiveness of the dashboard so it works properly on tablets and smaller laptop screens.

Emily: Another suggestion from users was to improve accessibility. The text contrast is too low, and some buttons are difficult to identify. I can work on accessibility improvements next week after finishing the dashboard redesign.

Michael: I also recommend increasing automated test coverage. Currently, our API test coverage is only about 55%, which isn't sufficient for a production release.

John: That's a good point. We should aim for at least 85% API test coverage before the beta release.

David: I'll help Michael with the backend test cases once the authentication fixes are complete.

Sarah: We also need to optimize image loading because large banner images are slowing down the homepage.

John: Yes, that's important, but it isn't as urgent as the authentication issue.

Emily: Marketing has requested a new landing page for the product launch next month. We don't need to complete it this week, but we should start planning the design.

Michael: I found another issue. Error messages are inconsistent across different pages. Some pages show technical exceptions while others display user-friendly messages.

John: We definitely need consistent error handling. Can someone take ownership?

Sarah: I'll handle the frontend error messages.

David: I'll standardize the backend API error responses.

John: Excellent.

Emily: Should we also update the documentation for the new dashboard?

John: Yes, but that can wait until after the beta release.

Michael: One more thing. We should improve logging because debugging production issues is currently difficult.

John: Good point. Let's create a logging improvement task, but we don't need to assign an owner right now.

Sarah: We also discussed adding dark mode during the last meeting.

John: Let's postpone dark mode until the next development sprint.

David: Our cloud infrastructure costs have increased by nearly 20% over the last month. We should analyze resource utilization.

John: That's important but not urgent. We'll review it in next month's infrastructure meeting.

Emily: Are there any blockers remaining?

David: Apart from the authentication issue, everything else is progressing well.

Michael: If we complete the critical fixes before Friday, I believe we're ready for beta testing.

John: Great. Here's the summary:
- Authentication bugs must be fixed by tomorrow.
- Dashboard redesign should be completed before Friday.
- Database optimization and caching should be finished this week.
- Responsive design improvements should begin immediately.
- API test coverage should reach at least 85%.
- Accessibility improvements can begin next week.
- Landing page planning can start next month.
- Logging improvements should be added to the backlog without assigning an owner.
Thanks, everyone. Let's meet again next Monday to review progress.
"""
}

result = graph.invoke(state)

report = result["report"]

print("\nMeeting Summary")
print(report["Meeting Summary"])

print("\nKey Topics")
for topic in report["Key Topics"]:
    print("-", topic)

print("\nAction Items")
for item in report["Action Items"]:
    print(f"- {item['task']} ({item['owner']})")

print("\nPriority")
print(report["Priority"])