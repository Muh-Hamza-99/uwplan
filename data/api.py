import os
import csv
import requests
from dotenv import load_dotenv

load_dotenv()

URL = "https://openapi.data.uwaterloo.ca/v3/Courses/1241/"
response = requests.get(URL, headers={ "x-api-key": os.getenv("UW_API_KEY") })
courses = response.json()

def valid_course(course) -> bool:
    return course["associatedAcademicCareer"] == "UG" and course["courseComponentCode"] != "SEM"

with open("courses.csv", "w", newline="") as file:
    headers = ["code", "title", "description", "requirements"]
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    for course in courses:
        if valid_course(course):
            code = f"{course['subjectCode']} {course['catalogNumber']}".strip()
            title, description, requirements = course["title"], course["description"], course["requirementsDescription"]
            values = [code, title, description, requirements]
            writer.writerow({ key: value for key, value in zip(headers, values) })
