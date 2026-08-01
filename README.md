# 📝 AI Meeting Notes Analyzer using LangGraph

An AI-powered Meeting Notes Analyzer that converts unstructured meeting transcripts into structured meeting reports using a **multi-agent workflow** built with **LangGraph**, **LangChain**, **Google Gemini**, and **Streamlit**.

The application automatically extracts discussion topics, generates concise meeting summaries, identifies action items with task owners, classifies meeting priority, and produces downloadable reports.

---

## 🌐 Live Demo

👉 **[Try it on Streamlit Cloud](https://ai-meeting-notes-analyzer-5yp3hpha3hv5frcyzojrvv.streamlit.app/)**

---

## 🚀 Features

- 🤖 Multi-Agent AI workflow using LangGraph
- 📝 Automatic meeting summary generation
- 📌 Key discussion topic extraction
- ✅ Action item identification
- 👤 Task owner extraction
- 🔥 Meeting priority classification
- 🔀 Conditional workflow execution
- 📂 Upload meeting transcripts
  - TXT
  - PDF
  - DOCX
- ✍️ Manual transcript input
- 📄 Download meeting report as Markdown
- 📑 Download meeting report as PDF
- 🎨 Interactive Streamlit UI
- ✅ Structured outputs using Pydantic

---

# 🏗️ System Architecture

```
                 User
                   │
                   ▼
          Streamlit Interface
                   │
                   ▼
         Meeting Transcript Input
                   │
                   ▼
            LangGraph Workflow
                   │
        ┌──────────┴──────────┐
        │                     │
        ▼                     ▼
 Topic Extraction Agent
        │
        ▼
 Meeting Summary Agent
        │
        ▼
 Action Item Agent
        │
        ▼
 Conditional Routing
        │
   ┌────┴────┐
   │         │
   ▼         ▼
Priority    Output Node
 Agent         │
   │           ▼
   └────────► Final Report
                   │
                   ▼
       Streamlit Output + Download
```

---

# 🧠 AI Agents

The project follows an **Agentic AI** architecture where every agent performs a single responsibility.

### 1️⃣ Topic Extraction Agent

Extracts the major discussion topics from the meeting transcript.

---

### 2️⃣ Meeting Summary Agent

Generates a concise summary of the entire meeting.

---

### 3️⃣ Action Item Extraction Agent

Extracts:

- Task Description
- Task Owner

If the owner is unavailable, it returns:

```
Owner: Not Specified
```

---

### 4️⃣ Priority Classification Agent

Determines the overall meeting priority.

Possible outputs:

- High Priority
- Medium Priority
- Low Priority

The agent detects urgency using phrases like:

- ASAP
- Urgent
- Today
- Tomorrow
- Before Friday
- This Week

---

### 5️⃣ Output Node

Combines all generated information into a structured meeting report.

---

# 📁 Project Structure

```
meeting_notes_analyzer/
│
├── app.py
├── main.py
├── graph.py
├── state.py
├── prompts.py
├── schemas.py
├── requirements.txt
│
├── nodes/
│   ├── topic_agent.py
│   ├── summary_agent.py
│   ├── action_agent.py
│   ├── priority_agent.py
│   └── output_node.py
│
├── utils/
│   ├── file_reader.py
│   ├── markdown_generator.py
│   └── pdf_generator.py
│
└── README.md
```

---

# ⚙️ Tech Stack

| Category | Technology |
|-----------|------------|
| Language | Python |
| Workflow | LangGraph |
| LLM Framework | LangChain |
| LLM | Google Gemini 2.5 Flash |
| Structured Output | Pydantic |
| UI | Streamlit |
| PDF Processing | PyPDF2 |
| DOCX Processing | python-docx |
| Version Control | Git & GitHub |

---

# 🔄 Workflow

```
START
   │
   ▼
Transcript Input
   │
   ▼
Topic Extraction
   │
   ▼
Meeting Summary
   │
   ▼
Action Item Extraction
   │
   ▼
Conditional Routing
   │
 ┌─┴──────────────┐
 │                │
 ▼                ▼
Priority      Output Node
Agent
 │
 ▼
END
```

---

# 📊 Example Input

```
John: We need to improve website performance.

Sarah: The homepage is loading slowly.

David: I'll optimize the database queries this week.

Emily: I'll redesign the homepage before Friday.

Michael: I'll improve API test coverage.

John: Let's finish everything before the beta release.
```

---

# 📋 Example Output

## Meeting Summary

The team discussed improving website performance before the beta release. Responsibilities were assigned for backend optimization, UI redesign, and testing.

---

## Key Topics

- Website Performance
- Database Optimization
- Homepage Redesign
- API Testing

---

## Action Items

- Optimize database queries — David
- Redesign homepage — Emily
- Increase API test coverage — Michael

---

## Priority

**High Priority**

---

# 💡 Why LangGraph?

Instead of using one large prompt, this project divides the problem into multiple specialized AI agents.

Advantages include:

- Better modularity
- Easier debugging
- Improved scalability
- Cleaner prompts
- Shared state management
- Conditional execution
- Better maintainability

---

# 📥 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/meeting_notes_analyzer.git

cd meeting_notes_analyzer
```

Create a virtual environment:

```bash
python -m venv myenv
```

Activate it:

### Windows

```bash
myenv\Scripts\activate
```

### Linux / macOS

```bash
source myenv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

```
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

Or skip local setup entirely and use the hosted version: **[Live Demo](https://ai-meeting-notes-analyzer-5yp3hpha3hv5frcyzojrvv.streamlit.app/)**

---

# 📌 Future Improvements

- 🎙️ Speech-to-Text Integration
- 🌍 Multilingual Support
- 📅 Google Calendar Integration
- 📧 Automatic Email Generation
- 📊 Speaker Analytics
- 😊 Sentiment Analysis
- 📌 Decision Extraction Agent
- 🔐 User Authentication
- 📈 Meeting Analytics Dashboard

---

# 📚 Learning Outcomes

This project demonstrates practical experience with:

- Agentic AI
- LangGraph
- LangChain
- Prompt Engineering
- Google Gemini
- State Management
- Structured Outputs
- Pydantic
- Streamlit
- Multi-Agent Systems

---

# 🤝 Contributing

Contributions, feature requests, and improvements are welcome.

Feel free to fork the repository and submit a pull request.

---

# 📄 License

This project is intended for educational and portfolio purposes.

---

# 👨‍💻 Author

**Sagar Singh**

AI/ML | Generative AI | LangGraph | LangChain | Python

---

⭐ If you found this project helpful, consider giving it a star!
