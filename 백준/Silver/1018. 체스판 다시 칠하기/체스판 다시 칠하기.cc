#include <iostream>
#include <string.h>
using namespace std;

int Find(int check[][50], int idxN, int idxM)
{
	int compare = 1;
	int count = 0;
	for (int i = idxN; i < idxN+8; i++)
	{
		for (int j = idxM; j < idxM+8; j++)
		{
			if (check[i][j] != compare)
			{
				count++;
			}
			compare *= -1;
		}
		compare *= -1;
	}
	int min = count;
	count = 0;
	compare = -1;
	for (int i = idxN; i < idxN + 8; i++)
	{
		for (int j = idxM; j < idxM + 8; j++)
		{
			if (check[i][j] != compare)
			{
				count++;
			}
			compare *= -1;
		}
		compare *= -1;
	}
	if (count < min)
	{
		min = count;
	}
	return min;

}


int main()
{
	char chass;
	int n, m;
	cin >> n >> m;
	int check[50][50];


	for (int i = 0; i < n; i++)
	{
		memset(check[i], 0, sizeof(int) * m);
	}

	//등록
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			cin >> chass;
			if (chass == 'W')
			{
				check[i][j] = -1;
			}
			else
			{
				check[i][j] = 1;
			}
		}
	}


	int min = 10000;
	int value = 0;
	//찾기
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			value = Find(check, i, j);
			if (value < min)
			{
				min = value;
			}
			if (j+7 == m-1)
			{
				break;
			}
		}
		if (i + 7 == n)
		{
			break;
		}
	}
	cout << min;


}