public class Solution {
    public int countNumbersWithUniqueDigits(int n) {
        // 9*9*8*7...
        if (n == 0) return 1;
        int result = 10;
        for (int i = 2; i <= n; i++) {
            int t = 9;
            for (int j = 0; j < i - 1; j++) { t *= (9 - j); }
            result += t;
        }
        return result;
    }
}
