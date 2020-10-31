//BUBBLE SORT FOR SORTING FILES REPO
//BY HERIPOTIR


#include <iostream>
using namespace std;

void swap( float *ptr1, float *ptr2 ) //swaps by ptr
{
	float temp= *ptr2;
	*ptr2=*ptr1;
	*ptr1=temp;

}

void bubble_sort(float array[])
{
	int n=sizeof(array)-1;
	int flag=0;
	for(int i=0; i<(n-1) ; i++ )
	{	
		flag=0;
		for(int j=0; j<(n-1-i);j++)
		{
			if(array[j]>array[j+1])
			{
				swap(&array[j],&array[j+1]);
				flag=1;
			}
			if(flag==0)
				break;
		}		
	};	
};

void print_array(float array[]) 
{ 
    int n=sizeof(array)-1;
    for (int i=0; i < n; i++) 
        cout<<array[i]<<" ";     
    cout<<endl;
} 

int main() 
{ 
    float array[] = {64, 34, 25, 12, 22, 11, 90}; 
    cout<<"Original array"<<endl; 
    print_array(array);
    cout<<"Sorted array"<<endl; 
    bubble_sort(array); 
    print_array(array); 
    return 0; 
} 
