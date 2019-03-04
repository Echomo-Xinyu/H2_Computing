# by Mr Leong, not myself

# 0d48 - '0' ... 0d57 - '9'
# 0d65 - 'A' ... 0d90 - 'Z'
# 0d97 - 'a' ... 0d122 - 'z'

plainText = input("Please enter a message to encrypt: ")
offset = int(input("Please enter a shift value: "))
encodedText = ""

for c in plainText:
    encodedChar = c
    if ord(c) >= 48 and ord(c) <= 57:
        shiftedChar = chr(ord(c) + offset % 10)
        encodedChar = shiftedChar if ord(shiftedChar) >= 48 and ord(shiftedChar) <= 57 else chr(48 + ord(shiftedChar) % 57 - 1)
    elif ord(c) >= 65 and ord(c) <= 90:
        shiftedChar = chr(ord(c) + offset % 26)
        encodedChar = shiftedChar if ord(shiftedChar) >= 65 and ord(shiftedChar) <= 90 else chr(65 + ord(shiftedChar) % 90 - 1)
    elif ord(c) >= 97 and ord(c) <= 122:
        shiftedChar = chr(ord(c) + offset % 26)
        encodedChar = shiftedChar if ord(shiftedChar) >= 97 and ord(shiftedChar) <= 122 else chr(97 + ord(shiftedChar) % 122 - 1)
    encodedText += encodedChar

print("The encoded message is: " + encodedText)