# Python program: String Reversal and Palindrome Checker
# Date: 2026-08-28

def reverse_string(s: str) -> str:
    return s[::-1]

def is_palindrome(s: str) -> bool:
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    test_str = "Radar"
    print(f"Original: {test_str}")
    print(f"Reversed: {reverse_string(test_str)}")
    print(f"Is Palindrome: {is_palindrome(test_str)}")
