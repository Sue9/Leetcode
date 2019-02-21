#include <iostream>
#include <cassert>
#include <vector>

using namespace std;

class Solution {
private:
    const string letterMap[10] = {
            " ",    //0
            "",     //1
            "abc",  //2
            "def",  //3
            "ghi",  //4
            "jkl",  //5
            "mno",  //6
            "pqrs", //7
            "tuv",  //8
            "wxyz"  //9
    };

    vector<string> res;

    // s saved a string created from digits[0..index-1]
    // find the corresponding alphabet to the digit[index]
    void findCombination(const string &digits, int index, const string &s){
        if(index == digits.size()){
            //save s
            res.push_back(s);
            std::cout << "\t\t push_result: "<< s << std::endl;
            return;
        }
        char c = digits[index];
        assert( c >= '0' and c <= '9' and c!= '1');
        string letters = letterMap[c - '0'];
        for(int i = 0; i < letters.size(); i++){
            std::cout << "i = " << i << std::endl;
            std::cout << "\t s = "<< s << "\t s+letters[i]" << s+letters[i]<< std::endl;

            findCombination(digits, index+1, s + letters[i]);
        }
        return;
    };

public:
    vector<string> letterCombinations(string digits) {
        res.clear();
        if(digits == "")
            return res;
        findCombination(digits, 0, "");
        return res;
    }
};

int main() {
    string l= "234";
    vector<string> res = Solution().letterCombinations(l);
    for(int i = 0; i < res.size(); i++){
        cout<<res[i]<<endl;
    }
    return 0;
}