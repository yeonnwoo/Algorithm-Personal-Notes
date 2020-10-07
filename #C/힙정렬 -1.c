#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>
#include<stdlib.h>

#define my_max 100

typedef struct
{
	int arr[my_max];
	int last_size;
}heap;

void init(heap* h)
{
	h->last_size = 0;
}

void upheap(heap* h)
{
	int i = h->last_size;
	int key = h->arr[i];

	while ((i != 1) && (key < h->arr[i / 2]))
	{
		h->arr[i] = h->arr[i / 2];
		i/= 2;
		
	}

	h->arr[i] = key;

}

void insert(heap* h, int data)
{
	h->last_size += 1;
	h->arr[h->last_size] = data;

	upheap(h);

}

void print_heap(heap* h)
{
	int i;
	for (i = 1; i <= h->last_size; i++)
	{
		printf("[%d]", h->arr[i]);
	}
}

void downheap(heap* h)
{
	int tmp = h->arr[1];
	int parent = 1, child = 2;
	while (child <= h->last_size)
	{
		if (child < h->last_size && (h->arr[child] > h->arr[child + 1]))
		{
			child++;
		}
		if (tmp < h->arr[child])
		{
			break;
		}
		h->arr[1] = h->arr[child];
		parent = child;
		child = child * 2;
	}
	h->arr[parent] = tmp;
}

int remove(heap* h)
{
	int key = h->arr[1];
	h->arr[1] = h->arr[h->last_size];
	
	h->last_size -= 1;
	downheap(h);
	return key;
}


void main()
{
	heap heap;
	init(&heap);

	char c;
	int data;
	
	while (1)
	{
		scanf("%c", &name);
		getchar();
		if (name == 'i')
		{
			scanf("%d", &data);
			getchar();
			insert(&heap, data);
			printf("%d\n", 0);
		}
		if (name == 'd')
		{
			printf("%d\n", remove(&heap));
		}
		if (name == 'q')
		{
			break;
		}
	}
	

}
