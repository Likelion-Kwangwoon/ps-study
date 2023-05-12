#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int N;
    cin>>N;
    int arr[100001];
    arr[0]=0;
    arr[1]=1;
    arr[2]=2;
    arr[3]=3;
    for(int i=4; i<=N; i++){
        arr[i]=arr[i-1]+1;
        for(int j=1; j*j<=i; j++){
            arr[i]=min(arr[i], arr[i-j*j]+1);
        }
    }
    cout<<arr[N];
}