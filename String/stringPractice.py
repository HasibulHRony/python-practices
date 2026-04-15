# commad = input("Enter your command: ")
# if commad == "open":
#     print("You are welcome!")
# else:
#     print("Get lost!")



#1. Take a string input and print it in uppercase
name = "Hasibul Hassan Rony"
print(name.upper())
print(name.lower())

#2. Count the number of characters in a string
print(len(name))


#3. Print the first and last character of a string
print(name[0])
print(name[-1])


#4. Reverse a string (without using built-in reverse)
splitingName = ""
for charecter in name:
    splitingName = charecter + splitingName

print(splitingName)

#5. vowels counting
vowels = 0
for letter in name:
    letter = letter.lower()
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        vowels = vowels + 1

print(vowels)


#6. Check if a string is a palindrome (same forward & backward)
# txt = input("Please enter the Text: ")
# reverseTxt = ""
# txt = txt.lower()
# for letter in txt:
#     reverseTxt = letter + reverseTxt

# if reverseTxt == txt:
#     print("Wow! It's a Palindrome. Welcome!")
# else:
#     print("Sorry! It's No.")

#7. Replace all spaces with _
splitedTxt = (name.split( ))
newTxt = ""
for eachTxt in splitedTxt:
    newTxt = newTxt + eachTxt
print(newTxt)


#8. Find the most frequent character in a string

loop = 1
while loop == 1:
    #get user's string input
    string = input("\nEnter a String: ").upper().replace(" ", "")
    if string == "":
        #exception handling
        print("\nEnter a valid string!")
    else:
        loop = 0

frequency = {}

for x in string:
    if x in frequency:
        frequency[x] +=1
    else:
        frequency[x] = 1

print(frequency)