#implements OTP

import binascii


def dec(x):
    with open("input.txt", "r") as f:
        text = f.read()
        binary_text = binascii.unhexlify(text)
        binary_key = binascii.unhexlify(x)
        i =

    print(binary_key + binary_text)


dec("84A837C9D374AD")