a = 3
b = 5
m = 64

def cipher(x):

    y = (ord(x)*a + b) % 64
    return y

def decrypt(x):
    y = (modInverse(3,64) * (ord(x) - 5)) % 64
    return y
def modInverse(a, m):
    for x in range(1, m):
        if (((a%m) * (x%m)) % m == 1):
            return x
    return -1

# Driver Code

# m diganti ato dibatesin
# Function call
print(cipher("a"))
print(decrypt("("))