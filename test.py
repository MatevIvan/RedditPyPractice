def vowelReplace(s):
  temp = ""
  vowels = ['a','e','i','o','u','y']
  for c in s:
    if c.lower() in vowels:
      temp += "*"
    else:
      temp += c
  return temp


print(vowelReplace("Ivan"))
print(vowelReplace("Becca"))

# Input: string
# output: string

# create a temp string variable
# go through s and check every letter to see if it's a vowel
# if it is a vowel, change the vowel to "*"
# return the modified string