#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>

#define SIZE 10
#define INF 10000000
#define TRUE 1
#define FALSE 0

int distance[SIZE] = { 0 }; //거리 값 계산
bool visited[SIZE];

typedef struct
{
	int n, m; //정점의 개수,간선의 개수
	int weight[SIZE][SIZE];

}GraphType;


void make_adj(GraphType* g, int a, int b, int weight)
{
	g->weight[a][a] = 0; //자기자신은 0
	g->weight[b][b] = 0;

	g->weight[a][b] = weight;
	g->weight[b][a] = weight;
}

void init_adj(GraphType* g, int n)
{
	int i, j;
	for (i = 0; i < n; i++)
	{
		for (j = 0; j < n; j++)
		{
			g->weight[i][j] = INF;
		}
	}
}

int find_min_index(int n)
{
	int i;
	int min = INF + 1;
	int min_index;

	for (i = 0; i < n; i++)
	{
		if (!visited[i] && min > distance[i])
		{
			min = distance[i];
			min_index = i;
		}
	}
	return min_index;
}

void dijkstra(GraphType* g, int s)
{
	int i, j, min;

	//distance 배열 만들기
	for (i = 0; i < g->n; i++)
	{
		distance[i] = g->weight[s][i];
	}
	visited[s] = TRUE; // 시작 노드는 방문 체크

	for (i = 0; i < g->n - 1; i++)
	{
		min = find_min_index(g->n); //distance 배열에서 최소값을 갖는 인덱스
		visited[min] = TRUE; // 방문 처리

		if (distance[min] != INF)
		{
			printf("%d %d \n", min + 1, distance[min]);
		}

		for (j = 0; j < g->n; j++)
		{
			if (!visited[j])
			{
				if (distance[j] > (distance[min] + g->weight[min][j]))
				{
					distance[j] = (distance[min] + g->weight[min][j]);
				}
			}
		}

	}
}
void main()
{
	GraphType g;

	int n, m, s, i, j, a, b, weight;

	scanf("%d %d %d", &g.n, &g.m, &s);

	init_adj(&g, g.n);

	for (i = 0; i < g.m; i++)
	{
		scanf("%d %d %d", &a, &b, &weight);
		make_adj(&g, a - 1, b - 1, weight);
	}

	dijkstra(&g, s - 1);

	for (int i = 0; i < g.n; i++)
	{
		printf("%d ", distance[i]);
	}

}