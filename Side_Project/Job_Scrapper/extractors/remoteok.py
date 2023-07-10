from bs4 import BeautifulSoup
import requests
from emoji import core


def extract_remoteok_jobs(keyword):
    url = f"https://remoteok.com/remote-{keyword}-jobs"
    request = requests.get(url, headers={"User-Agent": "Kimchi"})

    if request.status_code == 200:
        results = []
        soup = BeautifulSoup(request.text, "html.parser")

        # write your ✨magical✨ code here
        jobs = soup.find_all("tr", class_='job')
        for job in jobs:
            companys = job.find_all("td", class_='company')
            job_sections = job.find_all("td", class_='company')
            for job_section in job_sections:
                link = f"https://remoteok.com{job_section.find(class_='preventLink')['href']}"
                position = job.find("h2", itemprop="title").string
                company = job.find("h3", itemprop="name").string
                location = "".join(
                    list(
                        map(lambda x: x.string,
                            job_section.find_all(
                                class_="location")[:-1]))).replace(
                                    ",", "").replace("\n", '')
                salary = job_section.find_all(class_="location")[-1].string
                job_info = {
                    "position": position.replace(",", "").replace("\n", ''),
                    "company": company.replace(",", "").replace("\n", ''),
                    "location": core.replace_emoji(location,
                                                   replace="").strip(),
                    "link": link,
                    "source": "remoteok"
                }  #"salary":salary,
                results.append(job_info)
                print(results[-1])
                print("-" * 50)
        return results
    else:
        print("Can't get jobs.")
