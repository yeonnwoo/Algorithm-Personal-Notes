#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>

#define SIZE 100
#define INF 100000
#define TRUE 1
#define FALSE 0

//adj의 구조체 AdjType
typedef struct
{
	int start, end, weight; //시작 정점,끝 정점,가중치

}AdjType;

typedef struct
{
	int n, m; //노드 개수,간선의 개수
	AdjType adj[SIZE]; //간선을 저장하기 위한 배열

}GraphType;


int k = 0;

//그래프 생성
void make_adj(GraphType* g, int start, int end, int weight)
{

	g->adj[k].start = start;
	g->adj[k].end = end;
	g->adj[k].weight = weight;
	k++;
}

int parent[SIZE];


void init_parent(int m) //parent 배열 초기화 (자기자신 연결)
{
	for (int i = 0; i < m; i++)
	{
		parent[i] = i;
	}
}

int getParent(int x)
{
	if (parent[x] == x) //부모랑 자신이랑 같으면 return(종료조건)
	{
		return x;
	}
	else //자신이 현재 가리키고 있는 부모노드의 값과 자신과 다르다면 실제 부모를 찾음
	{
		return parent[x] = getParent(parent[x]);
	}
}

void unionParent(int a, int b) //새로 찾은 부모로 넣어줌 (둘중에 작은애를 부모로)
{
	a = getParent(a);
	b = getParent(b);

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
	return (x->weight - y->weight);
}

void kruskal(GraphType* g)
{
	AdjType str;

	int edge_accepted = 0;
	int a, b;
	int sum = 0;

	//정렬
	qsort(g->adj, g->m, sizeof(AdjType), compare);

	//union-parent의 parent 배열 초기화
	init_parent(g->m); 
	
	int i = 0;

	while (edge_accepted < g->n-1) //선택된 간선의 수가 그래프의 노드-1 보다 작을 동안
	{
		str = g->adj[i];

		a = getParent(str.start);
		b = getParent(str.end);

		if (a != b) //다른 부모를 가지면.. => 싸이클이 형성 안되면
		{

			printf(" %d", str.weight);
			sum += str.weight;
			edge_accepted++;
			unionParent(a, b); //새로운 부모로 갱신
		}
		i++;
	}

	printf("\n");
	printf("%d", sum);
}

void main()
{
	GraphType g;

	int i, j, a, b, w;

	scanf("%d %d", &g.n, &g.m);


	//adj 초기화
	for (i = 0; i < g.m; i++)
	{
		g.adj[i].start = 0;
		g.adj[i].end = 0;
		g.adj[i].weight = INF;
	}

	for (i = 0; i < g.m; i++)
	{
		scanf("%d %d %d", &a, &b, &w);

		make_adj(&g, a, b, w);
	}

	kruskal(&g);

}