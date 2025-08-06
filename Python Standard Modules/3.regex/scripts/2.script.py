# Validate Phone Number Format

# Check if a string is a valid US phone number in the format (XXX) XXX-XXXX.
import re 

phone = "(123) 456-7890"

def phole_validator(phone):
    pattern = r'^\(\d{3}\) \d{3}-\d{4}$'
    return bool(re.match(pattern, phone))


print(phole_validator(phone))