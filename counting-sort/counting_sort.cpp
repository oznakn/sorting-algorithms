#include <bits/stdc++.h>

using namespace std;

vector<int> counting_sort(vector<int> v, int max_num){
    int numbers[max_num+1], j=0, n=v.size();
    for(int i=0;i<max_num+1;i++) numbers[i]=0;
    for(int i=0;i<n;i++) numbers[v[i]]++;
    for(int i=0;i<max_num+1;i++) while(numbers[i]--) v[j++]=i;
    return v;
}

int main(){
    ios_base::sync_with_stdio(false); cin.tie(NULL);

    int n=100000;
    vector<int> v;

    for(int i=0;i<n;i++) v.push_back(rand()%1001);

    v = counting_sort(v, 1000);

    for(int i=0;i<n;i++){
        cout<<v[i]<<' ';
    }
    
}
