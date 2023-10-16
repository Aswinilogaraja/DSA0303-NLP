import re

# Sample text to search
text = """
Alice's email is alice@example.com.
Bob's email is bob123@gmail.com.
John's email is john.doe@company.org.
"""

# Define a regex pattern to match email addresses
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Find all email addresses in the text using the regex pattern
emails = re.findall(email_pattern, text)

# Print the found email addresses
print("Email addresses found in the text:")
for email in emails:
    print(email)
