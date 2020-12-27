from flask import Flask, render_template, request, redirect, send_file
from scrapper import get_jobs
from exporter import save_to_file

"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""

app = Flask("JobScrapper")

db = {}

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/search")
def search():
    input = request.args.get("input")
    if input:
        input = input.lower()
        existing_jobs = db.get(input)
        if existing_jobs:
            jobs = existing_jobs
        else:
            jobs = get_jobs(input)
            db[input] = jobs
    else:
        return redirect("/")

    return render_template("search.html", input=input, jobs=jobs, job_count=len(jobs))

@app.route("/export")
def export():
    try:
        input = request.args.get("input")

        if not input:
            raise Exception()

        input = input.lower()
        jobs = db.get(input)

        if not jobs:
            raise Exception()

        save_to_file(jobs)

        return send_file("jobs.csv")
    except:
        return redirect("/")

app.run(host="127.0.0.1")
