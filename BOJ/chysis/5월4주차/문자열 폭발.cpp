#include <iostream>
#include <string>
#include <vector>
#include <stack>
using namespace std;

int main()
{
    vector<char> v;
    stack<pair<char, int>> stk;
    string s, bomb;
    int temp=0;
    cin>>s>>bomb;
    for(int i=0; i<s.length(); i++){
        if(stk.empty() && s[i]!=bomb[0]) {
            stk.push(make_pair(s[i], 0));
        }
        else if(s[i]==bomb[0]) {
            stk.push(make_pair(s[i], 1));
        }
        else if(stk.top().second!=0){
            if(s[i]==bomb[stk.top().second]){
                stk.push(make_pair(s[i], stk.top().second+1));
            }
            else if(s[i]==bomb[0]){
                stk.push(make_pair(s[i], 1));
            }
            else{
                stk.push(make_pair(s[i], 0));
            }
        }
        else{
            stk.push(make_pair(s[i], 0));
        }
        
        if(stk.top().second==bomb.length()){
            for(int j=0; j<bomb.length(); j++){
                stk.pop();
            }
        }
    }
    if(stk.empty()) cout<<"FRULA";
    else{
        while(!stk.empty()){
            v.push_back(stk.top().first);
            stk.pop();
        }
        for(int i=0; i<v.size(); i++){
            cout<<v[v.size()-i-1];
        }
    }
}