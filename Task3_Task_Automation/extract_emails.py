import re

input_file = "input.txt"
output_file = "emails.txt"

try:
    with open(input_file, "r") as file:
        text = file.read()
except FileNotFoundError:
    print(f"Input file '{input_file}' not found. Make sure it is in the same folder.")
    exit()
    
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

unique_emails = set(emails)

with open(output_file, "w") as file:
    for email in unique_emails:
        file.write(email + "\n")

print(f"✅ Email extraction completed.")
print(f"📧 Total emails found: {len(unique_emails)}")
print(f"📁 Emails saved to '{output_file}'")