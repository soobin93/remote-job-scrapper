import requests
from bs4 import BeautifulSoup

SOURCE = "Remoteok"
URL = "https://remoteok.io/"
HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

def get_jobs(input):
    jobs = []

    url = f"{URL}remote-{input}-jobs"
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")

    jobs_board = soup.find("table", {"id": "jobsboard"})

    if jobs_board:
        job_sections = jobs_board.find_all("tr", {"class": "job"})

        for job_section in job_sections:
            job_details = job_section.find("td", {"class": "company_and_position"})

            title = job_details.find("h2", {"itemprop": "title"}).get_text()
            company = job_section.find("a", {"class": "companyLink"}).get_text()
            sub_link = job_section.find("a", {"class": "preventLink"})["href"]
            link = f"{URL}{sub_link}"

            jobs.append({
                "title": title,
                "company": company,
                "link": link,
                "source": "Remoteok"
            })

    return jobs

