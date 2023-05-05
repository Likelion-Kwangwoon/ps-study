#include <iostream>
#include <string>
using namespace std;

int main()
{
    string board;
    cin>>board;
    
    int len=board.length();
    string ans="";
    
    int i=0;
    while(i<len){
        if(len>=i+4){
            if(board[i]=='X' && board[i+1]=='X' && board[i+2]=='X' && board[i+3]=='X'){
                ans+="AAAA";
                i+=4;
            }
            else if(board[i]=='X' && board[i+1]=='X'){
                ans+="BB";
                i+=2;
            }
            else if(board[i]=='.'){
                ans+=".";
                i++;
            }
            else{
                cout<<-1;
                return 0;
            }
        }
        else if(len>=i+2){
            if(board[i]=='X' && board[i+1]=='X'){
                ans+="BB";
                i+=2;
            }
            else if(board[i]=='.'){
                ans+=".";
                i++;
            }
            else{
                cout<<-1;
                return 0;
            }
        }
        else{
            if(board[i]=='X'){
                cout<<-1;
                return 0;
            } else{
                ans+=".";
                i++;
            }
        }
    }
    for(int i=0; i<ans.length(); i++){
        cout<<ans[i];
    }
}