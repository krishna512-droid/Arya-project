import streamlit as st
from agents.planner import PlannerAgent
from agents.web_agent import WebAgent
from agents.api_agent import APIAgent
from agents.analyst import AnalystAgent

st.set_page_config(
    page_title="PS-10 Multi-Agent Explorer",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 PS-10 — Multi-Agent Web & API Explorer")
st.caption("Autonomous multi-agent research using web pages + public APIs")

with st.sidebar:
    st.header("Agents")
    st.write("🧠 Planner Agent")
    st.write("🌐 Web Agent")
    st.write("🔌 API Agent")
    st.write("📊 Analyst Agent")
    st.divider()
    st.info("Demo uses public/read-only endpoints. No paid API key is required.")

goal = st.text_area(
    "Enter your exploration goal",
    value="Research Python and find popular GitHub repositories related to it.",
    height=100
)

if st.button("🚀 Run Multi-Agent Exploration", type="primary"):
    if not goal.strip():
        st.warning("Please enter a goal.")
        st.stop()

    planner = PlannerAgent()
    web_agent = WebAgent()
    api_agent = APIAgent()
    analyst = AnalystAgent()

    with st.status("Running autonomous agent workflow...", expanded=True) as status:
        st.write("🧠 Planner Agent is creating a plan...")
        plan = planner.plan(goal)
        st.json(plan)

        st.write("🌐 Web Agent is exploring web sources...")
        web_results = web_agent.run(plan)

        st.write("🔌 API Agent is exploring GitHub API...")
        api_results = api_agent.run(plan)

        st.write("📊 Analyst Agent is combining the evidence...")
        report = analyst.analyze(goal, plan, web_results, api_results)

        status.update(label="Exploration complete!", state="complete")

    st.header("📋 Final Report")
    st.markdown(report)

    with st.expander("View Planner Output"):
        st.json(plan)

    with st.expander("View Web Agent Results"):
        st.json(web_results)

    with st.expander("View API Agent Results"):
        st.json(api_results)
