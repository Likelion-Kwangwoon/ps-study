#include <iostream>
using namespace std;

int map[101][101];

int main()
{
    int N, L;
    cin>>N>>L;
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            cin>>map[i][j];
        }
    }
    int ans=N*2;
    for(int i=0; i<N; i++){
        int tem_len=1;
        bool desc=false;
        bool solved=false;
        for(int j=0; j<N-1; j++){
            if(map[i][j]==map[i][j+1]){
                tem_len++;
                if(desc && solved) desc=false;
            }
            else if(map[i][j]+1==map[i][j+1]){
                desc=false;
                if(tem_len<L){
                    ans--;
                    break;
                }
                else tem_len=1;
            }
            else if(map[i][j]-1==map[i][j+1]){
                if(desc && !solved){
                    ans--;
                    break;
                }
                tem_len=1;
                desc=true;
                solved=false;
            }
            else{
                ans--;
                break;
            }
            
            if(j!=N-2 && desc){
                if(tem_len>=L){
                    tem_len-=L;
                    solved=true;
                }
            }
            
            if(j==N-2 && desc){
                if(tem_len<L){
                    ans--;
                    break;
                }
            }
        }
    }

    for(int i=0; i<N; i++){
        int tem_len=1;
        bool desc=false;
        bool solved=false;
        for(int j=0; j<N-1; j++){
            if(map[j][i]==map[j+1][i]){
                tem_len++;
                if(desc && solved) desc=false;
            }
            else if(map[j][i]+1==map[j+1][i]){
                desc=false;
                if(tem_len<L){
                    ans--;
                    break;
                }
                else tem_len=1;
            }
            else if(map[j][i]-1==map[j+1][i]){
                if(desc && !solved){
                    ans--;
                    break;
                }
                tem_len=1;
                desc=true;
                solved=false;
            }
            else{
                ans--;
                break;
            }
            
            if(j!=N-2 && desc){
                if(tem_len>=L){
                    tem_len-=L;
                    solved=true;
                }
            }
            
            if(j==N-2 && desc){
                if(tem_len<L){
                    ans--;
                    break;
                }
            }
        }
    }
    cout<<ans;
}