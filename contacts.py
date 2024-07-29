# You task
# Help King Kahuka by developing a contact book program.

# This program will store the details of foreign monarchs, including their names, phone numbers, emails, and addresses, 
# allowing King Kahuka to add, remove, update, and search for contacts effortlessly.

# Instructions
# Define the contact book as a dictionary named contacts, where the key is the contact's name, and the value is another 
# dictionary containing phone, email, and address.

# Implement the following features:

# Adding a Contact:
# Prompt for the contact's name, phone number, email, and address.
# Check if the contact already exists. If not, add it to the contact book.

# Removing a Contact:
# Ask for the name of the contact to remove.
# Verify if the contact exists before removal.

# Updating a Contact:
# Request the name of the contact to update.
# Allow the user to enter new values for the contact's phone, email, and address.

# Searching for a Contact:
# Prompt for the contact's name to search.
# Display the contact's details if found.
# Displaying Contacts:
# Display all contacts in the contact book.
# Exiting the Program:
# Allow the user to exit the program.

contacts = {'jw': {'phone_number': '8600', 'email': '@gmail.com', 'address': 'amk'}}

contact_name = input("Input contact's name: ")
phone_number = input("Input phone number: ")
email = input("Input email: ")
address = input("Input address: ")

if contact_name in contacts:
    print('Contact already exists.')

else:
    # Add new contact details to the dictionary
    contacts[contact_name] = {
        'phone_number': phone_number,
        'email': email,
        'address': address
    }
    print('Contact added successfully.')

# Remove contact if present in dict
removal = input("Contact to remove (Type name of contact): ")
if removal in contacts:
    del contacts[removal]
else:
    print("Contact not found. ")

# Update contact information
update = input("Contact to update (Type name of contact): ")
updated_dict = {}

if update in contacts:
    update_phone_number = input("Input phone number: ")
    update_email = input("Input email: ")
    update_address = input("Input address: ")
    
    updated_dict[update] = {
        'phone_number': update_phone_number,
        'email': update_email,
        'address': update_address
    }

    contacts[update] = updated_dict[update]

    print('Contact updated successfully.')
else:
    print("No contact found.")

print(contacts)

# Searching for a Contact
search = input("Input contact's name to search: ") # Prompt for the contact's name to search.

# Display the contact's details if found.
if search in contacts:
    print(contacts[search])
else:
    print("No such contact.")

# Displaying Contacts:
# Display all contacts in the contact book.
print(f"All contacts: {contacts}")
