from bs4 import BeautifulSoup
import requests

url = "https://pypi.org/project/RandomPi/"
response = requests.get(url)

if response.status_code == 200:
    headers = {"Accept": "application/vnd.pypi.simple.v1+html"}
    html_text = response.text
    soup = BeautifulSoup(html_text, features="html.parser")
    
    name_tag = soup.find("h1", class_="package-header__name")
    name = name_tag.text.strip() if name_tag else "Name not found"
    
    date_tag = soup.find("p", class_="package-header__date")
    date = date_tag.text.strip() if date_tag else "Date not found"
    
    des_tag = soup.find("p", class_="package-description__summary")
    des = des_tag.text.strip() if des_tag else "Description not found"
    
    print(f"Name:\n  {name}\nRelease Date:\n  {date}\nDescription:\n  {des}\n")
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")
