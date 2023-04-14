// 딜러가 숫자 M을 외침
// 플레이어는 제한된 시간내에 n1,n2,n3 의 카드를 뽑고 
// n1+n2+n3 <= M이여가 한다.
// 14*2.5

//입력부분
// 개수N 과 넘으면안되는수M

//출력부분
// 3개를 골라서 더한다음에 가장 M과 비슷한 수를 구하여라

#include <iostream>
using namespace std;

int main()
{
	int cardCount; // 3<= cardCount <= 100
	int maxNum; // 10 <= maxNum <= 300,000
	int compareMaxNum = 0; //비교할 가장 큰 수

	cin >> cardCount >> maxNum;

	int cardNums[100] = { 0, }; //cardCount개수에 대한 카드의 수
	for (int i = 0; i < cardCount; i++)//개수만큼 카드수를 받음
	{
		cin >> cardNums[i];
	}

	// 모든 경우의 수를 다 찾는 알고리즘
	for (int i = 0; i < cardCount-2; i++)//첫 번째 자리의 경우의수
	{
		for (int j = i+1; j < cardCount-1; j++)//두 번째 수의 경우의수  
		{
			for (int k = j+1; k < cardCount; k++)//세 번째 수의 경우의수
			{
				if (maxNum < (cardNums[i] + cardNums[j] + cardNums[k]))//3수의 합이 m을 넘어버리면 out
				{
					continue;
				}
				else if (compareMaxNum < (cardNums[i] + cardNums[j] + cardNums[k]))//3수의 합이 이때까지 찾은 수 중에서 가장 크다면
				{
					compareMaxNum = cardNums[i] + cardNums[j] + cardNums[k];
				}
			}
		}
	}
	cout << compareMaxNum;
}