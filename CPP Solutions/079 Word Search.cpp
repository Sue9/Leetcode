#include <iostream>
#include <vector>
#include <cassert>
using namespace std;

class Solution {
private:
    int d[4][2] = {
            {-1, 0}, //up
            {0, 1},  //right
            {1, 0},  //down
            {0, -1}  //left
    };

    int m,n;
    vector<vector<bool>> visited;

    bool inArea(int x, int y){
        return x >= 0 && x < m && y >= 0 && y < n;
    }
    //search word[index..word.size()), from board[startx][starty]
    bool searchWord(const vector<vector<char>>& board, const string& word, int index, int startx, int starty){
        if(index == word.size()-1){
            return word[index] == board[startx][starty];
        }

        if( board[startx][starty] == word[index]){
            visited[startx][starty] = true;
            // start from startx, starty
            // search on four directions
            for(int i = 0; i < 4; i++){
                int newx = startx + d[i][0];
                int newy = starty + d[i][1];

                //check validation of newx & newy
                //check if has visited
                if(inArea(newx, newy) && !visited[newx][newy]){
                    if(searchWord(board, word, index + 1, newx, newy))
                        return true;
                }


            }
            visited[startx][starty] = false;
        }

        return false;
    }

public:
    bool exist(vector<vector<char>>& board, string word) {
        //m: row
        m = board.size();
        //n: column
        assert( m > 0);
        n = board[0].size();
        visited = vector<vector<bool>>(m, vector<bool>(n, false));

        for(int i = 0; i < board.size(); i++){
            for(int j = 0; j < board[i].size(); j++){
                if(searchWord(board, word, 0, i, j))
                    return true;
            }
        }
        return false;
    }
};

int main() {
    vector<vector<char>> board;
    char a[4] = {'A', 'B', 'C', 'E'};
    char b[4] = {'S', 'F', 'C', 'S'};
    char c[4] = {'A', 'D', 'E', 'E'};
    vector<char> va(a, a+4);
    vector<char> vb(b, b+4);
    vector<char> vc(c, c+4);
    board.push_back(va);
    board.push_back(vb);
    board.push_back(vc);

    string words = "ABCCED";

    bool res = Solution().exist(board, words);
    cout << "Result is : " << res << endl;

    return 0;
}