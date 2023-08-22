def remove_pii(text):
    pii_keywords = [
        "name", "address", "phone", "email", "SSN", "credit card", "bank account", "passport", "medical record", "health insurance", "biometric", "username", "IP address", "GPS coordinates"]
    words = text.split()
    result = []
    for word in words:
        contains_pii = any(keyword in word.lower() for keyword in pii_keywords)
        if not contains_pii:
            result.append(word)
        else:
            result.append("[REDACTED]")
    redacted_text = ' '.join(result)
    return redacted_text
text_with_pii = "Hello, my name is John and my phone number is 123-456-7890."
redacted_text = remove_pii(text_with_pii)
print(redacted_text)