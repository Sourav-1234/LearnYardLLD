package lambdastrategy;

public class NumberTests {
    public static boolean passAll(int x) {
        return true;
    }
    public static boolean isEven(int x) {
        return x % 2 == 0;
    }

    public static boolean isOdd(int x) {
        return !isEven(x);
    }

    public static boolean isPrime(int x) {
        if(x == 2) return true;
        if(x < 3) return false;
        for(int i = 3; i*i <= x; i+=2) {
            if(x%i == 0) return false;
        }
        return true;
    }

    public static boolean isPerfectSquare(int x) {
        if(x <= 1) return true;
        int lo = 1, hi = x;
        while(lo <= hi) {
            int mid = lo + (hi-lo)/2;
            int midSquare = mid*mid;
            if(midSquare == x) return true;
            if(midSquare < x) {
                lo = mid+1;
            } else {
                hi = mid-1;
            }
        }
        return false;
    }

    public static boolean isFibonacci(int x) {
        return isPerfectSquare(5*x*x+4) || isPerfectSquare(5*x*x-4);
    }

    public static boolean isFiboAndOdd(int x) {
        return isFibonacci(x) && isOdd(x);
    }
}
