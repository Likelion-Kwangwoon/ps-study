#include <iostream>
using namespace std;

int arr[1001][1001];

int main()
{
    int N, K;
    cin>>N>>K;
    for(int i=0; i<=N; i++){
        arr[i][0]=1;
        arr[i][i]=1;
    }
    for(int i=2; i<=N; i++){
        for(int j=1; j<i; j++){
            arr[i][j]=(arr[i-1][j-1]+arr[i-1][j])%10007;
        }
    }
    cout<<arr[N][K];
}