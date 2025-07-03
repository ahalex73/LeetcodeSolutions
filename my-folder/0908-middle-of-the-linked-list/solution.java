/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode middleNode(ListNode head) {
        int length = 0;
        ListNode current = head;

        // Find the length of the linked list
        while(current != null){
            length ++;
            current = current.next;
        }

        // Divide the length in half and traverse from the middle point
        int middle_index = length / 2;
        current = head;
        for (int i = 0; i < middle_index; i++) {
            current = current.next;
        }

        return current;
    }
}
