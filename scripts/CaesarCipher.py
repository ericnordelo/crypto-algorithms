def generate_key(n):
    letters = "abcdefghijklmnopqrstuvwxyz".upper()
    key = {}
    count = 0
    for c in letters:
        key[c] = letters[(count+n) % len(letters)]
        count += 1
    return key


def encrypt(key, message):
    cipher = ""
    for c in message:
        if c in key:
            cipher += key[c]
        else:
            cipher += c
    return cipher


if __name__ == "__main__":
    key = generate_key(3)
    message = "YOU ARE AWESOME"
    cipher = encrypt(key, message)
    print(cipher)
