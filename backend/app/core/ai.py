from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from app.config import OPENAI_API_KEY
import logging

logger = logging.getLogger(__name__)

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.2,
    api_key=OPENAI_API_KEY,
)

def generate_ai_insights(metrics: dict) -> tuple[str, list[str]]:
    prompt = f"""
You are an SEO expert.

Analyze the following website SEO metrics and do the following:
1. Write a concise 2–3 paragraph summary of overall site quality.
2. Provide 3–5 actionable SEO improvement suggestions as bullet points.

Metrics:
{metrics}
"""

    try:
        response = llm.invoke([HumanMessage(content=prompt)])
        content = response.content

        suggestions = [
            line.strip("- ").strip()
            for line in content.split("\n")
            if line.strip().startswith("-")
        ]

        return content, suggestions

    except Exception as e:
        # Fail gracefully — do NOT crash the request
        return (
            "AI analysis could not be generated at this time.",
            ["Retry analysis later", "Verify OpenAI API configuration"],
        )
