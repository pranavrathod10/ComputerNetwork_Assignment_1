def substitute_decrypt(s):
    decrypt_msg = ""
    for i in range(len(s)):
        a = ord(s[i])
        print(a)
        if(a >= ord('a') and a <= ord('z')):
            dj = chr((a - ord('a') - 2)%26 + ord('a'))
            decrypt_msg += dj
        elif(a >= ord('A') and a <= ord('Z')):
            dj = chr((a - ord('A') - 2)%26 + ord('A'))
            decrypt_msg += dj
        elif(a >= ord('0') and a <= ord('9')):
            dj = chr((a - ord('0') - 2)%10 + ord('0'))
            decrypt_msg += dj
    return decrypt_msg


def transpose_decrypt(s):
    ans = s.split(" ")

    for idx in range(0,len(ans)):
       ans[idx] = ans[idx][:: -1]

    return " ".join(ans)

def substitute_encrypt(s):
    encrypt_msg = ""
    for i in range(len(s)):
        a = ord(s[i])
        print(a)
        if(a >= ord('a') and a <= ord('z')):
            dj = chr((a - ord('a') + 2)%26 + ord('a'))
            encrypt_msg += dj
        elif(a >= ord('A') and a <= ord('Z')):
            dj = chr((a - ord('A') + 2)%26 + ord('A'))
            encrypt_msg += dj
        elif(a >= ord('0') and a <= ord('9')):
            dj = chr((a - ord('0') + 2)%10 + ord('0'))
            encrypt_msg += dj
    return encrypt_msg
print(substitute_encrypt('abdABD129'))

print(substitute_decrypt(substitute_encrypt('abdABD129')))