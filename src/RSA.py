from dataclasses import dataclass
from src.PrimeGenerator import PrimeGenerator
import binascii

@dataclass
class PublicKey:
    n : int
    e : int

@dataclass
class PrivateKey:
    n : int
    d : int

class RSA:
    def __init__(self) -> None:
        pass

    def produce_keys(self):
        generator = PrimeGenerator()

        p = generator.get_probable_prime()
        q = generator.get_probable_prime()
        n = p*q
        f = (p-1)*(q-1)
        e_generator = PrimeGenerator(3, f)
        e = e_generator.get_probable_prime()
        d = self.egcd(e, f)

        public_key = PublicKey(n, e)
        private_key = PrivateKey(n, d)

        return public_key, private_key

    def encrypte(self, public_key : PublicKey, msg : str) -> int:
        m = int(binascii.hexlify(msg.encode("utf-8")), 16)
        return pow(m, public_key.e, public_key.n)

    def decrypte(self, private_key : PrivateKey, y : int) -> str:
        m = pow(y, private_key.d, private_key.n)
        return binascii.unhexlify(format(m, "x").encode("utf-8")).decode("utf-8")


    def egcd(self, a, b):
        x,y, u,v = 0,1, 1,0
        while a != 0:
            q, r = b//a, b%a
            m, n = x-u*q, y-v*q
            b,a, x,y, u,v = a,r, u,v, m,n
            gcd = b
        return x



        