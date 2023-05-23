#include <iostream>
using namespace std;

int main()
{
    int N;
    cin>>N;
    int arr[1001];
    int dp[1001];
    for(int i=0; i<N; i++){
        cin>>arr[i];
    }
    for(int i=0; i<N; i++){
        dp[i]=1;
    }
    for(int i=1; i<N; i++){
        for(int j=0; j<i; j++){
            if(arr[j]<arr[i])
                dp[i]=max(dp[i], dp[j]+1);
        }
    }

    int ans=-1;
    for(int i=0; i<N; i++){
        ans=max(ans, dp[i]);
    }
    cout<<ans;
}