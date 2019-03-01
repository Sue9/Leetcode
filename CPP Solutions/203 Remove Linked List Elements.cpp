#include <iostream>


//Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        ListNode* dummyHead = new ListNode(0);
        dummyHead->next = head;

        ListNode* cur = dummyHead;
        while(cur->next != NULL){
            if(cur->next->val == val){
                cur->next = cur->next->next;
            }
            else
                cur = cur->next;
        }

        ListNode* retNode = dummyHead->next;
        delete(dummyHead);
        return retNode;

    }
};

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}