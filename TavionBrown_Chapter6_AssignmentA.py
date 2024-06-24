import re

def validate_phone_number(phone_number):
    """
    Validates a phone number.
    The pattern considered here is (XXX) XXX-XXXX, XXX-XXX-XXXX, XXX.XXX.XXXX, XXX XXX XXXX, or XXXXXXXXXX.
    """
# Define the regular expression pattern for validating phone numbers
    pattern = re.compile(r'^(\(\d{3}\)\s?|\d{3}[-.\s]?|\d{3})\d{3}[-.\s]?\d{4}$')
# Return true if the phone number matches the pattern
    return bool(pattern.match(phone_number))

def validate_ssn(ssn):
    """
    Validates a Social Security Number (SSN).
    The pattern considered here is XXX-XX-XXXX
    """
# Define the regular expression pattern for validating SSN
    pattern = re.compile(r'^\d{3}-\d{2}-\d{4}$')
# Return true if the SSn matches the pattern
    return bool(pattern.match(ssn))

def validate_zip_code(zip_code):
    """
    Validates a US ZIP code.
    The pattern considered here is XXXXX or XXXXX-XXXX
    """
# Define the regular expression pattern for validating Zip codes
    pattern = re.compile(r'^\d{5}(-\d{4})?$')
# Return true if the zip code matches the pattern
    return bool(pattern.match(zip_code))

def main():
# Tell user to put in a phone number
    phone_number = input("Enter phone number (e.g., 123-456-7890): ")
# Tell user to put in a social security number
    ssn = input("Enter social security number (e.g., 123-45-6789): ")
# Tell user to put in a zip code
    zip_code = input("Enter ZIP code (e.g., 12345 or 12345-6789): ")

# Print this result if its right
    is_phone_valid = validate_phone_number(phone_number)
    is_ssn_valid = validate_ssn(ssn)
    is_zip_valid = validate_zip_code(zip_code)

# Print this result if its wrong
    print(f"Phone number valid: {is_phone_valid}")
    print(f"Social security number valid: {is_ssn_valid}")
    print(f"ZIP code valid: {is_zip_valid}")

# Execute the main function if the code is run directly
if __name__ == "__main__":
    main()
