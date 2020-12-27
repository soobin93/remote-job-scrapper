import requests
from bs4 import BeautifulSoup

SOURCE = "WWR"
URL = "https://weworkremotely.com"

def get_jobs(input):
    jobs = []

    url = f"{URL}/remote-jobs/search?term={input}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    job_list = soup.find("section", {"class": "jobs"})

    if job_list:
        job_sections = job_list.find_all("li")[0:-1]

        for job_section in job_sections:
            title = job_section.find("span", {"class": "title"}).get_text()
            company = job_section.find("span", {"class": "company"}).get_text()
            sub_link = job_section.find("a")["href"]
            link = f"{URL}{sub_link}"

            jobs.append({
                "title": title,
                "company": company,
                "link": link,
                "source": "WWR"
            })

    return jobs

