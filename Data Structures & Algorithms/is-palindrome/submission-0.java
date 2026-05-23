class Solution {
    public boolean isPalindrome(String s) {

        String newStr = s.toLowerCase().replaceAll("[^a-zA-Z0-9]", ""); 
        int index1 = 0;
        int index2 = newStr.length() - 1;

        while (index1 < index2) {
            char c1 = newStr.charAt(index1);
            char c2 = newStr.charAt(index2);
            if (c1 != c2) {
                return false;
            }

            index1++;
            index2--;
        }

        return true;
    }
}
