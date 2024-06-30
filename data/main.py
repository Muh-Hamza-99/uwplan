import re
import pandas as pd

# Return type is dict("prereqs": str, "coreqs": str, "antireqs": str)
def requirement_splitter(requirement: str) -> dict[str, str]:
    result = { "prereqs": "", "coreqs": "", "antireqs": "" }
    prereqs_match = re.search(r"Prereq: ([^.]*)", requirement)
    coreqs_match = re.search(r"Coreq: ([^.]*)", requirement)
    antireqs_match = re.search(r"Antireq: ([^.]*)", requirement)
    if prereqs_match:
        result["prereqs"] = prereqs_match.group(1).strip()
    if coreqs_match:
        result["coreqs"] = coreqs_match.group(1).strip()
    if antireqs_match:
        result["antireqs"] = antireqs_match.group(1).strip()
    return result

class Course:
    def __init__(self, code, title, description, requirements):
        self.code = code
        self.title = title
        self.description = description
        self.requirements = requirements
        self.prereqs = requirement_splitter(requirements)["prereqs"]
        self.coreqs = requirement_splitter(requirements)["coreqs"]
        self.antireqs = requirement_splitter(requirements)["antireqs"]

def main():
    data = pd.read_csv("courses.csv", encoding="unicode_escape")
    data["requirements"] = data["requirements"].fillna("")
    courses = []
    for i, row in data.iterrows():
        code, title, description, requirements = row["code"], row["title"], row["description"], row["requirements"]
        course = Course(code, title, description, requirements)
        courses.append(course)

main()