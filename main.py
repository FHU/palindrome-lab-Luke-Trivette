#REMOVE PASS AND FIX THIS FUNCTION
def palindrome(word):
    cleaned_text = "".join(word.split()).lower()
    return cleaned_text == cleaned_text[::-1]

if __name__ == '__main__': 
    user_input = input("Enter a text: ")
    result = palindrome(user_input)
    if result:
        print("The entered text is a palindrome.")
    else:
        print("The entered text is not a palindrome.")
