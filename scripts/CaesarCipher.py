def generate_key(n):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = {}
    cnt = 0
    for c in letters:
        key[c] = letters[(cnt + n) % len(letters)]
        cnt += 1
    return key


def get_decryption_key(n):
    return generate_key(26-n)


def encrypt(key, message):
    cipher = ""
    for c in message:
        if c in key:
            cipher += key[c]
        else:
            cipher += c
    return cipher


key = generate_key(3)
message = "YOU ARE AWESOME"
cipher = encrypt(key, message)
print(cipher)
dkey = get_decryption_key(3)
message = encrypt(dkey, cipher)
print(message)
