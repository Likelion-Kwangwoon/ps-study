#include <iostream>
#include <algorithm>
using namespace std;

int arr[10001];
int DP[10001];

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int N;
    cin>>N;
    for(int i=1; i<=N; i++){
        cin>>arr[i];
    }
    DP[1]=arr[1];
    DP[2]=arr[1]+arr[2];
    for(int i=3; i<=N; i++){
        DP[i]=max(max(DP[i-2]+arr[i], DP[i-3]+arr[i-1]+arr[i]), DP[i-1]);
    }
    cout<<DP[N];
}