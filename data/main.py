import re
import pandas as pd

# Return type is dict("prereqs": str, "coreqs": str, "antireqs": str)
def requirement_splitter() -> dict[str, str]:
    pass

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
    pass