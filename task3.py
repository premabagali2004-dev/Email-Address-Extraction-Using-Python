import re

# Read the input text file
with open("input.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Find all email addresses
emails = re.findall(
    r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
    text
)

# Remove duplicates while preserving order
emails = list(dict.fromkeys(emails))

# Save each email address on a separate line
with open("emails.txt", "w", encoding="utf-8") as file:
    for email in emails:
        file.write(email + "\n")

print("Email extraction completed successfully!")
print("Total email addresses found:", len(emails))
print("Results saved in emails.txt")
