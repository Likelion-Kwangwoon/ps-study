#include <iostream>
#include <vector>
using namespace std;

struct Node{
    char left, right;
};

vector<Node> v(26);

void preorder(char node){
    if(node=='.') return;
    
    cout<<node;
    preorder(v[node].left);
    preorder(v[node].right);
}

void inorder(char node){
    if(node=='.') return;
    
    inorder(v[node].left);
    cout<<node;
    inorder(v[node].right);
}

void postorder(char node){
    if(node=='.') return;
    
    postorder(v[node].left);
    postorder(v[node].right);
    cout<<node;
}

int main()
{
    int N;
    char root, l, r;
    cin>>N;
    for(int i=0; i<N; i++){
        cin>>root>>l>>r;
        v[root].left=l;
        v[root].right=r;
    }
    preorder('A');
    cout<<"\n";
    
    inorder('A');
    cout<<"\n";
    
    postorder('A');
}