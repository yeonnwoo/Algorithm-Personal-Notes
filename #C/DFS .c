#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>

#define SIZE 100
#define INF 100000
#define TRUE 1
#define FALSE 0

int visited[SIZE] = { FALSE };

typedef struct
{
	int n, m;
	int adj[SIZE][SIZE];

}GraphType;

void make_adj(GraphType* g, int a, int b)
{
	g->adj[a][b] = 1;
	g->adj[b][a] = 1;
}

void dfs(GraphType* g, int s)
{
	visited[s] = TRUE;
	printf("%d\n", s + 1);

	for (int i = 0; i < g->n; i++)
	{
		if (!visited[i] && g->adj[s][i] == 1)
		{
			dfs(g, i);
		}

	}

}
void main()
{
	GraphType g;
	int n, m, s, a, b, i,j;

	scanf("%d %d %d", &g.n, &g.m, &s);

	//인접행렬 초기화
	for (i = 0; i < g.n; i++) 
	{
		for (j = 0; j < g.n; j++)
		{
			g.adj[i][j] = 0;
		}
	}

	//인접행렬 만들기
	for (i = 0; i < g.m; i++)
	{
		scanf("%d %d", &a, &b);
		make_adj(&g, a-1, b-1);
	}
	dfs(&g, s - 1);

}