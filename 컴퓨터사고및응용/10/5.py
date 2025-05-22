key = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(n, plaintext):
    result = ''
    for l in plaintext.lower():
        try:
            i = (key.index(l) + n) % 26
            result += key[i]
        except ValueError:
            result += l
    return result.lower()

def decrypt(n, ciphertext):
    result = ''
    
    for l in ciphertext:
        try:
            i = (key.index(l) - n) % 26
            result += key[i]
        except ValueError:
            result += l
    
    return result

n = 3
text = 'The language of truth is simple.'
encrypted = encrypt(n, text)
decrypted = decrypt(n, encrypted)
print('평문: ', text)
print('암호문: ', encrypted)
print('복호문: ', decrypted)

