# phone book
# Create a phone book dictionary with 4 contacts. Each contact should have a name and a phone number.

phone_Book = {
    "Hammad": 123456,
    "Ali": 654321,
    "Ahmed": 456789,
    "Kashif": 987654
}

new_contact = input("Enter the name of the contact: ")
new_number = int(input("Enter the number of the contact: ")) 
phone_Book[new_contact] = new_number
print(phone_Book)

contact = input("Enter the name of the contact you want to remove: ")
phone_Book.pop(contact)
print(phone_Book)

search = input("Enter the name of the contact you want to search: ")
if search in phone_Book:
    print(f"{search} is in the phone book")

updated_contact = input("Enter the name of the contact you want to update: ")
new_name = input("Enter the updated name: ")

updated_number = int(input("Enter the updated number: "))
new_number = phone_Book[updated_contact] = updated_number

if updated_contact in phone_Book:
    phone_Book[updated_contact] = new_name
    phone_Book.pop(updated_contact)
    
if updated_number in phone_Book: 
    phone_Book[updated_number] = new_number
    phone_Book.pop(updated_number)

phone_Book[new_name] = new_number
print(phone_Book)

# finish