import requests
from bs4 import BeautifulSoup


print("What do you want to search for: ")
search = input(">").lower().replace(" ", "")
print("Put some skill that you are familier with")
skill = input(">").title()
print(f'Filtering {skill}')

html_text = requests.get(f"https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords={search}&txtLocation=").text

soup = BeautifulSoup(html_text, 'lxml')

jobs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
for job in jobs:
    
    job_date = job.find('span', class_='sim-posted').span.text
    if 'few' not in job_date:
        company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
        skills = job.find('span', class_='srp-skills').text.title().replace(' ', '')
        if skill in skills:

            more_info = job.header.h2.a['href']
            print(f"Company name: {company_name.strip()}")
            print(f"Required skills: {skills.strip()}")
            print(f"Published date: {job_date}")

            print('')
        