from pyDes import *


#############################################################################
# 				Examples				    #
#############################################################################
def example_16_rounds_DES():
    from time import time

    # example of DES encrypting in CBC mode with the IV of "\0\0\0\0\0\0\0\0"

    print("Example 16 Rounds DES")
    t = time()
    k = des("DESCRYPT")
    data = "DES encryption algorithm"
    print("Key      : %r" % k.getKey())
    print("Data     : %r" % data)

    d = k.encrypt(data)
    print("Encrypted: %r" % d)

    d = k.decrypt(d)
    print("Decrypted: %r" % d)
    print("DES time taken: %f (6 crypt operations)" % (time() - t))
    print("")


def example_3_rounds_DES():
    from time import time

    # example of DES encrypting in CBC mode with the IV of "\0\0\0\0\0\0\0\0"

    print("Example 3 Rounds DES")
    t = time()
    k = des("DESCRYPT", number_of_rounds=3)
    data = "DES encryption algorithm"
    print("Key      : %r" % k.getKey())
    print("Data     : %r" % data)

    d = k.encrypt(data)
    print("Encrypted: %r" % d)

    d = k.decrypt(d)
    print("Decrypted: %r" % d)
    print("DES time taken: %f (6 crypt operations)" % (time() - t))
    print("")


if __name__ == '__main__':
    example_16_rounds_DES()
    example_3_rounds_DES()