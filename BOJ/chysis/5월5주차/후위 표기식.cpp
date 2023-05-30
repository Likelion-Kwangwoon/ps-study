#include <iostream>
#include <string>
#include <stack>
using namespace std;

stack<char> stk;
char ans[101];
int p=0;

int main()
{
    string s;
    cin>>s;
    for(int i=0; i<s.length(); i++){
        if(0<=s[i]-'A' && s[i]-'A'<=25){
            ans[p++]=s[i];
        }
        else {
            if(s[i]=='(')
                stk.push(s[i]);
            else if(s[i]=='*' || s[i]=='/'){
                while(!stk.empty() && (stk.top()=='*' || stk.top()=='/')){
                    ans[p++]=stk.top();
                    stk.pop();
                }
                stk.push(s[i]);
            }
            else if(s[i]=='+' || s[i]=='-'){
                while(!stk.empty() && stk.top()!='('){
                    ans[p++]=stk.top();
                    stk.pop();
                }
                stk.push(s[i]);
            }
            else if(s[i]==')'){
                while(!stk.empty() && stk.top()!='('){
                    ans[p++]=stk.top();
                    stk.pop();
                }
                stk.pop();
            }
        }
    }
    while(!stk.empty()){
        ans[p++]=stk.top();
        stk.pop();
    }
    cout<<ans;
}