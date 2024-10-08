def vowelReplace(testString):
  """
  input: String
  ouput: String

  Approach:
  Create a temp string variable
  Go through the testString and check every letter to see if it's a vowel
  If it is a vowel, change it to "*"
  Return the modified temp string variable 
  """

  # create a temp variable to store the new string
  temp = ""
  # create a list of vowels
  vowels = ['a','e','i','o','u','y']
  # go through each character in the testString
  for character in testString:
    # if the lowercase character is found in the vowels list, add "*" to the return string
    if character.lower() in vowels:
      temp += "*"
    else:
      # else add the current character to the return string
      temp += character
  # return the temp string after we get out of the loop
  return temp

# Test cases
print(vowelReplace("Ivan"))
print(vowelReplace("Becca"))
