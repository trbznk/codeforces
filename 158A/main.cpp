#include <iostream>

using namespace std;

int main() {
    int n, k;
    int min_score = 1;
    int count = 0;

    cin >> n;
    cin >> k;
    k--;

    for (int i = 0; i < n; i++) {
       int p;
       cin >> p;
       if (p < min_score) {
           break;
       } 
       if (i == k) {
           min_score = p;
       }
       count++;
    }
    cout << count << endl;
}

