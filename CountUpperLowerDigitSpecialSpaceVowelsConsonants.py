def CountUpperLowerDigitSpecialSpaceVowelsConsonants():
    s=input("enter a sentence")
    upper_count=0
    lower_count=0
    space_count=0
    vowel_count=0
    digit_count=0
    for ch in s:
        if ch.isupper():
            upper_count+=1
        elif ch.islower():
            lower_count+=1
        elif ch.isdigit():
            digit_count+=1
        elif ch.isspace():
            space_count+=1
        if ch in 'aeiouAEIOU':
            vowel_count+=1
    print("uppercase letters:",upper_count)
    print("lowercase letters:",lower_count)
    print("digit:",digit_count)
    print("space:",space_count)
    print("vowel:",vowel_count)
    print("consonant:",upper_count+lower_count-vowel_count)
    print("special character:",len(s)-(upper_count+lower_count+digit_count+space_count))
CountUpperLowerDigitSpecialSpaceVowelsConsonants()
