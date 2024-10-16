def vowel_replace(phrase: str) -> str:
  """
  Args:
    phrase: str
  Returns:
    str

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
  for character in phrase:
    # if the lowercase character is found in the vowels list, add "*" to the return string
    if character.lower() in vowels:
      temp += "*"
    else:
      # else add the current character to the return string
      temp += character
  # return the temp string after we get out of the loop
  return temp

# Test cases
print(vowel_replace("Ivan")) # *v*n
print(vowel_replace("Becca")) # B*cc*
print(vowel_replace("")) # (empty)
print(vowel_replace(" ")) # (empty)
print(vowel_replace("aeiouy")) # ******
print(vowel_replace("qwertyuiopasdfghjklzxcvbnm")) # qw*rt****p*sdfghjklzxcvbnm
