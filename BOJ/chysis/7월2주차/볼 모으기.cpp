#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
    int N;
    string s;
    cin>>N>>s;
    
    int b=0, r=0, cnt=0;
    for(int i=0; i<s.length(); i++){
        if(s[i]=='R') r++;
        else b++;
    }
    int ans=min(b, r);
    
    for(int i=0; i<s.length(); i++){
        if(s[i]!=s[0]) break;
        cnt++;
    }
    if(s[0]=='R') ans=min(ans, r-cnt);
    else ans=min(ans, b-cnt);
    
    cnt=0;
    
    for(int i=s.length()-1; i>=0; i--){
        if(s[i]!=s[s.length()-1]) break;
        cnt++;
    }
    if(s[s.length()-1]=='R') ans=min(ans, r-cnt);
    else ans=min(ans, b-cnt);
    cout<<ans;
}