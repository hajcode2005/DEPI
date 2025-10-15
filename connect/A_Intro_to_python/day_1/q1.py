strig = input("Enter your string : ")
coun = 0
vowel = "aeiouAEIOU"
for char in strig:
    if char in vowel:
      coun += 1
print("the number of characters is : ", coun)  