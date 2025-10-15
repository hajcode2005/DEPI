word = input("Enter your string : ")
print(word)
vowel = "aeiouAEIOU"
for i in word:
    if i in vowel:
      new_word = word.replace(i, "")
print(new_word)    