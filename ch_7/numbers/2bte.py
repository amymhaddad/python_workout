# Create a list of strings, each of which contains a US-style phone numbers (XXX-YYY-ZZZZ, where XXX is the area code). 
# Use a list comprehension to return a new list of strings, in which any phone number whose YYY begins with the digits 0-5 will have its area code changed to XXX+1.


phone_number = ['431-0222-2222', '111-0111-1111', '111-999-1111']

new_phone_number = [
    str(int(number.split("-")[0]) + 1) + "-" + number.split("-")[1] + "-" + number.split("-")[2]
    for number in phone_number
    if number.split("-")[1].startswith(('0', '1', '2', '3', '4', '5'))
]

print(new_phone_number)

