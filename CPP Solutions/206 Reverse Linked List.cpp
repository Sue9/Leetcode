#include <iostream>
using namespace std;
/**
 * Definition for singly-linked list.
 *  */
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

ListNode* createLinkedList(int arr[], int n){
    if( n == 0 )
        return NULL;

    ListNode* head = new ListNode(arr[0]);
    ListNode* cur = head;
    for(int i = 1; i < n; i++){
        cur->next = new ListNode(arr[i]);
        cur = cur->next;
    }

    return head;
}


void printLinkedList(ListNode* head){
    ListNode* cur = head;
    while(cur != NULL){
        cout << cur->val <<" -> ";
        cur = cur->next;
    }
    cout<<"NULL"<<endl;
    return;
}


void deleteLinkedList(ListNode* head){
    ListNode* cur = head;
    while( cur != NULL ){
        ListNode* delNode = cur;
        cur = cur->next;
        delete delNode;
    }
}

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* pre = NULL;
        ListNode* cur = head;
        while(cur != NULL){
            ListNode* next = cur->next;
            cur->next = pre;
            pre = cur;
            cur = next;
        }
        return pre;
    }
};
int main() {
    int arr[] = {1,2,3,4,5};
    int n = sizeof(arr) / sizeof(int);

    ListNode* head = createLinkedList(arr, n);
    printLinkedList(head);

    ListNode* head2 = Solution().reverseList( head );
    printLinkedList(head2);

    deleteLinkedList(head2);

    return 0;
}