#include <iostream>
#include <string>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
    string str;
    int board[3][3];
    int o=0, x=0;
    bool owin, xwin, full=true;
    
    while(true){
        o=0; x=0;
        full=true; owin=false; xwin=false;
        
        cin>>str;
        if(str=="end") break;
        
        for(int i=0; i<3; i++){
            for(int j=0; j<3; j++){
                board[i][j]=str[3*i+j];
                if(board[i][j]=='O') o++;
                else if(board[i][j]=='X') x++;
                else full=false;
            }
        }
        
        if(o>x || x>o+1){
            cout<<"invalid\n";
            continue;
        }
        
        // 가로 확인
        for(int i=0; i<3; i++){
            if(board[i][0]=='O' && board[i][1]=='O' && board[i][2]=='O') owin=true;
            if(board[i][0]=='X' && board[i][1]=='X' && board[i][2]=='X') xwin=true;
        }
        
        // 세로 확인
        for(int i=0; i<3; i++){
            if(board[0][i]=='O' && board[1][i]=='O' && board[2][i]=='O') owin=true;
            if(board[0][i]=='X' && board[1][i]=='X' && board[2][i]=='X') xwin=true;
        }
        
        // 대각선 확인
        if(board[0][0]=='O' && board[1][1]=='O' && board[2][2]=='O') owin=true;
        if(board[0][0]=='X' && board[1][1]=='X' && board[2][2]=='X') xwin=true;
        
        if(board[0][2]=='O' && board[1][1]=='O' && board[2][0]=='O') owin=true;
        if(board[0][2]=='X' && board[1][1]=='X' && board[2][0]=='X') xwin=true;
        
        if(o==x && owin && !xwin) cout<<"valid\n";
        else if(x==o+1 && xwin && !owin) cout<<"valid\n";
        else if(!owin && !xwin && full) cout<<"valid\n";
        else cout<<"invalid\n";
    }
}