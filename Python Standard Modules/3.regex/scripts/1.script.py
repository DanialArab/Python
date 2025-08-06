# Extract All Email Addresses


# Given a string, extract all email addresses using a regular expression.

text = "Please contact us at support@example.com or sales@example.org for assistance."

import re 

def email_extractor(text_data):
    return re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b', text_data)

print(email_extractor(text))