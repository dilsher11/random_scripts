import requests
from bs4 import BeautifulSoup as bs

query = "hello"
query_url = "https://www.duckduckgo.com/search?q=" + query

response = requests.get(query_url)
print(f"URL: {response.url}")
print(f"Response code: {response.status_code}")

returned_html = response.text
soup = bs(returned_html, "lxml")

#access html tags
print(soup.title)
print(soup.head)

#access properties of a tag e.g. id, class, rel etc
anchors = soup.a["class"]
print(anchors)

print(soup.find_all("p"))