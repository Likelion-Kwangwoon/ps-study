#include <iostream>
using namespace std;

int board[9][9];
bool flag=false;
bool rowUsed[9][10];
bool colUsed[9][10];
bool squareUsed[9][10];

void change(int i, int j, int num){
    rowUsed[i][num]=!rowUsed[i][num];
    colUsed[j][num]=!colUsed[j][num];
    squareUsed[3*(i/3)+(j/3)][num]=!squareUsed[3*(i/3)+(j/3)][num];
}

bool promising(int i, int j, int num){
    return !rowUsed[i][num] && !colUsed[j][num] && !squareUsed[3*(i/3)+(j/3)][num];
}

void solve(int i, int j){
    if(i==9){
        for(int a=0; a<9; a++){
            for(int b=0; b<9; b++){
                cout<<board[a][b];
            }
            cout<<"\n";
        }
        flag=true;
        return;
    }
    
    if(board[i][j]){
        if(j==8) solve(i+1, 0);
        else solve(i, j+1);
    }
    else{
        for(int a=1; a<=9; a++){
            if(promising(i, j, a)){
                board[i][j]=a;
                change(i, j, a);
                if(j==8) solve(i+1, 0);
                else solve(i, j+1);
                if(flag) return;
                board[i][j]=0;
                change(i, j, a);
            }
        }
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    char ch;
    for(int i=0; i<9; i++){
        for(int j=0; j<9; j++){
            cin>>ch;
            int num=ch-'0';
            board[i][j]=num;
            if(board[i][j]){
                rowUsed[i][num]=true;
                colUsed[j][num]=true;
                squareUsed[3*(i/3)+(j/3)][num]=true;
            }
        }
    }
    solve(0, 0);
}