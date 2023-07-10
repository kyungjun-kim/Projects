from bs4 import BeautifulSoup
import requests
from requests import get


def get_indeed_page_count(keyword):
    base_url = "https://kr.indeed.com/jobs?q="
    response = get(f"{base_url}{keyword}")
    if response.status_code != 200:
        print("Can't request page")
    else:
        soup = BeautifulSoup(response.text, "html.parser")
        pagination = soup.find("ul", class_="pagination-list")
        # indeed 기준
        if pagination == None:
            return 1
        pages = pagination.find_all("li", recursive=False)
        cnt = len(pages)
        if cnt >= 5:
            return 5
        else:
            return cnt
