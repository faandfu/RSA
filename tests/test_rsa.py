from src.RSA import RSA
import pytest


def test_rsa():
    rsa = RSA()
    public_key, private_key = rsa.produce_keys()

    msg = "VerschlüsselterText"
    y = rsa.encrypte(public_key, msg)
    z = rsa.decrypte(private_key, y)
    assert msg == z
