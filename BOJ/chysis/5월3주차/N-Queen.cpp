#include <iostream>
#include <cmath>
#define MAX 15
using namespace std;

int N;
int col[MAX+1];
int ans=0;

bool promising(int cnt){
    int k=0;
    bool flag=true;
    
    while(k<cnt && flag){
        if(col[cnt]==col[k] || abs(col[cnt]-col[k])==cnt-k) flag=false;
        k++;
    }
    return flag;
}

void queens(int cnt){
    if(cnt==N){
        ans++;
        return;
    }
    else {
        for(int j=1; j<=N; j++){
            col[cnt]=j;
            if(promising(cnt)){
                queens(cnt+1);
            }
        }
    }
}

int main()
{
    cin>>N;
    queens(0);
    cout<<ans;
}