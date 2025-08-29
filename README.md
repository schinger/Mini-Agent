# Mini-Agent which can use terminal do anything
- Based on [mini-swe-agent](https://github.com/SWE-agent/mini-swe-agent).
- Core logic less than 100 lines of Python code.
- Directly call (Google) LLM API, don't rely on LangChain or other frameworks.
- Install and Run:
```bash
git clone https://github.com/schinger/Mini-Agent
cd mini-swe-agent
pip install -e .
export MSWEA_MODEL_API_KEY="YOUR_GEMINI_API_KEY"
# cd to any directory you want, and run:
mini
```