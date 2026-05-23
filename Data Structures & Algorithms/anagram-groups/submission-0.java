class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        
        HashMap<String, List<String>> results = new HashMap<>();

        // create an array of 0-26 for each string to represent 
        // its letter frequency
        
        for (String word: strs) {
            int[] freq = new int[26];
            
            // Convert each word into a character array which basically
            // makes it so we can access each individual letter of every word
            for (char letter: word.toCharArray()) {

                // we do the letter minus the unicode of a to get the index that needs to be
                // incremented, and we increment it to 1 to indicate that letter is there
                freq[letter - 'a']++;
            }

            // now we will build a string that will be the key for the hashmap that represents
            // the frequency array in string form for easy comparison
            StringBuilder keyBuilder = new StringBuilder();
            for (int i = 0; i < 26; i++) {
                keyBuilder.append("#");
                keyBuilder.append(freq[i]);
            }

            // String builder makes the string mutables and .toString() reverses it back to an 
            // immutable string
            String key = keyBuilder.toString();

            // this basically puts a key into the map, and adds the word to the element list
            // if the key does not exist, it makes a new entry 
            results.computeIfAbsent(key, k -> new ArrayList<>()).add(word);
        }

        // return a list of the elements of the hashmap.
        return new ArrayList<>(results.values());
    }
}
