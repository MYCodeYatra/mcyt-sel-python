import os
import requests
from bs4 import BeautifulSoup
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
def generate_selenium_test(url, test_description):
    # 1. Fetch the raw HTML of the target page
    response = requests.get(url)
    html_content = response.text
    # 2. Clean the HTML (Remove heavy scripts/styles to save AI Tokens)
    soup = BeautifulSoup(html_content, 'html.parser')
    for script in soup(["script", "style"]):
        script.extract()
    clean_html = soup.body.prettify()[:5000] # Pass the first 5000 chars of the body
    # 3. Configure the LLM
    # Make sure OPENAI_API_KEY is set in your environment variables
    llm = ChatOpenAI(model_name="gpt-4", temperature=0.2)
    # 4. Define the AI Prompt Template
    prompt = PromptTemplate(
        input_variables=["html", "description"],
        template="""
        You are an expert SDET. I will provide you with the HTML of a webpage and a description of a test.
        Write a complete, functional Pytest Selenium script to perform this test.
        Rules:
        - Use standard Pytest fixtures (e.g., passing `driver`).
        - Use explicit waits (WebDriverWait).
        - Base your locators ONLY on the provided HTML.
        - Output ONLY valid Python code. Do not include markdown formatting or explanations.
        Test Description: {description}
        HTML Source:
        {html}
        """
    )
    # 5. Execute the AI Chain!
    print(f"[AI] Generating test for {url}...")
    formatted_prompt = prompt.format(html=clean_html, description=test_description)
    result = llm.invoke(formatted_prompt)
    # 6. Save the generated code to a file
    output_file = "tests/generated_test.py"
    with open(output_file, "w") as f:
        f.write(result.content)
    print(f"[AI] Test generated successfully: {output_file}")
# Example Usage:
generate_selenium_test(
    url="https://mycodeyatra.com/login",
    test_description="Verify that entering invalid credentials displays an error message."
)