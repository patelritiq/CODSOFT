import random
import string

def generate_password(length):
    if length < 4:
        raise ValueError("Password length must be at least 4 to include all character types.")
    
    allowed_special = "!@#$%^&_~"
    character_pool = string.ascii_uppercase + string.ascii_lowercase + string.digits + allowed_special

    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(allowed_special)
    ]

    password += random.choices(character_pool, k=length - 4)

    random.shuffle(password)
    
    return ''.join(password)

def main():
    print("\n===== The Password Architect =====")
    
    while True:
        try:
            length = int(input("Enter the desired length of the password: ").strip())
            if length <= 0:
                raise ValueError("Length must be a positive integer.")
            
            password = generate_password(length)
            print(f"\nYour Generated Password is: {password}\n")
        except ValueError as e:
            print(f"Error: {e}")

        again = input("Would you like to generate another password? (y/n): ").strip().lower()
        if again != 'y':
            break
    
    print("=============================================")

if __name__ == "__main__":
    main()
