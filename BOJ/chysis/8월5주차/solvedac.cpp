#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

int arr[300001];

int main()
{
    int N;
    cin>>N;
    if(N==0){
        cout<<0;
        return 0;
    }
    for(int i=0; i<N; i++){
        cin>>arr[i];
    }
    sort(arr, arr+N);
    int offset=round(N*0.15);
    double sum=0;
    for(int i=offset; i<N-offset; i++){
        sum+=arr[i];
    }
    cout<<round(sum/(N-2*offset));
}