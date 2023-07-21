#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int K;
char arr[10];
int ans[11];
bool visited[11];
vector<string> v;

void solve(int cnt) {
    if(cnt==K+1){
        string s="";
        for(int i=0; i<K+1; i++){
            s+=ans[i]+'0';
        }
        v.push_back(s);
        return;
    }
    for(int i=0; i<=9; i++){
        if(!visited[i]){
            visited[i]=true;
            ans[cnt]=i;
            if(cnt>=1){
                if(arr[cnt-1]=='<'){
                    if(ans[cnt-1]<ans[cnt]){
                        solve(cnt+1);
                    }
                }
                else{
                    if(ans[cnt-1]>ans[cnt]){
                        solve(cnt+1);
                    }
                }
            }
            else{
                solve(cnt+1);
            }
            visited[i]=false;
        }
    }
}

int main() {
    cin>>K;
    for(int i=0; i<K; i++){
        cin>>arr[i];
    }
    solve(0);
    sort(v.begin(), v.end());
    cout<<v[v.size()-1]<<"\n"<<v[0];
}