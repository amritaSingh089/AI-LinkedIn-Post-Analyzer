from scraper import scrape_linkedin_post
from gemini_helper import analyze_post

url = input("Enter LinkedIn Post URL: ")

print("\nScraping LinkedIn post...")

post_text = scrape_linkedin_post(url)

print("\nAnalyzing with Gemini...")

result = analyze_post(post_text)

print("\nAnalysis Result:\n")

print(result)

with open("output.json", "w", encoding="utf-8") as file:
    file.write(result)

print("\nOutput saved successfully.")