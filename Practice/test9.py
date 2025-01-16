#dictionary
person = {
    "name": "Robert",
    "age": 25,
    "is_cool": True
}

print(person["name"])
print(person.get("birthday"))
print(person.get("birthday", "No such key exists"))

person["birthday"] = "Jan 3 1999"
print(person["birthday"])