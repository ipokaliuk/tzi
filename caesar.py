def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

# Приклад використання
text = "this is Caesar's code"
shift = 3
encrypted_text = caesar_cipher(text, shift)
print(f"Зашифрований текст: {encrypted_text}")
