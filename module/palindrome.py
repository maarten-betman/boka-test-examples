def is_palindrome(in_: str):
    string_cleaned = in_.strip().lower().replace(" ","")
    return string_cleaned == string_cleaned[::-1]
