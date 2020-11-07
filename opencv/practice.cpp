#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int x; 
	int y; 
	int z;
	int sum; 
	printf("첫번째 숫자를 입력하시오:"); 
	scanf_s("%d", &x); 
	printf("두번째 숫자를 입력하시오:"); 
	scanf_s("%d", &y);
	printf("세번째 숫자를 입력하시오:");
	scanf_s("%d", &z);
	sum = x + y + z;
	printf("모든수의 합: %d", sum);
	sum = (x + y + z) / 3;
    printf("모든수의 평균: %d", sum);
	return 0;
}