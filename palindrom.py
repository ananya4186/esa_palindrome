def is_palindrome(text):
    return text == text[::-1]

if __name__ == "__main__":
    text = input()
    print(is_palindrome(text))
