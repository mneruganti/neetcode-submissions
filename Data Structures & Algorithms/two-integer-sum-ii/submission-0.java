class Solution {
    public int[] twoSum(int[] numbers, int target) {

       // We start by making two indicies - a left and right to track two ends of the array
       // we are going for a classic two pointer approach
        int left_ind = 0;
        int right_ind = numbers.length - 1;
        int[] results = new int[2];

        // the left index starts at the smaller end of the array
        // the right index starts at the bigger end of the array
        while (left_ind < right_ind) {
            
            // left and right pointers updated after every iteration
            int left = numbers[left_ind];
            int right = numbers[right_ind];

            if (left + right > target) {
                right_ind--;
            }
            else if (left + right < target) {
                left_ind++;
            }
            else {
                results[0] = left_ind + 1;
                results[1] = right_ind + 1;
                break;
            }

        }

        return results;
        
    }
}
