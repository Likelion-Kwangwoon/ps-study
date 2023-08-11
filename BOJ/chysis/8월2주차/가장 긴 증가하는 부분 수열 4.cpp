#include <iostream>
#include <algorithm>
using namespace std;

int arr[1001];
int DP[1001];

void backtrack(int idx, int len){
    if(idx==-1) return;
    if(DP[idx]==len){
        backtrack(idx-1, len-1);
        cout<<arr[idx]<<" ";
    }
    else{
        backtrack(idx-1, len);
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int N;
    cin>>N;
    for(int i=0; i<N; i++){
        cin>>arr[i];
    }
    for(int i=0; i<N; i++){
        DP[i]=1;
    }
    int len=DP[0];
    for(int i=0; i<N; i++){
        for(int j=0; j<i; j++){
            if(arr[j]<arr[i])
                DP[i]=max(DP[j]+1, DP[i]);
                if(DP[i]>len) len=DP[i];
        }
    }
    
    cout<<len<<"\n";
    backtrack(N-1, len);
}