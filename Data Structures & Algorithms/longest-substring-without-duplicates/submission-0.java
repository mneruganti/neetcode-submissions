class Solution {
    public int lengthOfLongestSubstring(String s) {

        if (s.isEmpty()) {
            return 0;
        }

        // Hashset blocks duplicates and allows you to keep track
        // of characters after traversing them
        HashSet<Character> set = new HashSet<>();

        // left pointer
        int left = 0;

        // max length of longest substring
        int maxLen = 0;

        for (int right = 0; right < s.length(); right++) {
            // get each character of the string
            char c = s.charAt(right);

            while (set.contains(c)) {
                set.remove(s.charAt(left));
                left++;
            }

            set.add(c);
            maxLen = Math.max(maxLen, right - left + 1);
        }

        return maxLen;

        
    }
}
