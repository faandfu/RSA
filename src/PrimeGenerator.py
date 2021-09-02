import random


class PrimeGenerator:
    def __init__(
        self,
        start: int = pow(10, 28),
        end: int = pow(10, 32),
        repetitions: int = 10,
    ) -> None:
        """
        params
        start: range start for primes
        end: range end for primes
        repetitions: number of miller rabin repetitions
        """
        self.start = start
        self.end = end
        self.repetitions = repetitions

    def get_probable_prime(self) -> int:
        n = self.get_random_number()
        while not self.is_prime(n):
            n = self.get_random_number()
        return n

    def miller_rabin(self, n: int) -> bool:
        d = n - 1
        k = 0
        while d % 2 == 0:
            d = d >> 1
            k += 1

        a = random.randint(2, n - 1)

        for i in range(k + 1):
            e = d * 2 ** (k - i)
            result = pow(a, e, n)
            if result != 1:
                if result != n - 1:
                    return False
                break
        return True

    def is_prime(self, n: int) -> bool:
        for _ in range(self.repetitions):
            if not self.miller_rabin(n):
                return False
        return True

    def get_random_number(self) -> int:
        return random.randint(self.start, self.end)
