def assess_password_strength(password):
    """
    Assesses the strength of a password based on various criteria.

    Args:
        password (str): The password to assess.

    Returns:
        tuple: A tuple containing the password strength (str) and feedback (str).
    """
    length = len(password)
    has_uppercase = any(c.isupper() for c in password)
    has_lowercase = any(c.islower() for c in password)
    has_digits = any(c.isdigit() for c in password)
    has_special = any(c in password for c in password)

    score = 0
    feedback = ""

    if length >= 12:
        score += 2
        feedback += "Length is good (+2). "
    elif length >= 8:
        score += 1
        feedback += "Length is okay (+1). Consider making it longer. "
    else:
        feedback += "Length is too short! Try making it at least 8 characters long. "

    if has_uppercase:
        score += 1
        feedback += "Contains uppercase letters (+1). "
    else:
        feedback += "Consider adding uppercase letters. "

    if has_lowercase:
        score += 1
        feedback += "Contains lowercase letters (+1). "
    else:
        feedback += "Consider adding lowercase letters. "

    if has_digits:
        score += 1
        feedback += "Contains numbers (+1). "
    else:
        feedback += "Consider adding numbers. "

    if has_special:
        score += 1
        feedback += "Contains special characters (+1). "
    else:
        feedback += "Consider adding special characters (e.g., !@#$%^&*). "

    if score >= 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback.strip()

if __name__ == "__main__":
    while True:
        password = input("Enter the password to check (or type 'exit' to quit): ")
        if password.lower() == 'exit':
            break

        strength, feedback = assess_password_strength(password)
        print(f"\nPassword Strength: {strength}")
        print(f"Feedback: {feedback}\n")
