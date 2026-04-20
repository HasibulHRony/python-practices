def translater(phrase):
    translation = ""
    for letter in phrase:
        if(letter in "AEIOUaeiou"):
            if letter.isupper():
               translation = translation + "G"
            else: 
                translation = translation + "g"
        else:
            translation=translation + letter
    return translation


print(translater(input("Enter a phrase: ")))