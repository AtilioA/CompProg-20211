#include <iostream>

using namespace std;

int main()
{
    int n, m, i, a[30000];

    cin >> n >> m;
    for (i = 1; i < n; i++)
    {
        cin >> a[i];
    }

    for (i = 1; i < n;)
    {
        if (m == i || i > m)
        {
            break;
        }

        i += a[i];
    }

    if (i == m)
    {
        cout << "YES";
    }
    else
    {
        cout << "NO";
    }

    return 0;
}
