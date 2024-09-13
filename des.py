from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

def des_encrypt(plain_text, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plain_text.encode(), DES.block_size)
    encrypted_text = cipher.encrypt(padded_text)
    return encrypted_text

def des_decrypt(encrypted_text, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_padded_text = cipher.decrypt(encrypted_text)
    decrypted_text = unpad(decrypted_padded_text, DES.block_size)
    return decrypted_text.decode()

# Приклад використання
key = b'8bytekey'  # Ключ має бути довжиною 8 байт
plain_text = "This is a secret message"

encrypted_text = des_encrypt(plain_text, key)
print(f"Зашифрований текст: {encrypted_text}")

decrypted_text = des_decrypt(encrypted_text, key)
print(f"Розшифрований текст: {decrypted_text}")
