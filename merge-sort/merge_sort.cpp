#include <bits/stdc++.h>

int totCmp=0;
int totLkp=0;
int totMem=0;
int simMem=0;
int maxMem=0;

template<typename T>
int cmpMerge(T x,T y){
	totCmp++;
	if(x>y){
		return -1;
	}
	return 1;
}

//recursively call merge sort, in each layer calculate deeper levels first
//and when the left and right half is sorted with merge sort, compare and
//zip two halves together in O(n). //copy left and right half into 2 arrays

void MergeSort(int *l, int *r){
	int * mid=(r-l)/2 + l;
	totLkp+=3;
	if(r-l==1){
		return;	
	}
	totCmp++;
	MergeSort(l,mid);
	MergeSort(mid,r);
	int sz1=mid-l;
	int sz2=r-mid;
	totLkp+=4;
	int *tmparr=new int[sz1];
	int *tmparr2=new int[sz2];
	totMem+=sz1+sz2;
	simMem+=sz1+sz2;
	maxMem=simMem<maxMem?maxMem:simMem;
	for(int i=0;i<r-l;i++){
		totLkp++;
		if(i<sz1){
			tmparr[i]=l[i];
			totLkp+=2;
			
		}else{
			tmparr2[i-sz1]=l[i];
			totLkp+=3;
		}
		totCmp++;
	}
	int ptr1=0;
	int ptr2=0;
	int *begin=l;
	
	//both of the arrays have elements left
	while(ptr1 < sz1 && ptr2 < sz2){
		totLkp++;
		totCmp+=3;
		if(cmpMerge(tmparr[ptr1],tmparr2[ptr2])>0){
			*begin=tmparr[ptr1];
			begin++;
			ptr1++;
		}else{
			*begin=tmparr2[ptr2];
			begin++;
			ptr2++;
		}
		totLkp+=3;
	}
	//if at least one of the arrays don't have elements left
	while(ptr1 < sz1 || ptr2 < sz2){
		totCmp+=3;
		if(ptr1 < sz1){
			*begin=tmparr[ptr1];
			begin++;
			ptr1++;		
		}else{
			*begin=tmparr2[ptr2];
			begin++;
			ptr2++;			
		}
		totLkp+=3;
	}
	delete []tmparr;
	delete []tmparr2;
	simMem-=sz1+sz2;
	//now l -> r is sorted, you can return to tell that this half is now sorted.
	return;
}
int main(){
	int arr[150];
	int n;
	std::cout<<"enter the size of your array:";
	std::cin >> n;
	std::cout<<"\nenter your array:";
	for(int i=0;i<n;i++){
		std::cin >> arr[i];
	}
	std::cout<<std::endl;
	MergeSort(arr,arr+n);
	for(int i=0;i<n;i++){
		std::cout<<arr[i]<<" ";
	}std::cout<<std::endl;
	std::cout<<totCmp<<" ~total comparisons made"<<std::endl;
	std::cout<<totLkp<<" ~total lookups+calculations made"<<std::endl;
	std::cout<<totMem<<" ~total memory allocations"<<std::endl;
	std::cout<<maxMem<<" ~max <int> memory used simultaneously"<<std::endl;
	return 0;
}
//version without lookup/memory counters:
/*
template<typename T>
int cmpMerge(T x,T y){
	if(x>y){
		return -1;
	}
	return 1;
}


void MergeSort(int *l, int *r){
	int * mid=(r-l)/2 + l;
	totLkp+=3;
	if(r-l==1){
		return;	
	}
	totCmp++;
	MergeSort(l,mid);
	MergeSort(mid,r);
	int sz1=mid-l;
	int sz2=r-mid;
	totLkp+=4;
	int *tmparr=new int[sz1];
	int *tmparr2=new int[sz2];
	totMem+=sz1+sz2;
	simMem+=sz1+sz2;
	maxMem=simMem<maxMem?maxMem:simMem;
	for(int i=0;i<r-l;i++){
		if(i<sz1){
			tmparr[i]=l[i];
		}else{
			tmparr2[i-sz1]=l[i];
		}
	}
	int ptr1=0;
	int ptr2=0;
	int *begin=l;
	
	//both of the arrays have elements left
	while(ptr1 < sz1 && ptr2 < sz2){
		if(cmpMerge(tmparr[ptr1],tmparr2[ptr2])>0){
			*begin=tmparr[ptr1];
			begin++;
			ptr1++;
		}else{
			*begin=tmparr2[ptr2];
			begin++;
			ptr2++;
		}
	}
	//if at least one of the arrays don't have elements left
	while(ptr1 < sz1 || ptr2 < sz2){
		if(ptr1 < sz1){
			*begin=tmparr[ptr1];
			begin++;
			ptr1++;		
		}else{
			*begin=tmparr2[ptr2];
			begin++;
			ptr2++;			
		}
	}
	delete []tmparr;
	delete []tmparr2;
	//now l -> r is sorted, you can return to tell that this half is now sorted.
	return;
}
*/
