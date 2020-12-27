import requests
from bs4 import BeautifulSoup

URL = "https://stackoverflow.com/jobs?r=true&sort=i"

def get_last_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    pagination_container = soup.find("div", {"class": "s-pagination"})

    if pagination_container:
        pages = pagination_container.find_all("a")
        last_page = pages[-2].get_text()
    else:
        last_page = 1

    return int(last_page)

def extract_job(html):
    title = html.find("h2").find("a", {"class": "s-link"})["title"]

    company = html.find("h3").find_all("span", recursive=False)[0]
    company = company.get_text()

    job_id = html['data-jobid']


    return {
        "title": title,
        "company": company,
        "link": f"https://stackoverflow.com/jobs/{job_id}",
        "source": "Stack Overflow"
    }

def extract_jobs(last_page, url):
    jobs = []

    for page in range(last_page):
        print(f"Scrapping stack overflow jobs in page {page}")

        response = requests.get(f"{url}&pg={page + 1}")
        soup = BeautifulSoup(response.text, "html.parser")
        job_sections = soup.find_all("div", {"class": "-job"})

        for job_section in job_sections:
            job = extract_job(job_section)
            jobs.append(job)

    return jobs

def get_jobs(input):
    url = f"{URL}&q={input}"
    last_page = get_last_page(url)
    jobs = extract_jobs(last_page, url)
    return jobs

