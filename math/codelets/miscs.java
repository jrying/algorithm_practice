import java.io.*;
import java.math.*;

class GCD {
    // GCD
    // Library
    // public BigInteger gcd(BigInteger val)
    public static int gcd(int a, int b) {
        return BigInteger.valueOf(a).gcd(BigInteger.valueOf(b)).intValue();
    }


    // Recursive

    // Iterate

    // Tester
    public static void main (String[] args)
    {
        GCD gcd = new GCD();
        assert gcd.gcd(14, 21) == 7;
        assert gcd.gcd(14, 20) == 2;
        assert gcd.gcd(14, 1) == 1;
        // System.out.println(gcd.gcd(14, 21));
        System.out.println("All passed");
    }
}
