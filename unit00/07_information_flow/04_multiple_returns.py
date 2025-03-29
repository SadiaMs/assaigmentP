def get_user_info():
    """
    Asks the user for their first name, last name, and email address 📧
    Returns them as a tuple. 👤
    """
    first_name: str = input("👋 What is your first name?: ")
    last_name: str = input("🔤 What is your last name?: ")
    email_address: str = input("📧 What is your email address?: ")
    
    return first_name, last_name, email_address

########## No need to edit code past this point :) ##########

def main():
    user_data = get_user_info()
    print("✅ Received the following user data:", user_data)

if __name__ == "__main__":
     main()
