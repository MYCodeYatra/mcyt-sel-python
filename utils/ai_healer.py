import os
from openai import OpenAI
# Initialize the OpenAI Client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
def heal_locator(broken_locator, page_source):
    """
    Sends the broken locator and the DOM to GPT-4 to calculate a new valid CSS Selector.
    """
    # We only send a subset of the HTML to save tokens
    clean_html = page_source[:6000] 
    prompt = f"""
    You are an AI Self-Healing engine for a Selenium test framework.
    The original locator used was: '{broken_locator}'.
    It has failed because the developer changed the HTML structure.
    Look at the current HTML Source provided below. Based on semantic meaning 
    (button text, nearby labels, standard naming conventions), determine the 
    NEW valid CSS Selector to find this element.
    Output ONLY the raw CSS Selector string. Do NOT include markdown or explanations.
    HTML Source:
    {clean_html}
    """
    print(f"\n[AI-Healer] Analyzing DOM to fix broken locator: {broken_locator}")
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1 # Keep it deterministic
    )
    new_locator = response.choices[0].message.content.strip()
    print(f"[AI-Healer] Successfully calculated new locator: {new_locator}")
    return new_locator