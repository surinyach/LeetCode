class Solution {
    public int myAtoi(String s) {
       int res = 0;
       Boolean negative = false;
       Boolean number = false;

       for (int i = 0; i < s.length(); ++i) {
        char c = s.charAt(i);
        if (c == ' ' && !number) continue;
        else if (c == '+' && !number) number = true;
        else if (c == '-' && !number) {
            negative = true;
            number = true;
        }
        else if (c >= '0' && c <= '9') {
            int n = c - '0';
            if (!negative && (res > Integer.MAX_VALUE / 10 || (res == Integer.MAX_VALUE / 10 && n >= 7)))  return Integer.MAX_VALUE;
            if (negative && (res > Integer.MAX_VALUE / 10 || (res == Integer.MAX_VALUE / 10 && n >= 8))) return Integer.MIN_VALUE;
            res *= 10;
            res += n;
            number = true;
            
        }
        else break;
       } 
    
       return negative ? -res : res;
    }
}