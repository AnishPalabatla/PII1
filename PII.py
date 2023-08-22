def remove_pii(text):
    pii_keywords = ["name", "address", "phone", "email", "SSN", "credit card", "bank account", "passport", "medical record", "health insurance", "biometric", "username", "IP address", "GPS coordinates"]
    words = text.split()
    result = []
    for word in words:
        cont = any(keyword in word.lower() for keyword in pii_keywords)
        if not cont:
            result.append(word)
        else:
            result.append("[CENSORED]")
    output = ' '.join(result)
    return output
input = "Anish's email is test@temp.com and his phone number is 123-456-7890, SSN is 765-433-123"
output = remove_pii(input)
print(output)
