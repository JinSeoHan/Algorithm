#include <iostream>
using namespace std;

int main()
{
	int testCase = 0;
	cin >> testCase; 
	int students[1000] = { 0, };
	int studentsScore[100][1000];
	for (int i = 0; i < testCase; i++)
	{
		cin >> students[i];//테스트케이스 만큼 학생들의 수를 받음
		for (int j = 0; j < students[i]; j++)//학생들의 수만큼 점수를 받음
		{
			cin >> studentsScore[i][j];
		}
	}
	float averages[100] = { 0, };
	for (int i = 0; i < testCase; i++)//점수 평균
	{
		for (int j = 0; j < students[i]; j++)
		{
			averages[i] += studentsScore[i][j];
		}
		averages[i] /= students[i];
	}
	float ovAverageCount = 0;/*[100] = { 0, };*/
	for (int i = 0; i < testCase; i++)//평균을 넘는 학새의수를 샌다
	{
		for (int j = 0; j < students[i]; j++)
		{
			if (averages[i] < studentsScore[i][j])
			{
				ovAverageCount++;
			}
		}
		cout << fixed;
		cout.precision(3);
		cout << ovAverageCount / students[i] * 100 << '%' << endl;

		ovAverageCount = 0;
	}
}