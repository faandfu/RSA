from src.PrimeGenerator import PrimeGenerator
import pytest

def test_primes():
    generator = PrimeGenerator()
    prime = generator.get_probable_prime()
    assert generator.miller_rabin(prime)