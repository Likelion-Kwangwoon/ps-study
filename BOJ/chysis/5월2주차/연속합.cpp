#include <iostream>
#include <algorithm>
using namespace std;

int arr[100001];

int main()
{
    int N;
    cin>>N;
    for(int i=0; i<N; i++){
        cin>>arr[i];
    }
    for(int i=1; i<N; i++){
        arr[i]=max(arr[i-1]+arr[i], arr[i]);
    }
    int ans=arr[0];
    for(int i=0; i<N; i++){
        if(ans<arr[i]) ans=arr[i];
    }
    cout<<ans;
}