#include <iostream>
#include <vector>
using namespace std;

int N;
int ans[8];

bool isPrime(int n){
    if(n==1) return false;
    for(int i=2; i*i<=n; i++){
        if(n%i==0) return false;
    }
    return true;
}

void solve(int now, int cnt){
    if(cnt==N){
        cout<<now<<"\n";
        return;
    }
    
    int other[5]={1, 3, 5, 7, 9};
    
    for(int i=0; i<5; i++){
        int tmp=now*10+other[i];
        if(isPrime(tmp)){
            solve(tmp, cnt+1);
        }
    }
}

int main()
{
    cin>>N;
    int prime[4]={2, 3, 5, 7};
    for(int i=0; i<4; i++){
        ans[0]=prime[i];
        solve(prime[i], 1);
    }
}