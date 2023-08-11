#include <iostream>
using namespace std;

int arr[1001];
int DP[1001];

int main()
{
    int N;
    cin>>N;
    for(int i=0; i<N; i++){
        cin>>arr[i];
    }
    for(int i=0; i<N; i++){
        DP[i]=1;
    }
    int ans=1;
    for(int i=0; i<N; i++){
        for(int j=0; j<i; j++){
            if(arr[j]>arr[i]){
                DP[i]=max(DP[j]+1, DP[i]);
                if(ans<DP[i]) ans=DP[i];
            }
        }
    }
    cout<<ans;
}