# PS-10: Multi-Agent Autonomous Web & API Environment Explorer

A hackathon-ready reference implementation for:

**PS-10: Multi-Agent Autonomous Web & API Environment Explorer**

## What it does

The application accepts a research goal and uses multiple specialized agents:

1. **Planner Agent** — breaks the goal into tasks.
2. **Web Agent** — retrieves information from Wikipedia and public web pages.
3. **API Agent** — queries the public GitHub API.
4. **Analyst Agent** — combines the collected evidence into a concise report.

The UI is built with Streamlit.

## Architecture

```text
User Goal
   |
   v
Planner Agent
   |
   +------------------+
   |                  |
   v                  v
Web Agent          API Agent
   |                  |
   +--------+---------+
            |
            v
       Analyst Agent
            |
            v
       Final Report
```

## Requirements

- Python 3.10+
- Internet connection
- No paid API key is required for the included demo.
- The public GitHub API has rate limits.

## Run on Windows

```powershell
cd PS10_MultiAgent_Web_API_Explorer

python -m venv .venv
.venv\Scripts\activate

pip install -r requirements.txt

streamlit run app.py
```

Then open the local URL shown by Streamlit.

## Run on Linux/macOS

```bash
cd PS10_MultiAgent_Web_API_Explorer

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

streamlit run app.py
```

## Example tasks

Try:

- `Research Python and find popular GitHub repositories`
- `Explore LangGraph and compare it with AutoGen`
- `Research FastAPI and identify popular related repositories`
- `Explore computer vision and find useful GitHub projects`

## Project structure

```text
PS10_MultiAgent_Web_API_Explorer/
├── app.py
├── agents/
│   ├── planner.py
│   ├── web_agent.py
│   ├── api_agent.py
│   └── analyst.py
├── utils/
│   └── http_client.py
├── requirements.txt
├── .env.example
└── README.md
```

## Important hackathon note

This is a working **reference implementation**, not a claim that an autonomous agent should be allowed unrestricted access to arbitrary websites or APIs. For a hackathon demo, keep tool access limited to trusted/read-only endpoints.

## How it maps to PS-10

- **Multi-Agent:** four specialized agents.
- **Autonomous:** planner creates tasks from the user's goal and agents execute them.
- **Web:** Wikipedia/web-page retrieval.
- **API:** GitHub REST API.
- **Environment exploration:** the system gathers, combines, and reasons over information from different sources.
