#include <iostream>
#include <vector>
#include <list>
using namespace std;

int main() {
    int N, Q;
    cin >> N >> Q;
    vector<list<int> > apps (N+1, list<int> ());
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
                unread -= apps[x].size();
                apps[x].clear();
                break;
            case 3:
                for (int i = 1; i < N+1; i++) {
                    while (apps[x].size() > 0 && apps[x].front() < x) {
                        // TODO: bs
                        unread -= 1;
                        apps[x].pop_front();
                    }
                }
                break;
        }
        cout << unread << endl;
    }
    return 0;
}
