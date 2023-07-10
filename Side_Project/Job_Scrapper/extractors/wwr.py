from requests import get
from bs4 import BeautifulSoup
from emoji import core


def extract_wwr_jobs(keyword):
    base_url = 'https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term='
    response = get(f'{base_url}{keyword}')
    if response.status_code != 200:
        print("Can't request website")
    else:
        soup = BeautifulSoup(response.text, "html.parser")
        jobs = soup.find_all('section', class_="jobs")
        results = []
        for job_sections in jobs:
            job_posts = job_sections.find_all('li')
            job_posts.pop(-1)
            for post in job_posts:
                anchor = post.find_all("a")
                anchor = anchor[1]
                link = anchor['href']
                company, kind, location = anchor.find_all('span',
                                                          class_='company')
                title = anchor.find('span', class_='title')
                job_date = {
                    'position':
                    title.string.replace(",", " "),
                    'company':
                    company.string.replace(",", " "),
                    'location':
                    core.replace_emoji(location.string.replace(",", " "),
                                       replace="").strip(),
                    'link':
                    f'https://weworkremotely.com{link}',
                    'source':
                    "weworkremotely"
                }
                results.append(job_date)
        return results
