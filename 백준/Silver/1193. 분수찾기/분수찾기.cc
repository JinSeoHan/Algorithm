#include <iostream>
using namespace std;

int main()
{
	int x = 0;
	int y = 0;
	int input;
	cin >> input;
	int increase = -1;
	bool check = false;
	
	for (int i = 0; i < input; i++)
	{
		if (x == 0 && y == 0)
		{
			x++;
			y++;
			continue;
		}
		if (x == 1 && !check)
		{
			y++;
			increase *= -1;
			check = true;
			continue;
		}
		if (y == 1 && !check)
		{
			x++;
			increase *= -1;
			check = true;
			continue;
		}

		check = false;
		x += increase;
		y -= increase;
	}
	cout << x << '/' << y;
}