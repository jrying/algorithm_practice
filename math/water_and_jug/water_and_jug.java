import java.math.*;
public class Solution {
    public static int gcd(int a, int b) {
        return BigInteger.valueOf(a).gcd(BigInteger.valueOf(b)).intValue();
    }
    public boolean canMeasureWater(int x, int y, int z) {
        return x + y + z == 0 || (z <= x + y && z % gcd(gcd(x, y), Math.abs(x-y)) == 0);
    }
}
