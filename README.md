# Legal Document Simplifier Graph

This project implements a **LangGraph workflow** that ingests legal or contractual text and produces a structured plain‑English interpretation.  
The system decomposes the input into specialist tasks, evaluates risk, and routes execution to the appropriate summary node.

---

## Architecture

The workflow is modeled as a directed graph with the following nodes:

- **Explain Clauses (specialist)**  
  Translates complex legal clauses into simple, human‑readable language.

- **Identify Obligations (specialist)**  
  Extracts duties and responsibilities of each party.

- **Flag Risky Terms (specialist)**  
  Detects unusual, unclear, or potentially harmful clauses.

- **Assess Risk (decision)**  
  Determines whether the document is *Low Risk* or requires *Careful Review*.

- **Plain Summary Response (terminal)**  
  Produces a concise summary when no significant risks are found.

- **Risk Review Response (terminal)**  
  Generates a summary highlighting flagged risks and advising caution.

The graph routes execution linearly through the specialist nodes, then conditionally to one of the two terminal nodes.

---

## Technical Stack

- **Python 3.9+**
- **LangGraph** for workflow orchestration
- **LangChain OpenAI** for LLM integration
- **Pydantic** for state modeling (advanced version)
- **dotenv** for environment variable management

---

## Installation

```bash
git clone <your-repo-url>
cd legal-doc-simplifier
pip install -r requirements.txt
