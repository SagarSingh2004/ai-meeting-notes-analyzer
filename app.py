import streamlit as st
from graph import graph
from utils.file_reader import (
    read_txt,
    read_docx,
    read_pdf,
)

st.set_page_config(
    page_title="AI Meeting Notes Analyzer",
    page_icon="📝",
    layout="wide"
)

st.title("📝 AI Meeting Notes Analyzer")
st.write("Paste your meeting transcript below and click **Generate Meeting Notes**.")

uploaded_file = st.file_uploader(
    "Upload Meeting Transcript",
    type=["txt", "pdf", "docx"]
)

def generate_markdown(result):

    markdown = "# Meeting Report\n\n"

    markdown += "## Meeting Summary\n\n"
    markdown += result["summary"] + "\n\n"

    markdown += "## Key Topics\n"

    for topic in result["topics"]:
        markdown += f"- {topic}\n"

    markdown += "\n## Action Items\n"

    for item in result["action_items"]:
        markdown += (
            f"- {item['task']} "
            f"({item['owner']})\n"
        )

    markdown += (
        f"\n## Priority\n\n"
        f"{result['priority']}"
    )

    return markdown

transcript = ""

if uploaded_file:

    extension = uploaded_file.name.split(".")[-1]

    if extension == "txt":
        transcript = read_txt(uploaded_file)

    elif extension == "docx":
        transcript = read_docx(uploaded_file)

    elif extension == "pdf":
        transcript = read_pdf(uploaded_file)

    st.text_area(
        "Transcript Preview",
        transcript,
        height=300
    )

else:

    transcript = st.text_area(
        "Or paste transcript here",
        height=300
    )

generate = st.button("🚀 Generate Meeting Notes", use_container_width=True)

if generate:

    if not transcript.strip():
        st.warning("⚠️ Please enter a meeting transcript.")
        st.stop()

    with st.spinner("🤖 AI is analyzing the meeting transcript..."):

        state = {
            "transcript": transcript,
            "topics": [],
            "summary": "",
            "action_items": [],
            "priority": "",
            "report": {}
        }

        try:
            result = graph.invoke(state)

            # -----------------------------
            # Metrics
            # -----------------------------
            metric1, metric2, metric3 = st.columns(3)

            metric1.metric(
                label="Topics",
                value=len(result["topics"])
            )

            metric2.metric(
                label="Action Items",
                value=len(result["action_items"])
            )

            metric3.metric(
                label="Priority",
                value=result["priority"]
            )

            st.divider()

            # -----------------------------
            # Two Column Layout
            # -----------------------------
            col1, col2 = st.columns(2)

            # LEFT COLUMN
            with col1:

                with st.expander("📄 Meeting Summary", expanded=True):
                    st.write(result["summary"])

                with st.expander("📌 Key Topics", expanded=True):

                    for topic in result["topics"]:
                        st.markdown(f"- {topic}")

            # RIGHT COLUMN
            with col2:

                with st.expander("✅ Action Items", expanded=True):

                    if result["action_items"]:

                        for item in result["action_items"]:
                            st.markdown(
                                f"**Task:** {item['task']}  \n"
                                f"**Owner:** {item['owner']}"
                            )

                            st.divider()

                    else:
                        st.info("No action items identified.")

                with st.expander("🔥 Priority", expanded=True):

                    priority = result["priority"]

                    if priority.lower() == "high":
                        st.error("🔴 High Priority")

                    elif priority.lower() == "medium":
                        st.warning("🟡 Medium Priority")

                    else:
                        st.success("🟢 Low Priority")
                    
                
                markdown = generate_markdown(result)

                st.download_button(
                    label="📥 Download Markdown Report",
                    data=markdown,
                    file_name="meeting_report.md",
                    mime="text/markdown",
                )
                
        except Exception as e:
            st.error(f"An error occurred:\n\n{e}")
