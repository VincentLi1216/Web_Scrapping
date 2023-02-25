import time
from bs4 import BeautifulSoup
import requests

unfamiliar_skill = "none"

def find_jobs(url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation="):
    global unfamiliar_skill
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, "lxml")
    jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")

    jobs_found = 0
    jobs_filtered_out = 0

    if unfamiliar_skill == "none":
        print("Put some skill that your are not familiar with (put \"no\" if you want to disable this func.)")
        unfamiliar_skill = input(">")

    if unfamiliar_skill != "no":
        print(f'Filtering out \"{unfamiliar_skill}\"')
    else:
        print("Disable filter func")

    print("-" * 30)
    for index, job in enumerate(jobs):
        published_date = job.find("span", class_="sim-posted").text
        if "few" not in published_date:
            continue
        company_name = job.find("h3", class_="joblist-comp-name").text.strip()
        skills = job.find("span", class_="srp-skills").text
        if unfamiliar_skill.upper() in skills.upper() and unfamiliar_skill != "no":
            jobs_filtered_out += 1
            continue
        more_info = job.header.h2.a["href"]
        jobs_found += 1
        with open(f'posts/{index}.txt', "w") as f:
            f.write(f'Company Name: {company_name.strip()}\n')
            f.write(f'Required Skills: {skills.strip()}\n')
            f.write(f'More Info: {more_info}\n')
            print(f'Company Name: {company_name.strip()}')
            print(f'Required Skills: {skills.strip()}')
            print(f'More Info: {more_info}')
            print("-" * 30)

    print(f'Result: {jobs_found} jobs found!')
    print(f'(Filtered: {jobs_filtered_out} jobs out)')


if __name__ == "__main__":
    while True:
        find_jobs()
        time_wait = 3
        print(f'Waiting {time_wait} seconds...')
        time.sleep(time_wait)
