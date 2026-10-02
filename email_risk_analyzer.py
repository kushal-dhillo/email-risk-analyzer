# Email Risk Analyzer

email = input("Enter the email content: ")

text = email.lower()
risk_score = 0
warnings = []

# Check for urgent requests
urgent_words = ["urgent", "immediately", "act now", "asap", "account will be closed"]

for word in urgent_words:
    if word in text:
        risk_score += 1
        warnings.append("Urgent or threatening language detected.")
        break

# Check for suspicious links
if "http://" in text or "https://" in text or "www." in text:
    risk_score += 2
    warnings.append("Link detected. Verify the link before opening it.")

# Check for sensitive information requests
sensitive_words = [
    "password",
    "otp",
    "credit card",
    "bank account",
    "cvv",
    "pin",
    "social security"
]

for word in sensitive_words:
    if word in text:
        risk_score += 2
        warnings.append("Request for sensitive information detected.")
        break

# Check for suspicious money/payment requests
money_words = ["send money", "payment", "transfer money", "gift card"]

for word in money_words:
    if word in text:
        risk_score += 2
        warnings.append("Possible financial request detected.")
        break

# Display result
print("\n--- Email Risk Analysis ---")

if risk_score >= 5:
    print("Risk Level: HIGH")
elif risk_score >= 2:
    print("Risk Level: MEDIUM")
else:
    print("Risk Level: LOW")

print("Risk Score:", risk_score)

if warnings:
    print("\nWarnings:")
    for warning in warnings:
        print("-", warning)
else:
    print("\nNo obvious suspicious patterns detected.")
