import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)
def analyze_post(post_text):

    prompt = f"""
You are a professional LinkedIn Content Strategist.

Analyze the following LinkedIn post.

POST:
{post_text}

Tasks:

1. Identify the main topic.
2. Detect engagement hooks.
3. Identify writing style.
4. Explain why the post may perform well.
5. Create 3 improved versions:
   - Version 1: More engaging
   - Version 2: Storytelling style
   - Version 3: Viral LinkedIn style

Return ONLY JSON.

{{
  "topic":"",
  "engagement_hooks":[],
  "writing_style":"",
  "performance_reason":"",
  "improved_versions":[
      "",
      "",
      ""
  ]
}}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text