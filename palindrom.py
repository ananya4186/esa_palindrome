def is_palindrome(text):
    return text == text[::-1]

if __name__ == "__main__":
    text = input("Enter a text: ")

    if is_palindrome(text):
        print("Yes, it is palindrome")
    else:
        print("No, it is not palindrome")
