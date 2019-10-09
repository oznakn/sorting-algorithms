#include <stdio.h> 
#include <algorithm>    
#include <vector>       
#include <ctime>        
#include <cstdlib>
using namespace std;
bool is_sorted(int a[], int n) 
{ 
	for (int i = 0; i < n-1; ++i)
		if (a[i] > a[i + 1]) 
			return false; 
	return true; 
}
void bogosort(int a[], int n) 
{ 
	while (!is_sorted(a, n)) 
		random_shuffle(a,a+n); 
}
int main() 
{ 
	srand(time(NULL));
	int a[] = { 7, 5, 6, 3, 1, 2}; 
	int n = sizeof a / sizeof a[0]; 
	bogosort(a, n); 
	for (int i = 0; i < n; i++) 
		printf("%d ", a[i]); 
	printf("\n"); 
	return 0; 
} 
