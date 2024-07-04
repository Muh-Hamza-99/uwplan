# This file contains all the string formatting functions used to format the requirement strings.

import re

# ABC/DEF 123 -> ABC 123/DEF 123 | ABC or DEF 123 -> ABC 123 or DEF 123
def two_subjects_one_code(string):
    return re.sub(r"([A-Z]{2,})\s?(/|or)\s?([A-Z]{2,})\s?([0-9]{3}[A-Z]?)", r"\1 \4/\3 \4", string)

# ABC 123/456 -> ABC 123/ABC 456 | ABC 123 or 456 -> ABC 123 or ABC 456
def one_subject_two_codes(string):
    return re.sub(r"([A-Z]{2,})\s?([0-9]{3}[A-Z]?)\s?(/|or)\s?([0-9]{3}[A-Z]?)", r"\1 \2/\1 \4", string)

# ABC 111, 222, 333, ... -> ABC 111, ABC 222, ABC 333, ...
def one_subject_multiple_numbers(string):
    many_catalog_numbers = re.findall(r"[A-Z]{2,}\s?(?:[0-9]{3}[A-Z]?,\s?)+[0-9]{3}[A-Z]?", string)
    for match in many_catalog_numbers:
        subject_code = re.findall(r"[A-Z]{2,}", match)[0]
        catalog_numbers = re.findall(r"[0-9]{3}[A-Z]?", match)
        expanded_string = ", ".join([f"{subject_code} {catalog_number}" for catalog_number in catalog_numbers])
        string = string.replace(match, expanded_string)
    return string

# One of AAA 111, BBB 222, CCC 333, ... -> (AAA 111 or BBB 222 or CCC 333 or ...)
def one_ofs(string):
    one_ofs = re.findall(r"[Oo]ne of (?:[A-Z]{2,}\s?[0-9]{3}[A-Z]?(?:,|/)?\s?)+", string)
    for match in one_ofs:
        codes = re.findall(r"[A-Z]{2,}\s?[0-9]{3}[A-Z]?", match)
        or_string = " or ".join(codes)
        string = string.replace(match, f"({or_string})")
    return string

# ABC 123 with at least XX% -> ABC 123 {XX%}
# At least XX% in ABC 123 -> ABC 123 {XX%}
def course_grades(string):
    string = re.sub(r"([A-Z]{2,}\s?[0-9]{3}[A-Z]?) with a grade of at least ([0-9]{2,}%)", r"\1 {\2}", string)
    string = re.sub(r"[Aa]t least ([0-9]{2,}%) in ([A-Z]{2,}\s?[0-9]{3}[A-Z]?)", r"\2 {\1}", string)
    return string