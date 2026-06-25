# =============================================================================
# Legal Document Simplifier Graph -- A LangGraph Assignment
# =============================================================================
import sys
import os
import operator
import json
from typing import Annotated, List, Dict
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END

sys.stdout.reconfigure(encoding="utf-8")
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key or api_key.startswith("sk-your"):
    logger.error("Open API Key is not set! Copy Check .env and add your key.")
    sys.exit(1)

# Define the state
class LegalDocState(BaseModel):
    text: str = ""
    clauses_plain: List[str] = []
    obligations: Dict[str, List[str]] = {}
    risky_terms: List[str] = []
    risk_level: str = ""
    summary: str = ""
    messages: Annotated[list, operator.add] = []

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.6)

# Specialist Node 1 - Explain clauses
def explain_clauses_plain_english(state: LegalDocState) -> dict:
    response = llm.invoke(
        f"Translate the following legal text into plain English clauses:\n\n{state.text}\n\n"
        f"Keep each clause short and clear."
    )
    return {
        "clauses_plain": response.content.split("\n"),
        "messages": [f"[explain_clauses_plain_english] Done"]
    }

# Specialist Node 2 - Identify obligations
def identify_obligations(state: LegalDocState) -> dict:
    response = llm.invoke(
        f"From this legal text:\n\n{state.text}\n\n"
        f"List the obligations of each party clearly."
    )
    try:
        obligations = json.loads(response.content)
    except json.JSONDecodeError:
        obligations = {"Unknown": ["Could not parse obligations"]}
    return {
        "obligations": obligations,
        "messages": [f"[identify_obligations] Done"]
    }

# Specialist Node 3 - Flag risky terms
def flag_risky_terms(state: LegalDocState) -> dict:
    response = llm.invoke(
        f"From this legal text:\n\n{state.text}\n\n"
        f"Identify any risky, unusual, or unclear terms. "
        f"Return them as a simple list."
    )
    return {
        "risky_terms": response.content.split("\n"),
        "messages": [f"[flag_risky_terms] Done"]
    }

# Decision Node
def assess_risk(state: LegalDocState) -> dict:
    risk_level = "High" if state.risky_terms and any(t.strip() for t in state.risky_terms) else "Low"
    return {
        "risk_level": risk_level,
        "messages": [f"[assess_risk] risk={risk_level}"]
    }

# Final Node - Plain summary
def plain_summary_response(state: LegalDocState) -> dict:
    response = llm.invoke(
        f"Summarize this legal text in plain English:\n\n{state.text}\n\n"
        f"Keep it concise and clear."
    )
    return {
        "summary": f"PLAIN SUMMARY\n{'='*45}\n{response.content}",
        "messages": [f"[plain_summary_response] Generated summary"]
    }

# Final Node - Risk review
def risk_review_response(state: LegalDocState) -> dict:
    response = llm.invoke(
        f"Summarize this legal text in plain English:\n\n{state.text}\n\n"
        f"Highlight the risky terms:\n{state.risky_terms}\n\n"
        f"Explain why they may need careful review."
    )
    return {
        "summary": f"RISK REVIEW SUMMARY\n{'='*45}\n{response.content}",
        "messages": [f"[risk_review_response] Generated risk review"]
    }

# Routing function
def route_after_decision(state: LegalDocState) -> str:
    return "risk" if state.risk_level == "High" else "plain"

# Build the graph
graph = StateGraph(LegalDocState)

graph.add_node("explain_clauses_plain_english", explain_clauses_plain_english)
graph.add_node("identify_obligations", identify_obligations)
graph.add_node("flag_risky_terms", flag_risky_terms)
graph.add_node("assess_risk", assess_risk)
graph.add_node("plain_summary_response", plain_summary_response)
graph.add_node("risk_review_response", risk_review_response)

graph.add_edge(START, "explain_clauses_plain_english")
graph.add_edge("explain_clauses_plain_english", "identify_obligations")
graph.add_edge("identify_obligations", "flag_risky_terms")
graph.add_edge("flag_risky_terms", "assess_risk")

graph.add_conditional_edges(
    "assess_risk",
    route_after_decision,
    {
        "plain": "plain_summary_response",
        "risk": "risk_review_response",
    }
)

graph.add_edge("plain_summary_response", END)
graph.add_edge("risk_review_response", END)

app = graph.compile()

# Runner
def run_legal_doc_check(text: str):
    print("=" * 55)
    print("  LEGAL DOCUMENT SIMPLIFIER")
    print(f"  Input text: \"{text[:60]}...\"")
    print("=" * 55)

    result = app.invoke({
        "text": text,
        "messages": [],
    })

    print("\n" + "=" * 55)
    print("  SIMPLIFIED SUMMARY")
    print("=" * 55)
    print(f"\n{result['summary']}")

    print("\n" + "-" * 55)
    print("  MESSAGE LOG")
    print("-" * 55)
    for msg in result["messages"]:
        print(f"  {msg}")

    return result

if __name__ == "__main__":
    print("\n" + "=" * 55)
    print("  LEGAL DOCUMENT SIMPLIFIER")
    print("=" * 55)
    print("\n  Paste your legal or contract text below.")
    print("  Type 'quit' to exit.\n")

    while True:
        text = input("  Paste legal text or type Exit to STOP").strip()

        if text.lower() in ("quit", "exit", "q"):
            print("\n  Goodbye! Stay legally safe.\n")
            break

        if not text:
            continue

        run_legal_doc_check(text)
        print("\n")
