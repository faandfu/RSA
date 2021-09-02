from dataclasses import dataclass
from src.PrimeGenerator import PrimeGenerator
import binascii


@dataclass
class PublicKey:
    n: int
    e: int


@dataclass
class PrivateKey:
    n: int
    d: int


class RSA:
    def __init__(self) -> None:
        pass

    def produce_keys(self):
        generator = PrimeGenerator()

        p = generator.get_probable_prime()
        q = generator.get_probable_prime()
        n = p * q
        f = (p - 1) * (q - 1)
        e_generator = PrimeGenerator(3, f)
        e = e_generator.get_probable_prime()
        d = self.get_mult_inverse(e, f)

        public_key = PublicKey(n, e)
        private_key = PrivateKey(n, d)

        return public_key, private_key

    def encrypte(self, public_key: PublicKey, msg: str) -> int:
        m = int(binascii.hexlify(msg.encode("utf-8")), 16)
        return pow(m, public_key.e, public_key.n)

    def decrypte(self, private_key: PrivateKey, y: int) -> str:
        m = pow(y, private_key.d, private_key.n)
        return binascii.unhexlify(format(m, "x").encode("utf-8")).decode("utf-8")

    def get_mult_inverse(self, a:int, b:int) -> int:
        """
        returns the multiplicative inverse of a mod b (using the extended euclidean algorithm).
        """
        x = 0
        y = 1
        u = 1
        v = 0
        while a != 0:
            q = b // a
            r = b % a
            m = x - u * q
            n = y - v * q
            b = a
            a = r
            x = u
            y = v
            u = m
            v = n
        return x
