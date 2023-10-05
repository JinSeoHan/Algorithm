#include <iostream>
using namespace std;
int main()
{
	bool check[10500] = { false, };
	int mok;
	int sum = 0;
	int count = 0;
	for (count = 0; count < 10000; count++)
	{
		mok = count+1;
		do
		{
			sum += mok % 10;
			mok /= 10;
		} while (mok != 0);
		check[sum+count+1] = true;
		sum = 0;
	}
	for (int i = 0; i < count; i++)
	{
		if (check[i] == true || i == 0)
		{
			continue;
		}

		cout << i << '\n';
	}
}