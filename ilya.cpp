#include <iostream>

using namespace std;

#define LIMIT 100000

int main()
{
    string s;
    int m, l, r, arr[LIMIT];

    cin >> s >> m;

    for (int i = 1; i < s.size(); i++)
    {
        arr[i + 1] = arr[i] + (s[i] == s[i - 1]);
    }

    for (int i = 1; i <= m; i++)
    {
        cin >> l >> r;
        cout << arr[r] - arr[l] << endl;
    }
}
