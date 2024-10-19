# count_vowels.py
def count_vowels_and_consonants(s):
    vowels = set("aeiouAEIOU")
    consonants_count = 0
    vowels_count = 0

    for char in s:
        if char.isalpha():  # Check if the character is a letter
            if char in vowels:
                vowels_count += 1
            else:
                consonants_count += 1

    return vowels_count, consonants_count

if __name__ == "__main__":
    string = input("Enter a string: ")
    vowels_count, consonants_count = count_vowels_and_consonants(string)
    print(f"Number of vowels: {vowels_count}")
    print(f"Number of consonants: {consonants_count}")
