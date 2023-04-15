#include <iostream>
using namespace std;

int main()
{
	int n;

	cin >> n;
	for (int i = 1; i <= n; i++)
	{
		int a = i;
		int unit = a;
		int result = 0;
		while (1)
		{

			result += unit;
			if (a == 0)
			{
				break;
			}
			unit = a % 10;
			a /= 10;
		}

		if (result == n)
		{
			cout << i;
			return 0;
		}
	}
	cout << 0;
}