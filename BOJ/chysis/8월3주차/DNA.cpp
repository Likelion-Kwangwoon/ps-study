#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<string> v;
string ans;
int hamDis=0;

int main()
{
    int N, M;
    cin>>N>>M;
    for(int i=0; i<N; i++){
        string str;
        cin>>str;
        v.push_back(str);
    }
    for(int i=0; i<M; i++){
        int DNA[4]={0,};
        for(int j=0; j<N; j++){
            if(v[j][i]=='A') DNA[0]++;
            else if(v[j][i]=='C') DNA[1]++;
            else if(v[j][i]=='G') DNA[2]++;
            else DNA[3]++;
        }
        int idx, m=-1;
        for(int j=0; j<4; j++){
            if(m<DNA[j]){
                idx=j;
                m=DNA[j];
            }
        }
        if(idx==0) ans+="A";
        else if(idx==1) ans+="C";
        else if(idx==2) ans+="G";
        else ans+="T";
        hamDis+=N-m;
    }
    cout<<ans<<"\n"<<hamDis;
}