#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<malloc.h>


void selsort(int arr[], int n)
{
	int i, j;
	int max, maxidx = 0;
	int tmp;

	for (i = n - 1; i > 0; i--)
	{
		max = arr[i];
		maxidx = i;

		for (j = i - 1; j >= 0; j--)
		{
			if (arr[j] > max)
			{
				max = arr[j];

				maxidx = j;
			}

		}

		tmp = arr[i];
		arr[i] = arr[maxidx];
		arr[maxidx] = tmp;

	}


}

int main(void)
{
	int n, i;

	scanf("%d", &n);

	int* arr = (int*)malloc(sizeof(int) * n);

	for (i = 0; i < n; i++)
	{
		scanf("%d", &arr[i]);
	}

	selsort(arr, n);

	for (i = 0; i < n; i++)
	{
		printf(" %d", arr[i]);
	}

	free(arr);

	return 0;
}
