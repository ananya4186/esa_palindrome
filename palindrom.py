def is_palindrome(text):
    if text == text[::-1]:
        print(f"{text} is palindrome")
        return True
    else:
        print(f"{text} is not palindrome")
        return False

if __name__ == "__main__":
    text = input("Enter a text: ")
    is_palindrome(text)
