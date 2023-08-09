#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
using namespace std;

string zero="0000";

int main()
{
    string str;
    cin>>str;
    int part=0;
    istringstream ss(str);
    vector<string> v, ans;
    string s;
    
    while(getline(ss, s, ':')){
        int len=s.size();
        if(len){
            part++;
            if(len<4){
                s=zero.substr(0, 4-len)+s;
            }
        }
        else if(len==0) s="-1";
        v.push_back(s);
    }
    
    for(int i=0; i<v.size(); i++){
        if(v[i]==""){
            v.erase(v.begin()+i);
        }
    }
    
    bool flag=false;
    for(int i=0; i<v.size(); i++){
        if(v[i]=="-1"){
            if(!flag){
                int num=8-part;
                while(num--){
                    ans.push_back(zero);
                }
                flag=true;
            }
        }
        else{
            ans.push_back(v[i]);
        }
    }
    
    for(int i=0; i<7; i++){
        cout<<ans[i]<<":";
    }
    cout<<ans[7];
}