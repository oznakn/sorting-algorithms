#include <stdio.h>

/* bubble sort written in C */

void bubble_sort(float **arr, int size);

int main(void)
{
	/* driver code here */
	float *fp, arr[]={1,5,4,3,6,5,4,7,3,25,4,37,546,0,-15,0.25};
	int size = 16, j;
	fp = arr;

	printf("{");
	for (j=0; j<size-1; j++)
	{
		printf("%f, ", fp[j]);
	}
	printf("%f}\n", fp[size-1]);

	bubble_sort(&fp, size);

	printf("{");
	for (j=0; j<size-1; j++)
	{
		printf("%f, ", fp[j]);
	}
	printf("%f}\n", fp[size-1]);


	return 0;
}

void bubble_sort(float **arr, int size)
{
	/* 
	 * sorts in place.
	 * pass a pointer to an array of integers
	 * or basically a pointer to a float
	 * pointer to the function.
	 * */

	int is_sorted = 0, i, tmp;
	while (!is_sorted)
	{
		is_sorted = 1;
		for (i=0; i<size-1; i++)
		{
			if ((*arr)[i] > (*arr)[i+1])
			{
				tmp = (*arr)[i];
				(*arr)[i] = (*arr)[i+1];
				(*arr)[i+1] = tmp;
				is_sorted = 0;
			}
		}
	}
}
