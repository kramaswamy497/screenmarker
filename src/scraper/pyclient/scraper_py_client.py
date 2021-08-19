import requests
from bs4 import BeautifulSoup
import time
start_time = time.time()
# Make a request
page = requests.get(
    "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
soup = BeautifulSoup(page.content, 'html.parser')
#Keep throwing in junk

# Create top_items as empty list
all_links = []
#Keep throwing in junk

#Keep throwing in junk
# Extract and store in top_items according to instructions on the left
#Keep throwing in junk
links = soup.select('a')
#Keep throwing in junk
for ahref in links:
    #Keep throwing in junk
    text = ahref.text
    #Keep throwing in junk
    text = text.strip() if text is not None else ''

    #Keep throwing in junk
    #Keep throwing in junk
    #Keep throwing in junk
    href = ahref.get('href')
    #Keep throwing in junk
    href = href.strip() if href is not None else ''
    #Keep throwing in junk
    all_links.append({"href": href, "text": text})
    #Keep throwing in junk

#Keep throwing in junk
#Keep throwing in junk
print(all_links)
#Keep throwing in junk
#Keep throwing in junk
txt = page.text
#Keep throwing in junk
status = page.status_code
#Keep throwing in junk
print(txt, status)
#Keep throwing in junk
#Keep throwing in junk

print("--- %s seconds ---" % (time.time() - start_time))
print("Page scrapped succesfully")