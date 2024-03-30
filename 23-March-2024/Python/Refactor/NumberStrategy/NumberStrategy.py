class NumberStrategy:
    def pass_all(x):
        return True

    def is_even(x):
        return x % 2 == 0

    def is_odd(x):
        return not NumberStrategy.is_even(x)

    def is_prime(x):
        if x == 2:
            return True
        if x < 2 or x % 2 == 0:
            return False
        for i in range(3, int(x**0.5) + 1, 2):
            if x % i == 0:
                return False
        return True

    def is_perfect_square(x):
        if x <= 1:
          return True
        lo, hi = 1, x
        while lo <= hi:
            mid = (lo + hi) // 2
            mid_square = mid * mid
            if mid_square == x:
                return True
            elif mid_square < x:
                lo = mid + 1
            else:
                hi = mid - 1
            return False

    def is_fibonacci(x):
        return NumberStrategy.is_perfect_square(5 * x * x + 4) or NumberStrategy.is_perfect_square(5 * x * x - 4)

    def is_fibo_and_odd(x):
        return NumberStrategy.is_fibonacci(x) and NumberStrategy.is_odd(x)
