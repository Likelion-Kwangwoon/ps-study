#include <iostream>
#include <algorithm>
using namespace std;

int L, C;
char arr[16];
char ans[16];
bool used[16];

bool promising(){
    bool flag=false;
    int v=0, c=0;
    char vowel[5]={'a', 'e', 'i', 'o', 'u'};
    for(int i=0; i<L; i++){
        bool isVowel=false;
        for(int j=0; j<5; j++){
            if(ans[i]==vowel[j]) isVowel=true;
        }
        if(isVowel) v++;
        else c++;
    }
    if(v>=1 && c>=2) flag=true;
    return flag;
}

void solve(int cnt, char num){
    if(cnt==L){
        if(promising()){
            for(int i=0; i<L; i++){
                cout<<ans[i];
            }
            cout<<"\n";
        }
        return;
    }
    for(int i=0; i<C; i++){
        if(!used[i] && arr[i]>=num){
            used[i]=true;
            ans[cnt]=arr[i];
            solve(cnt+1, arr[i]);
            used[i]=false;
        }
    }
}

int main()
{
    cin>>L>>C;
    for(int i=0; i<C; i++){
        cin>>arr[i];
    }
    sort(arr, arr+C);
    solve(0, arr[0]);
}