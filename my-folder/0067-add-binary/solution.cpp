class Solution {
 public:
  string addBinary(string a, string b) {
    // Reverse traversal
    // Time: O(n + m)
    // Space: O(n + m)

    string ans;
    int carry = 0;
    int i = a.length() - 1;
    int j = b.length() - 1;

    while (i >= 0 || j >= 0 || carry) {
      if (i >= 0)
        carry += a[i--] - '0'; // Convert bit to 0 or 1 from subtracing ASCII value 48 <-> '0' 
      if (j >= 0)
        carry += b[j--] - '0';

      ans += carry % 2 + '0'; 
      carry /= 2;
    }

    // We were doing a reversed traversal, such that we need to reverse all of the bits to see the answer
    reverse(begin(ans), end(ans));
    return ans;
  }
};
