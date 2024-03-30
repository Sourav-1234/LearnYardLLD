package lambdastrategy;

import java.util.List;

public class BadCode {
    public static int sumAll(List<Integer> nums) {
        int sum = 0;
        for(int num: nums) {
            sum += num;
        }
        return sum;
    }

    public static int sumAllOdd(List<Integer> nums) {
        int sum = 0;
        for(int num: nums) {
            if(num % 2 != 0) {
                sum += num;
            }
        }
        return sum;
    }

    public static int sumAllEven(List<Integer> nums) {
        int sum = 0;
        for(int num: nums) {
            if(num % 2 == 0) {
                sum += num;
            }
        }
        return sum;
    }

}

/*

Predicate

test which returns true or false.

Predicate<Integer> isOdd = (x) => x % 2 != 0;


isOdd.test(5)

Predicate<Object> 

(x) => x % 2 != 0;


 */