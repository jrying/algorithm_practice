#include <iostream>
#include <vector>
#include <set>
using namespace std;

int main() {
    int N, Q;
    cin >> N >> Q;
    vector<set<int> > apps (N+1, set<int> ());
    vector<int> read(Q+1, 0);
    int unread = 0;
    int readindex = 0;
    int k = 0;
    for (int i = 0; i < Q; i++) {
        int ty, x;
        cin >> ty >> x;
        switch(ty) {
            case 1:
                apps[x].insert(k);
                read[k] = x;
                unread ++;
                k ++;
                break;
            case 2:
                for (int i : apps[x]) {
                    unread --;
                    read[i] = 0;
                }
                apps[x].clear();
                break;
            case 3:
                for (int i = readindex; i < x; i++) {
                    if (read[i] > 0) {
                        apps[read[i]].erase(i);
                        read[i] = 0;
                        unread --;
                    }
                }
                readindex = x;
                break;
        }
        cout << unread << endl;
    }
    return 0;
}
