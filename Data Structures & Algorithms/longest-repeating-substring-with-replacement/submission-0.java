class Solution {
    public int characterReplacement(String s, int k) {
        HashMap<Character, Integer> counts = new HashMap<Character, Integer>();

        int left = 0;

        int maxLen = 0;
        int maxCount = 0;

        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            counts.put(c, counts.getOrDefault(c, 0) + 1);
            maxCount = Math.max(maxCount, counts.get(c));

            int diff = (right - left + 1) - maxCount;

            if (diff > k) {
                char leftChar = s.charAt(left);
                counts.put(leftChar, counts.get(leftChar) - 1);
                left++;

            }

            // frogot Math.max portion here
            maxLen = Math.max((right - left + 1), maxLen);
        }

        return maxLen;


    }
}
