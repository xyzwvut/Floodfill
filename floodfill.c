#include "stdio.h"

#define NUM_X 6
#define NUM_Y 6

char arr2d[NUM_Y][NUM_X] = {
	 1, 1, 0, 0, 0, 0,
	 1, 1, 0, 0, 0, 0,
	 0, 1, 0, 0, 0, 0,
	 0, 1, 0, 0, 0, 0,
	 0, 1, 1, 1, 0, 0,
	 0, 0, 0, 0, 0, 0,
};


void fill2d_h(int x, int y, char q, char color)
{
	if (x < 0 || x >= NUM_X)
		return;
	if (y < 0 || y >= NUM_Y)
		return;
	if (arr2d[y][x] != q)
		return;

	arr2d[y][x] = color;

	fill2d_h(x+1, y  , q, color);
	fill2d_h(x-1, y  , q, color);
	fill2d_h(x  , y+1, q, color);
	fill2d_h(x  , y-1, q, color);
}

void fill2d(int x, int y, char color)
{
	if (x < 0 || x >= NUM_X)
		return;
	if (y < 0 || y >= NUM_Y)
		return;

	fill2d_h(x, y, arr2d[y][x], color);
}

void print_grid()
{
	int y, x;

	for (y=0; y < NUM_Y; y++) {
		for (x=0; x < NUM_X; x++) {
			printf("%d", arr2d[y][x]);
		}
		printf("\n");
	}
}

int main (void)
{
	printf("Before\n");
	print_grid(arr2d);

	fill2d(0, 0, 4);

	printf("After\n");
	print_grid(arr2d);

	return 0;
}
