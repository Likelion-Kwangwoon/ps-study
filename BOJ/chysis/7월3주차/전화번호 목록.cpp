#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

int main()
{
    int T, N;
    cin>>T;
    for(int i=0; i<T; i++){
        cin>>N;
        string s;
        bool flag=true;
        vector<string> tem;
        for(int j=0; j<N; j++){
            cin>>s;
            tem.push_back(s);
        }
        sort(tem.begin(), tem.end());
        for(int j=0; j<tem.size()-1; j++){
            if(tem[j].length()>tem[j+1].length()) continue;
            if(tem[j]==tem[j+1].substr(0, tem[j].length())){
                flag=false;
                break;
            }
        }
        if(!flag) cout<<"NO\n";
        else cout<<"YES\n";
    }
}