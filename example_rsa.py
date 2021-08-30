from src.RSA import RSA

rsa = RSA()



for _ in range(1000):
    public_key, private_key = rsa.produce_keys()

    msg = "VerschlüsselterText"
    y = rsa.encrypte(public_key, msg)

    z = rsa.decrypte(private_key, y)
    print(msg, y, z)

