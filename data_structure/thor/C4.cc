#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int N, Q;
    cin >> N >> Q;
    vector<vector<int> > apps (N+1, vector<int> ());
    vector<int> read(Q+1, 0);
    int unread = 0;
    int readindex = 0;
    int k = 0;
    for (int i = 0; i < Q; i++) {
        int ty, x;
        cin >> ty >> x;
        switch(ty) {
            case 1:
                apps[x].push_back(k);
                unread ++;
                k ++;
                break;
            case 2:
                for (int i = 0; i < apps[x].size(); i++) {
                    if (read[apps[x][i]] == 0) {
                        unread --;
                        read[apps[x][i]] = 1;
                    }
                }
                apps[x].clear();
                break;
            case 3:
                if (readindex - k > k - x) {
                    int toread = 0;
                    for (int i = readindex; i < x; i++) {
                        toread ++;
                    }
                    unread -= toread;
                }
                else {
                    for (int i = readindex; i < x; i++) {
                        if (read[i] == 0) {
                            unread --;
                        }
                    }
                }
                readindex = x;
                break;
        }
        cout << unread << endl;
    }
    return 0;
}
