#include <iostream>
#include <vector>

using namespace std;

class Solution {
private:
    vector<vector<int>> res;
    // Find solutions of C(n, k)
    // all possible solutions are stored in c
    // we need to find new element from number 'start'
    void generateCominations(int n, int k, int start, vector<int> &c){
        if(c.size() == k){
            res.push_back(c);
            return;
        }

        // there are still k - c.size() place
        // the maximum value of i is: n - (k - c.size()) + 1
        for(int i = start; i <= n - (k - c.size()) + 1; i++){
            c.push_back(i);
            generateCominations(n, k, i+1, c);
            c.pop_back();
        }
        return;
    }
public:
    vector<vector<int>> combine(int n, int k) {
        res.clear();
        if(n <= 0 || k <= 0 || k > n)
            return res;

        vector<int> c;
        generateCominations(n, k, 1, c);
        return res;

    }
};
int main() {

    return 0;
}