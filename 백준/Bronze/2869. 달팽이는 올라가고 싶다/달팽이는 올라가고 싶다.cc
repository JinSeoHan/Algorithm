#include <iostream>
using namespace std;

int main()
{
	int a, b, v;
	cin >> a >> b >> v;
	int day = 1;
	int result = (v - a) / (a - b);



	if ((v - a) % (a - b) != 0)
	{
		cout << result + 2;
	}
	else
	{
		cout << result + 1;
	}
}