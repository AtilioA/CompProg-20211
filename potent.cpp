#include <stdio.h>

#define MAX_POTENTIOMETERS 200005

int data[MAX_POTENTIOMETERS], tree[4 * MAX_POTENTIOMETERS], par[MAX_POTENTIOMETERS];

// Segtree implementation --------------------------------
void build(int node, int start, int finish)
{
    if(start == finish)
    {
        tree[node] = data[start];
        par[start] = node;
    }
    else
    {
        int mid = (start + finish) / 2;

        build(node * 2, start, mid);
        build(node * 2 + 1, mid + 1, finish);

        tree[node] = tree[node * 2] + tree[node * 2 + 1];
    }
}

int query(int node, int start, int finish, int left, int right)
{
    if (right < start || left > finish)
    {
        return 0;
    }

    if (start >= left && finish <= right) {
        return tree[node];
    }

    int mid = (start + finish) / 2;

    return (query(node * 2, start, mid, left, right) + query((node * 2+1), mid+1, finish, left, right));
}

void update(int place, int val)
{
    int node = par[place];

    tree[node] = val;

    node = node / 2;

    while (node)
    {
        tree[node] = tree[node * 2] + tree[node * 2 + 1];
        node = node / 2;
    }
}
// --------------------------------

int main()
{
    int n, i, cases = 0;
    while(scanf("%d",&n)&&n)
    {
        // Blank line between cases
        if (cases) {
            printf("\n");
        }

        printf("Case %d:\n", ++cases);

        // Read potentiometers
        for(i = 1; i <= n; i++) {
            scanf("%d", &data[i]);
        }

        build(1, 1, n);

        // Read operations
        char op[10];
        while(scanf("%s", op))
        {
            // END
            if (op[0] == 'E')
            {
                break;
            }

            int value1 = -1, value2 = -1;
            scanf("%d %d", &value1, &value2);
            if(op[0] == 'M') // Measure
            {
                printf("%d\n",query(1, 1, n, value1, value2));
            }
            else // Set
            {
                update(value1,value2);
            }
        }
    }

    return 0;
}
