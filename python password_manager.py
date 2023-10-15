# Main menu for user actions
while True:
    # ... (Previous menu options)
    
    if choice == '1':
        # Add credentials
        print("\n*** Adding stored credentials ***")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        url = input("Enter the website: ")
        
        with open("credentials.txt", "a") as file:
            file.write("\nUsername: " + username)
            file.write("\nPassword: " + password)
            file.write("\nWebsite/Resource: " + url + "\n")
        print("\n*** Credentials added successfully! ***")
    
    elif choice == '2':
        # View or amend credentials
        print("\n*** Viewing stored credentials ***")
        with open("credentials.txt", "r") as file:
            content = file.read()
            if content:
                print("\nStored Credentials:\n")
                print(content)
                amend_choice = input("Would you like to amend a password? (y/n): ")
                if amend_choice.lower() == 'y':
                    amend_username = input("Enter the username to amend: ")
                    new_password = input("Enter the new password: ")
                    content = content.replace(f"Username: {amend_username}\nPassword: {password}\n", f"Username: {amend_username}\nPassword: {new_password}\n")
                    with open("credentials.txt", "w") as file:
                        file.write(content)
                    print(f"\n*** Password for {amend_username} amended successfully! ***")
            else:
                print("\nNo credentials stored yet.")
    
    elif choice == '3':
        # Exit the script
        print("Exiting the script. Thank you!")
        break
    
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

# ... (End of the script)
