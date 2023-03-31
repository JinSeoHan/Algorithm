#include <iostream>
using namespace std;

int matrix[101][101] = {0, };

void checkPosition(int x, int y);
int findResult(int x, int y);

int main() {

    int x = 1, y = 1;
    int count = 0;
    cin >> count;

    int dupliCount = 0;

    for (int i = 0; i < count; i++)
    {
        cin >> x >> y;
        checkPosition(x, y);
    }
    cout << findResult(x, y);
}

void checkPosition(int x, int y) {
    for (int i = x; i < x+10; i++)
    {
        for (int j = y; j < y+10; j++)
        {   
            matrix[i][j] = 1;
        }
    }
}

int findResult(int x, int y) {
    int count = 0;
    for (int i = 1; i <= 100; i++)
    {
        for (int j = 1; j <= 100; j++)
        {
            if (matrix[i][j] == 1) count++;
        }
    }
    return count;
}