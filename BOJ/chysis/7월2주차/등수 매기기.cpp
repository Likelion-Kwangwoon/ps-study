#include <iostream>
#include <algorithm>
using namespace std;

int arr[500001];

int main()
{
    int N;
    cin>>N;
    for(int i=1; i<=N; i++){
        cin>>arr[i];
    }
    sort(arr+1, arr+N+1);

    long long ans=0;
    for(int i=1; i<=N; i++){
        ans+=abs(i-arr[i]);
    }
    cout<<ans;
}