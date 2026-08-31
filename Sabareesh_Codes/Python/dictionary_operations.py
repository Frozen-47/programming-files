# Python program: Dictionary Word Frequency Counter and Aggregation
# Date: 2026-08-31

def count_word_frequency(text: str) -> dict:
    words = text.lower().split()
    freq = {}
    for w in words:
        cleaned = ''.join(c for c in w if c.isalnum())
        if cleaned:
            freq[cleaned] = freq.get(cleaned, 0) + 1
    return freq

if __name__ == "__main__":
    sample = "CodeHarbour daily practice code and algorithms practice for students"
    print("Word Frequencies:", count_word_frequency(sample))
