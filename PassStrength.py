import re
import string

def check_password_strength(password):
    """
    Check the strength of a password based on multiple criteria.
    Returns a dictionary with strength score and feedback.
    """
    score = 0
    feedback = []
    
    # Length check
    if len(password) >= 8:
        score += 2
    elif len(password) >= 6:
        score += 1
        feedback.append("Password should be at least 8 characters long")
    else:
        feedback.append("Password is too short (minimum 6 characters)")
    
    # Uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters")
    
    # Lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters")
    
    # Numbers
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add numbers")
    
    # Special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 2
    else:
        feedback.append("Add special characters (!@#$%^&*(),.?\":{}|<>)")
    
    # No repeated characters
    if not re.search(r"(.)\1{2,}", password):
        score += 1
    else:
        feedback.append("Avoid repeating characters more than twice")
    
    # No common patterns
    common_patterns = ['123', 'abc', 'qwerty', 'password', '111', '000']
    if not any(pattern in password.lower() for pattern in common_patterns):
        score += 1
    else:
        feedback.append("Avoid common patterns like '123', 'abc', 'qwerty'")
    
    # Determine strength level
    if score >= 8:
        strength = "Very Strong"
    elif score >= 6:
        strength = "Strong"
    elif score >= 4:
        strength = "Medium"
    elif score >= 2:
        strength = "Weak"
    else:
        strength = "Very Weak"
    
    return {
        'password': password,
        'strength': strength,
        'score': score,
        'max_score': 9,
        'feedback': feedback
    }

def display_results(result):
    """Display password strength results in a formatted way."""
    print(f"\n{'='*50}")
    print(f"PASSWORD STRENGTH ANALYSIS")
    print(f"{'='*50}")
    print(f"Password: {'*' * len(result['password'])}")
    print(f"Strength: {result['strength']}")
    print(f"Score: {result['score']}/{result['max_score']}")
    
    if result['feedback']:
        print(f"\nSuggestions for improvement:")
        for i, suggestion in enumerate(result['feedback'], 1):
            print(f"{i}. {suggestion}")
    else:
        print(f"\nExcellent! Your password meets all security criteria.")

def generate_strong_password(length=12):
    """Generate a strong password with specified length."""
    import random
    
    # Character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = "!@#$%^&*(),.?\":{}|<>"
    
    # Ensure at least one character from each set
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special)
    ]
    
    # Fill remaining length with random characters from all sets
    all_chars = lowercase + uppercase + digits + special
    for _ in range(length - 4):
        password.append(random.choice(all_chars))
    
    # Shuffle the password list
    random.shuffle(password)
    
    return ''.join(password)

def main():
    """Main function to run the password strength checker."""
    print("PASSWORD STRENGTH CHECKER")
    print("="*50)
    
    while True:
        print("\nOptions:")
        print("1. Check password strength")
        print("2. Generate strong password")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == '1':
            password = input("\nEnter password to check: ")
            if password:
                result = check_password_strength(password)
                display_results(result)
            else:
                print("Please enter a valid password.")
        
        elif choice == '2':
            try:
                length = input("\nEnter desired password length (default 12): ").strip()
                length = int(length) if length else 12
                if length < 4:
                    print("Minimum length is 4 characters.")
                    continue
                
                generated_password = generate_strong_password(length)
                print(f"\nGenerated strong password: {generated_password}")
                
                # Check the generated password
                result = check_password_strength(generated_password)
                display_results(result)
                
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == '3':
            print("\nThank you for using Password Strength Checker!")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Example usage and testing
if __name__ == "__main__":
    # Test with sample passwords
    test_passwords = [
        "123456",
        "password",
        "Password123",
        "MyStr0ng!Pass",
        "Sup3rS3cur3!P@ssw0rd"
    ]
    
    print(" TESTING PASSWORD STRENGTH CHECKER")
    print("="*50)
    
    for pwd in test_passwords:
        result = check_password_strength(pwd)
        print(f"\nPassword: {pwd}")
        print(f"Strength: {result['strength']} ({result['score']}/{result['max_score']})")
    
    print("\n" + "="*50)
    
    # Run interactive mode
    main()
