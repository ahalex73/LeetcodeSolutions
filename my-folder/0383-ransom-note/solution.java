class Solution {
    // Hashmap solution
    // Time: O(m) - Number of letters in magazin
    // Space: O(1) - Number of distinct letters in magazine (up to 26) such that its O(n) time but simplifies to O(1)

    public boolean canConstruct(String ransomNote, String magazine) {
        // Iterate over the ransomNote to see what letters we need
        if (magazine.length() < ransomNote.length()) {
            return false;
        }

        HashMap<Character, Integer> magazineLetters = new HashMap<>();


        for(int i = 0; i < magazine.length(); i++){
            char m = magazine.charAt(i);

            int currentCount = magazineLetters.getOrDefault(m, 0);
            magazineLetters.put(m, currentCount + 1);
        }

        // Time bounded by m letters in magazine dictionary
        for(int i = 0; i < ransomNote.length(); i ++){
            char r = ransomNote.charAt(i);

            int currentCount = magazineLetters.getOrDefault(r, 0);

            if (currentCount == 0) {
                return false;
            }
            magazineLetters.put(r, currentCount - 1);
        }


        return true;
    }
}
