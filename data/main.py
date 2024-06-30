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

def format_requirements(requirements: str) -> str:
    requirements = requirements.replace("0.50", "1").replace("1.00", "2").replace("1.50", "3").replace("2.00", "4").replace("2.50", "5")
    requirements = requirements.replace("0.5", "1").replace("1.0", "2").replace("1.5", "3").replace("2.0", "4").replace("2.5", "5")
    return requirements

class Course:
    def __init__(self, code, title, description, requirements):
        self.code = code
        self.title = title
        self.description = description
        self.requirements = format_requirements(requirements)
        self.prereqs = requirement_splitter(self.requirements)["prereqs"]
        self.coreqs = requirement_splitter(self.requirements)["coreqs"]
        self.antireqs = requirement_splitter(self.requirements)["antireqs"]
    def pretty_print(self, extended=False):
        if extended:
            print(f"Course: {self.code} - {self.title}")
            print(f"Description: {self.description}")
        else:
            print(f"Course: {self.code}")
        print(f"Requirements: {self.requirements}")
        print(f"Prerequisites: {self.prereqs}")
        print(f"Corequisites: {self.coreqs}")
        print(f"Antirequisites: {self.antireqs}")
        print("\n")
    def parse_prereqs(self):
        prereqs = self.prereqs

        # ABC/DEF 123 -> ABC 123/DEF 123 | ABC or DEF 123 -> ABC 123 or DEF 123
        prereqs = re.sub(r"([A-Z]{2,})\s?(/|or)\s?([A-Z]{2,})\s?([0-9]{3}[A-Z]?)", r"\1 \4 \2 \3 \4", prereqs)
        
        # ABC 123/456 -> ABC 123/ABC 456 | ABC 123 or 456 -> ABC 123 or ABC 456
        prereqs = re.sub(r"([A-Z]{2,})\s?([0-9]{3}[A-Z]?)\s?(/|or)\s?([0-9]{3}[A-Z]?)", r"\1 \2 \3 \1 \4", prereqs)

        print(f"Course: {self.code}")
        print(f"Prerequisites: {self.prereqs}")
        print(f"Parsed prerequisites: {prereqs}\n")
        
def main():
    data = pd.read_csv("courses.csv", encoding="unicode_escape")
    data["requirements"] = data["requirements"].fillna("")
    courses = []
    for i, row in data.iterrows():
        code, title, description, requirements = row["code"], row["title"], row["description"], row["requirements"]
        course = Course(code, title, description, requirements)
        course.parse_prereqs()
        courses.append(course)

main()