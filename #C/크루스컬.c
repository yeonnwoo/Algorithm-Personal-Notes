#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>

#define SIZE 100
#define INF 10000
#define TRUE 1
#define FALSE 0

//adj 구조체
typedef struct
{
	int start, end, weight;

}AdjType;

typedef struct
{
	int n, m;
	AdjType adj[SIZE];

}GraphType;

int k = 0;

void make_adj(GraphType* g, int start, int end, int weight)
{
	g->adj[k].start = start;
	g->adj[k].end = end;
	g->adj[k].weight = weight;
	k++;
}

int parent[SIZE];

void init_parent(int n)
{
	int i;
	for (i = 1; i < n+1; i++)
	{
		parent[i] = i;
	}
}

int get_parent(int x)
{
	if (parent[x] == x)
	{
		return x;
	}
	else
	{
		return parent[x] = get_parent(parent[x]);
	}

}

void union_parent(int a, int b) //하나의 그래프이니, 같은 부모로 연결
{
	if (a < b)
	{
		parent[b] = a;
	}
	else
	{
		parent[a] = b;
	}
}

int compare(const void* a, const void* b)
{
	AdjType* x = (AdjType*)a;
	AdjType* y = (AdjType*)b;
	return(x->weight - y->weight);

}

void kruscal(GraphType* g)
{
	qsort(g->adj, g->m, sizeof(AdjType), compare); //정렬할 것,개수,사이즈,함수

	int a, b;
	int sum = 0;
	int edge_accepted = 0;
	int i = 0;
	AdjType str;

	init_parent(g->n); //parent 배열 초기화

	while (edge_accepted < g->n-1)
	{
		str = g->adj[i];

		a = get_parent(str.start);
		b = get_parent(str.end );

		if (a != b) //부모가 같지 않으면
		{
			printf(" %d", str.weight);
			sum += str.weight;
			edge_accepted++;
		}

		union_parent(a, b); //같은 그래프로 넣어줌
		i++;

	}
	printf("\n");
	printf("%d", sum);
}

void main()
{
	int i, j, a, b, w;

	GraphType g;

	scanf("%d %d", &g.n, &g.m);

	//adj 초기화
	for (i = 0; i < g.m; i++)
	{
		g.adj[i].start = 0;
		g.adj[i].end = 0;
		g.adj[i].weight = INF;
	}

	//adj 만들기
	for (i = 0; i < g.m; i++)
	{
		scanf("%d %d %d", &a, &b, &w);
		make_adj(&g, a, b, w);
	}

	kruscal(&g);

}