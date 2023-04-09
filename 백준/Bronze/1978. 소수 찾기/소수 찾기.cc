#include <iostream>
using namespace std;

bool IsPrimeNumber(int value)
{
	bool isPrime = true;
	for (int i = 2; i*i <= value; i++)
	{
		if (value % i == 0)
		{
			isPrime = false;
			break;
		}
	}
	return isPrime;
}
int main()
{
	int count = 0;
	int input, value;
	cin >> input;
	for (int i = 0; i < input; i++)
	{
		cin >> value;
		if (value == 1)
		{
			continue;
		}
		if (IsPrimeNumber(value))
		{
			count++;
		}
	}
	cout << count;
	
}