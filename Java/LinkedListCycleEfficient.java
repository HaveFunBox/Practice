import java.util.HashSet;

// Definition for singly-linked list.
class ListNode {
    int val;
    ListNode next;
    ListNode(int x) {
        val = x;
        next = null;
    }
}

public class LinkedListCycleEfficient {
    public static boolean hasCycle(ListNode head) {
        HashSet<ListNode> passed = new HashSet<ListNode>();
        while (head != null){
            if (!passed.contains(head)){
                passed.add(head);
                head = head.next;
            } else {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args){
        ListNode test = new ListNode(0);
        test.next = new ListNode(1);
        test.next.next = test;

        System.out.println(hasCycle(test));
    }
}
