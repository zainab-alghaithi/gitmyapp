find_vowel= input("write a sentence:")
vowels= "aeiouAEIOU"
vowel_count = 0 

if find_vowel == "":
        print("invalid input please enter a sentence")
else:
    for i in  find_vowel:
        if  i in vowels:
         vowel_count += 1  # Increment vowel count 

    if vowel_count > 0:
         print (f"the vowels in the sentence are {vowel_count }")
    else:
        print("There are no vowels in the sentence")
