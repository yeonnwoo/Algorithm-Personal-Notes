#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<malloc.h>


void insertsort(int arr[], int n)
{
	int i, j, ptr;

	for (i = 1; i < n; i++)
	{
		ptr = arr[i];
		for (j = i - 1; j >= 0; j--)
		{
			if (ptr < arr[j])
			{
				arr[j + 1] = arr[j];
				arr[j] = ptr;
			}
		}

	}


}

int main(void)
{
	int* arr;
	int i, n;

	scanf("%d", &n);

	arr = (int*)malloc(sizeof(int) * n);

	for (i = 0; i < n; i++)
	{
		scanf("%d", &arr[i]);
	}


	insertsort(arr, n);

	for (i = 0; i < n; i++)
	{
		printf(" %d", arr[i]);
	}

	free(arr);


	return 0;

}
