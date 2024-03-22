def vernam_encrypt(plaintext, key):
    # Tekshirish: Matn va kalit so'zning uzunliklari bir xil bo'lishi kerak
    if len(plaintext) != len(key):
        raise ValueError("Matn va kalit so'z uzunliklari bir xil bo'lishi kerak")

    # Matn va kalit so'zni bitlarga ajratamiz
    plaintext_bits = [format(ord(char), '08b') for char in plaintext]
    key_bits = [format(ord(char), '08b') for char in key]

    # XOR amalini bajarib, shifrlangan matnni olish
    encrypted_bits = [format(int(plain_bit, 2) ^ int(key_bit, 2), '08b') for plain_bit, key_bit in
                      zip(plaintext_bits, key_bits)]

    # Shifrlangan matndan chiqishni olish
    encrypted_text = ''.join([chr(int(bit, 2)) for bit in encrypted_bits])

    return encrypted_text


# Matn va kalit so'zni o'rnating
plaintext = "INTERP"
key = "OTOTOT"

# Shifrlash vaqti
encrypted_text = vernam_encrypt(plaintext, key)

# Natijani chop etish
print(f"Matn: {plaintext}")
print(f"Kalit so'z: {key}")
print(f"Shifrlangan matn: {encrypted_text}")


def vernam_decrypt(encrypted_text1, key):
    # Tekshirish: Matn va kalit so'zning uzunliklari bir xil bo'lishi kerak
    if len(encrypted_text1) != len(key):
        raise ValueError("Matn va kalit so'z uzunliklari bir xil bo'lishi kerak")

    # Shifrlangan matn va kalit so'zni bitlarga ajratamiz
    encrypted_bits = [format(ord(char), '08b') for char in encrypted_text1]
    key_bits = [format(ord(char), '08b') for char in key]

    # XOR amalini bajarib, asl matnni olish
    decrypted_bits = [format(int(encrypted_bit, 2) ^ int(key_bit, 2), '08b') for encrypted_bit, key_bit in
                      zip(encrypted_bits, key_bits)]

    # Asl matndan chiqishni olish
    decrypted_text = ''.join([chr(int(bit, 2)) for bit in decrypted_bits])

    return decrypted_text


# Shifrlangan matn va kalit so'zni o'rnating
# encrypted_text = ""
# key = "OTOTOT"
