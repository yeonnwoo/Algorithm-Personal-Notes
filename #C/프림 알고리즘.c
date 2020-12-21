#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>

#define SIZE 100
#define INF 100000
#define TRUE 1
#define FALSE 0

int distance[SIZE];
int visited[SIZE] = { FALSE };

typedef struct
{
	int n, m;
	int adj[SIZE][SIZE];

}GraphType;

//인접행렬 생성
void make_adj(GraphType* g, int a, int b, int weight)
{
	int i,j;

	for (i = 0; i < g->n; i++)
	{
		for (j = 0; j < g->n; j++)
		{
			if (i == j)
			{
				g->adj[i][j] = 0;
			}

			g->adj[a][b] = weight;
			g->adj[b][a] = weight;
		}
	}

}

int min_check(int n)
{
	int min=0,i,j;

	//임의의 min 값 지정
	for (i = 0; i < n; i++)
	{
		if (!visited[i])
		{
			min = i;
			break;
		}
	}
	
	//진짜 min 값 찾아줌
	for (i = 0; i < n; i++)
	{
	
		if (!visited[i] && distance[i] < distance[min])
			{
				min = i;
			}	
	}

	return min;

}

void prim(GraphType* g, int s)
{
	int i,j,min;
	int sum = 0;

	//distance 초기화
	for (i = 0; i < g->n; i++)
	{
		distance[i] = INF;
	}

	distance[s] = 0;

	for (i = 0; i < g->n; i++)
	{
		min = min_check(g->n);
		visited[min] = TRUE;

		printf(" %d", min+1);
		sum += distance[min];

		//방문안했고, INF 값이 아닌 애들 distance에 넣어줌
		for (j = 0; j < g->n; j++)
		{
			if (!visited[j] && g->adj[min][j] !=INF && g->adj[min][j] < distance[j])
			{
				distance[j] = g->adj[min][j];
			}
		}		

	}
	printf("\n");
	printf("%d", sum);
	
}


void main()
{
	GraphType g;
	int i, j, a, b, w;
	int s = 0; //처음 시작하는 부분

	scanf("%d %d", &g.n, &g.m);

	//인접행렬 초기화
	for (i = 0; i < g.n; i++)
	{
		for (j = 0; j < g.n; j++)
		{
			g.adj[i][j] = INF;
		}
	}

	for (i = 0; i < g.m; i++)
	{
		scanf("%d %d %d", &a, &b, &w);
		make_adj(&g, a-1, b-1, w);
	}


	prim(&g, s);

}

