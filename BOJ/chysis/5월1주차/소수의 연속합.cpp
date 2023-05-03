#include <iostream>
#include <vector>
using namespace std;

vector<int> prime;

void solve(int n){
    if(n==1) return;
    vector<bool> v(n+1, true);
    
    for(int i=2; i*i<=n; i++){
        if(v[i]){
            for(int j=i*2; j<=n; j+=i){
                v[j]=false;
            }
        }
    }
    for(int i=2; i<=n; i++){
        if(v[i]) prime.push_back(i);
    }
}

int main()
{
    int N;
    cin>>N;
    if(N==1) {cout<<0; return 0;}
    
    solve(N);
    int s=0, e=0, cnt=0;
    int sum=0;
    while(e<=prime.size()){
        if(sum<N){
            sum+=prime[e++];
        }
        else{
            if(sum==N) cnt++;
            sum-=prime[s++];
        }
    }
    cout<<cnt;
}
