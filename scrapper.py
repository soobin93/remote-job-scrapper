from stackoverflow import get_jobs as get_so_jobs
from weworkremotely import get_jobs as get_wework_jobs
from remoteok import get_jobs as get_remoteok_jobs

def get_jobs(input):
    jobs = []

    jobs += get_so_jobs(input)
    jobs += get_wework_jobs(input)
    jobs += get_remoteok_jobs(input)

    return jobs
