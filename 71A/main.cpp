#include <iostream>
#include <string>

using namespace std;

int main() {
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        string word;
        cin >> word;
        if (word.size() > 10) {
            string word_sub = word.substr(1, word.size()-2);
            cout << word.front() << word_sub.size() << word.back() << endl;
        } else {
            cout << word << endl;
        }
    }
}
