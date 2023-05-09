#include <iostream>
#include <algorithm>
using namespace std;

int arr[1000001];

int main()
{
    int N;
    cin>>N;
    
    for(int i=1; i<=N; i++)
        arr[i]=i;
    
    for(int i=2; i<=N; i++){
        arr[i]=arr[i-1]+1;
        if(i%2==0){
            arr[i]=min(arr[i], arr[i/2]+1);
        }
        if(i%3==0){
            arr[i]=min(arr[i], arr[i/3]+1);
        }
    }
    cout<<arr[N]-1<<"\n";
    while(N>0){
        cout<<N<<" ";
        if(arr[N]==arr[N-1]+1) N-=1;
        else if(N%2==0 && arr[N]==arr[N/2]+1) N/=2;
        else if(N%3==0 && arr[N]==arr[N/3]+1) N/=3;
    }
}