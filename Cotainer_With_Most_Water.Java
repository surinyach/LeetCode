import java.util.*;

class Solution {
    public int maxArea(int[] height) {
        int water = 0;
        List<Integer> biggests = new ArrayList<>();
        int left = 0;
        
        for (int i = 1; i < height.length; ++i) {
            int nWater = Math.min(height[left], height[i]) * (i - left);
            if (nWater > water) water = nWater;
            if (height[i] > height[left]) biggests.add(i);
            for (int pos : biggests) {
                if (i != pos) {
                    int bigWater = Math.min(height[pos], height[i]) * (i - pos);
                    if (bigWater > water) {
                        water = bigWater;
                        left = pos; 
                    }
                } 
            }
        }
        return water;
    }
}