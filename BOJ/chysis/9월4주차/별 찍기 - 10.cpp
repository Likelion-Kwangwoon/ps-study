#include <iostream>
using namespace std;

char star[2188][2188]={'-',};

void solve(int size, int x, int y){
    if(size==3){
        for(int i=x; i<x+size; i++){
            for(int j=y; j<y+size; j++){
                if(i==x+1 && j==y+1) continue;
                else star[i][j]='*';
            }
        }
        return;
    }
    
    solve(size/3, x, y);
    solve(size/3, x, y+size/3);
    solve(size/3, x, y+size*2/3);
    solve(size/3, x+size/3, y);
    solve(size/3, x+size/3, y+size*2/3);
    solve(size/3, x+size*2/3, y);
    solve(size/3, x+size*2/3, y+size/3);
    solve(size/3, x+size*2/3, y+size*2/3);
    return;
}

int main()
{
    for(int i=1; i<2188; i++){
        for(int j=1; j<2188; j++){
            star[i][j]='-';
        }
    }
    
    int N;
    cin>>N;
    if(N==3){
        cout<<"***\n"<<"* *\n"<<"***";
        return 0;
    }
    
    solve(N, 1, 1);
    for(int i=1; i<=N; i++){
        for(int j=1; j<=N; j++){
            if(star[i][j]=='-') cout<<" ";
            else cout<<star[i][j];
        }
        cout<<"\n";
    }
}