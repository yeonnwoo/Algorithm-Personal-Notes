#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>

#define SIZE 100
#define INF 100000
#define TRUE 1
#define FALSE 0

typedef struct
{
	int n, m;
	int adj[SIZE][SIZE];

}GraphType;

void make_adj(GraphType* g, int a, int b, int weight)
{
	g->adj[a][b] = weight;
}

void floyd(GraphType* g)
{
	int i, j, k;

	for (k = 0; k < g->n; k++)
	{
		for (i = 0; i < g->n; i++)
		{
			for (j = 0; j < g->n; j++)
			{
				if (g->adj[i][j] > (g->adj[i][k] + g->adj[k][j]))
				{
					g->adj[i][j] = (g->adj[i][k] + g->adj[k][j]);
				}
			}
		}
	}

}

void main()
{
	GraphType g;
	int n, m, s, i, j,a,b,weight;

	scanf("%d %d %d", &g.n, &g.m, &s);

	//인접행렬 초기화
	for (i = 0; i < g.n; i++)
	{
		for (j = 0; j < g.n; j++)
		{
			g.adj[i][j] = INF;

			if (i == j)
			{
				g.adj[i][j] = 0;
			}
		}
	}

	//인접리스트 생성
	for (i = 0; i < g.m ; i++)
	{
		scanf("%d %d %d", &a, &b, &weight);
		make_adj(&g, a-1, b-1, weight);
	}

	//플로이드워셔 알고리즘
	floyd(&g);


	for (i = 0; i < g.n; i++)
	{
		for (j = 0; j < g.n; j++)
		{
			printf("%d ",g.adj[i][j]);
		}
		printf("\n");
	}



	/*

	4 7 1
	1 2 5
	2 1 7
	2 3 9
	3 1 2
	1 4 8
	3 4 4
	4 3 3


	------------


	0 5 11 8
	7 0 9 13
	2 7 0 4
	5 10 3 0

	*/
}