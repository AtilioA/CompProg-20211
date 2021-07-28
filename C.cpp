#include <iostream>
#include <vector>
#include <queue>
#include <limits>

using namespace std;

priority_queue<int, vector<int>, greater<int>> pq;
int operations = 0;
string inputString;

void insert(int x)
{
    pq.push(x);
    inputString.append("insert " + to_string(x) + "\n");
    operations++;
}

int removeMin()
{
    int x;
    if (pq.size())
    {
        x = pq.top();
        pq.pop();

        inputString.append("removeMin\n");

        operations++;
    }
    else
    {
        insert(0);
        removeMin();
    }
    return x;
}

void getMin(int x)
{
    if (pq.size() && pq.top() == x)
    {
        inputString.append("getMin " + to_string(x) + "\n");
        operations++;
        return;
    }

    int c = numeric_limits<int>::min();

    while (pq.size())
    {
        if (pq.top() == x)
        {
            getMin(x);
            return;
        }
        else if (pq.top() > x)
        {
            insert(x);
            inputString.append("getMin " + to_string(x) + "\n");
            operations++;

            return;
        }
        else
        {
            removeMin();
        }
    }

    insert(x);
    inputString.append("getMin " + to_string(x) + "\n");
    operations++;
}

void doOperation(string operation)
{
    int x;
    switch (operation[0])
    {
    case 'i':
        cin >> x;
        insert(x);
        break;
    case 'g':
        cin >> x;
        getMin(x);
        break;
    case 'r':
        removeMin();
        break;
    }
}

int main()
{

    int n;
    string operation;

    cin >> n;

    for (int i = 0; i < n; i++)
    {
        cin >> operation;
        doOperation(operation);
    }

    cout << operations << endl;
    cout << inputString.substr(0, inputString.length() - 1) << endl;

    return 0;
}
