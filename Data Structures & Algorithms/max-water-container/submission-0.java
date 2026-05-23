class Solution {
    public int maxArea(int[] heights) {
        // two pointer approach?

        int left_ind = 0;
        int right_ind = heights.length - 1;
        int maxArea = 0;
        int currArea = 0;

        while (left_ind < right_ind) {
            int left = heights[left_ind];
            int right = heights[right_ind];

            currArea = (right_ind - left_ind) * Math.min(left, right);

            if (Math.min(left, right) == left) {
                left_ind++;
            }
            else {
                right_ind--;
            }
            
            if (currArea > maxArea) {
                maxArea = currArea;
            }
        }

        return maxArea;
    }
}
