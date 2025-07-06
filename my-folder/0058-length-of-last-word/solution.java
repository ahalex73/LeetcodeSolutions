class Solution {
    public int lengthOfLastWord(String s) {    
        // Time: O(n)
        // Space: O(1)

        int length_of_last_word = 0;
        int i = s.length() - 1;

        // Skip trailing spaces
        while (i >= 0 && s.charAt(i) == ' ') {
            i--;
        }

        // Count characters until next space or beginning of string
        while (i >= 0 && s.charAt(i) != ' ') {
            length_of_last_word++;
            i--;
        }

        return length_of_last_word;
    }
}

