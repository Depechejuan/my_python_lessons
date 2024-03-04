customer = {
    "name": "John Smith",
    "age": 37,
    "is_verified": True,
    "email": "john@gmail.com",
    "phone": 123456789
}
#Don't have duplicates

print(customer["name"])
# print(customer["birthdate"]) ERROR!
# print(customer["Name"]) Also error, it's not exact
print(customer.get("Name"))
#None, this not generates an error
print (customer.get("birthdate", "Jul 21 1986"))

customer["name"] = "Jack Smith"
print(customer["name"])
customer["birthdate"] = "Jul 21 1986"
print(customer["birthdate"])