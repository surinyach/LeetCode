import java.util.*;

class Solution {
    public String convert(String s, int numRows) {

        if (s == null) return "";
        else if (s.length() <= numRows || numRows == 1) return s;
        
        int row = 0;
        boolean diagonal = false;
        Map<Integer, List<Character>> zigzag = new HashMap<>(); 

        for (int i = 0; i < s.length(); ++i) {
           if (row == 0) diagonal = false; 
        
           zigzag.putIfAbsent(row, new ArrayList<>());
           zigzag.get(row).add(s.charAt(i));

           if (diagonal) --row;
           else ++row;

          if (row == numRows) {
            diagonal = true;
            row = numRows - 2;
           }
        }

        StringBuilder result = new StringBuilder();

        for (Integer key : zigzag.keySet()) {
            List<Character> rowList = zigzag.get(key);
            for (char c : rowList) {
            result.append(c);
            }   
        }

        String resultS = result.toString();
        System.out.println(resultS);
        return resultS;
    }
}