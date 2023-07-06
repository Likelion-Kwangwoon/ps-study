#include <iostream>
using namespace std;

int arr[101];
int DP[10001];

int main()
{
    int N, K;
    cin>>N>>K;
    for(int i=0; i<N; i++){
        cin>>arr[i];
    }
    DP[0]=1;
    for(int i=0; i<N; i++){
        for(int j=arr[i]; j<=K; j++){
            DP[j]+=DP[j-arr[i]];
        }
    }
    cout<<DP[K];
}