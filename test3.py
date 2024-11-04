multiline_string = '''This is a long string
That spans across multiple lines'''
print(multiline_string)
#print first 5 char from index 0 to 5
print(multiline_string[0:5])
#- makes it go from the back so it prints last character
print(multiline_string[-1])
#print from 2nd char to 2nd to last
print(multiline_string[1:-1])
#formated string
name = "Robert"
msg = f"{name} is a legend"
print(msg)