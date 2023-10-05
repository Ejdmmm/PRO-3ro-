## matematicky c = (x + n) % 26 
## encode decode
## google pomohl, sam jsem to neudelal cele
def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr(((ord(char) - ord('a') + shift) % 26) + ord('a')) ## chr vestavena fc vraci retezec
            else:
                encrypted_text += chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text
shift = 3  # pocet pozic pro posunuti, můžu napsat kolik chci, aby se to posunulo a vyšly jiny cisla
text= str(input("Enter text to ecrypt: "))
def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)
encrypted_text = caesar_encrypt(text, shift)
print("Encrypted text:", encrypted_text)

decrypted_text = caesar_decrypt(encrypted_text, shift)
print("Decrypted text:", decrypted_text)