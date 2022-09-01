#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;
    int solved = 0;
    for (int i = 0; i < n; i++) {
        int sure = 0;
        for (int j = 0; j < 3; j++) {
            string p;
            cin >> p;
            if (p == "1") {
                sure++;
            }
        }
        if (sure >= 2) {
            solved++;
        }
    }
    cout << solved;
}

