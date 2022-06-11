from cgi import print_form
from email import message
import string
from bs4 import BeautifulSoup
import requests
from time import sleep
import smtplib

def send_message(message):

    senders_email = "alikhaledabdallah454@gmail.com"
    senders_password = "ryzchfxrprttgovy"
    receiver_email = "v3n0m444555444@gmail.com"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(senders_email, senders_password)
    server.sendmail(senders_email, receiver_email, message)


def scrap(file):

    url : string = "https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=python&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=python&pDate=I&sequence=3&startPage=1"
    html_page : string = requests.get(url).text

    soup = BeautifulSoup(html_page, "lxml")

    jobs = soup.find_all("li", class_ = "clearfix job-bx wht-shd-bx")

    for job in jobs:

        company_name = job.h3.text.strip()
        skills = job.find("span", class_ = "srp-skills").text.strip()
        posted_date = job.find("span", class_ = "sim-posted").span.text.strip()
        more_info_link = job.header.h2.a["href"].strip()


        file.writelines(f"COMPANY NAME : {company_name}\n")
        file.writelines(f"SKILLS REQUIRED : {skills}\n")
        file.writelines(f"POSTED DATE : {posted_date}\n")
        file.writelines(f"MORE INFO : {more_info_link}")
        file.writelines("\n\n\n\n\n")



i = 1
waiting_time_in_minutes = 2

while(True):

    file = open(f"file{i}.txt", "w")
    scrap(file)
    file.close()

    print("*" * 100)

    file = open("idk.txt", "r")
    intro = "FROM SERVER Here are the job opportunities that have been found, Enjoy\n\n\n\n"
    message = intro + file.read()
    file.close()

    send_message(message)

    i = i + 1
    sleep(waiting_time_in_minutes * 60)


#FAK YOU