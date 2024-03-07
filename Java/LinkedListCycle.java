import java.util.HashMap;

// Definition for singly-linked list.
class ListNode {
    int val;
    ListNode next;
    ListNode(int x) {
        val = x;
        next = null;
    }
}

public class LinkedListCycle {
    public static boolean hasCycle(ListNode head) {
        HashMap<ListNode, Boolean> passed = new HashMap<ListNode, Boolean>();
        while (true){
            if (head == null || head.next == null) {
                return false;
            }
            if (passed.get(head) == null){
                passed.put(head, true);
                head = head.next;
            } else {
                return true;
            }
        }
    }

    public static void main(String[] args){
        ListNode test = new ListNode(0);
        test.next = new ListNode(1);
        // test.next.next = test;

        System.out.println(hasCycle(test));
    }
}
