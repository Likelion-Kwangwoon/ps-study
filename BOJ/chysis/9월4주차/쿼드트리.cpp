#include <iostream>
using namespace std;

int arr[65][65];

int compression(int size, int x, int y){
    bool zero=false, one=false;
    for(int i=x; i<x+size; i++){
        for(int j=y; j<y+size; j++){
            if(arr[i][j]==0) zero=true;
            else if(arr[i][j]==1) one=true;
        }
    }
    
    if(zero && !one) return 0;
    else if(!zero && one) return 1;
    else return -1;
}

void solve(int size, int x, int y){
    int state=compression(size, x, y);
    if(state==0 || state==1){
        cout<<state;
    }
    else{
        cout<<"(";
        solve(size/2, x, y);
        solve(size/2, x, y+size/2);
        solve(size/2, x+size/2, y);
        solve(size/2, x+size/2, y+size/2);
        cout<<")";
    }
    return;
}

int main()
{
    int N;
    cin>>N;
    char c;
    for(int i=1; i<=N; i++){
        for(int j=1; j<=N; j++){
            cin>>c;
            arr[i][j]=c-'0';
        }
    }
    solve(N, 1, 1);
}