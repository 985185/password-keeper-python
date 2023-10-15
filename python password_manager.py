import os

# Check if the credentials file exists; create if not
if not os.path.exists("credentials.txt"):
    with open("credentials.txt", "w") as file:
        file.write("Welcome to the Password Manager!\n")
        file.write("================================\n")

# Display the welcome message
print("Welcome to the Password Manager!")
print("================================")

# Main menu for user actions
while True:
    print("\nOptions:")
    print("1. Add stored credentials")
    print("2. View stored credentials")
    print("3. Exit")
    
    choice = input("Select an option (1/2/3): ")
    
    if choice == '1':
        # Add credentials
        print("\n*** Adding stored credentials ***")
        username = input("Enter your username: ")  # Username
        password = input("Enter your password: ")  # Password
        url = input("Enter the website: ")  # Website
        
        with open("credentials.txt", "a") as file:
            file.write("\nUsername: " + username)
            file.write("\nPassword: " + password)
            file.write("\nWebsite/Resource: " + url + "\n")
        print("\n*** Credentials added successfully! ***")
    
    elif choice == '2':
        # View credentials
        print("\n*** Viewing stored credentials ***")
        with open("credentials.txt", "r") as file:
            content = file.read()
            if content:
                print("\nStored Credentials:\n")
                print(content)
            else:
                print("\nNo credentials stored yet.")
    
    elif choice == '3':
        # Exit the script
        print("Exiting the script. Thank you!")
        break
    
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

# End of the script
