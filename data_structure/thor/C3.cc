#include <iostream>
#include <vector>
#include <utility>
using namespace std;


int main() {
    int N, Q;
    cin >> N >> Q;
    vector<vector<int> > apps (N+1, vector<int> ());
    vector<int> read(Q+1, 0);
    int unread = 0;
    int toread = 0;
    int readindex = 0;
    int k = 0;
    vector<pair<int, int> > qs;

    for (int i = 0; i < Q; i++) {
        int _ty, _x;
        cin >> _ty >> _x;
        if (_ty < 3) {
            qs.push_back(pair<int, int>(_ty, _x));
        }
        else {
            toread = _x - readindex;
            readindex = _x;
            for (int q = 0; q < qs.size(); q++) {
                int ty = qs[q].first;
                int x = qs[q].second;
                switch(ty) {
                    case 1:
                        apps[x].push_back(k);
                        unread ++;
                        k ++;
                        break;
                    case 2:
                        for (int i = 0; i < apps[x].size(); i++) {
                            unread --;
                            if (apps[x][i] < readindex) {
                                toread --;
                            }
                        }
                        apps[x].clear();
                    break;
                }
                cout << unread << endl;
            }
            cout << toread << endl;
        }
    }
    return 0;
}
