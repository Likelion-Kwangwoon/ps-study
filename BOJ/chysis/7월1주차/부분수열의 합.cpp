#include <iostream>
using namespace std;

int N, S;
int cnt=0;
int arr[21];
int ans[21];
bool used[21];

void solve(int idx, int num, int sum){
    if(num!=0 && sum==S){
        cnt++;
    }
    
    for(int i=idx; i<N; i++){
        if(!used[i]){
            used[i]=true;
            ans[num]=arr[i];
            solve(i, num+1, sum+arr[i]);
            used[i]=false;
        }
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin>>N>>S;
    for(int i=0; i<N; i++){
        cin>>arr[i];
    }
    solve(0, 0, 0);
    cout<<cnt;
}