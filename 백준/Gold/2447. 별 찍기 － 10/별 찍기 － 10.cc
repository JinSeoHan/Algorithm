#include <iostream>
using namespace std;

char star[2187][2187];

//n크기의 배열을 ' '으로 초기화한다
void Init(int n)
{
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			star[i][j] = ' ';
		}
	}
}

void FillStar(int n, int x, int y)
{
	if (n == 1)
	{
		star[x][y] = '*';
		return;
	}
	for (int i = 0; i < 3; i++)
	{
		for (int j = 0; j < 3; j++)
		{
			if (i == 1 && j == 1)
			{
				continue;
			}
			FillStar(n / 3, x + (n/3)*i, y + (n/3)*j);
		}
	}
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n;
	cin >> n;
	Init(n);
	
	FillStar(n, 0, 0);
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			cout << star[i][j];
		}
		cout << '\n';
	}
	return 0;
}