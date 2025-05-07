from openai import OpenAI
import requests
from bs4 import BeautifulSoup
import re
import sys

# Initialize the OpenAI client
client = OpenAI()
"""
def clean_query(query):
    return re.sub(r'(?<! )(?=[A-Z])', ' ', query).replace('_', ' ')

def find_research_article(query):
    query = clean_query(query)
    search_url = f"https://scholar.google.com/scholar?q={query}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(search_url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        first_result = soup.find("h3", class_="gs_rt")
        if first_result and first_result.a:
            return first_result.a["href"]
    return None
"""
def summarize_article(user_query):
    prompt_template = f"Summarize the most substantive research article found about {user_query} in two sentences to use in a clinical note. Include the citation."

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a research assistant that summarizes academic articles succinctly to use in clinical notes."},
            {"role": "user", "content": prompt_template}
        ]
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    user_query = input()
    #article_url = find_research_article(user_query)
    
    #if article_url:
    summary = summarize_article(user_query)
    print(summary)
    #else:
        #print("No relevant research article found.")
