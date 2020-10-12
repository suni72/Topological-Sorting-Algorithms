#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define ld long double
#define pb push_back
#define pf push_front
#define mp make_pair
#define F first
#define S second
#define mod 1000000007
#define INF INT_MAX
#define vl vector<ll>
#define vi vector<int>
#define pi pair<int,int>
#define pl pair<ll,ll>
#define vpl vector<pl>
#define vpi vector<pi>
#define ml map<ll,ll>
#define mi map<int,int>
#define m(a,b) map<a,b>
#define YesNo(f) if(f){cout<<"YES"<<endl;}else{cout<<"NO"<<endl;continue;}
#define setval(a,val) memset(a,val,sizeof(a)) 
#define fastIO ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0)
//    1 based node numbering 

const int mxN=200005;
int in[mxN];
vi adj[mxN];
vi sorted;   // for storing the toposort
bool topoSort(int n){
	// use priority queue for the smallest sort
	queue<int> q;
	for(int i=1;i<=n;i++){
		if(in[i]==0){
			q.push(i);
		}
	}
	while(!q.empty()){
		int node=q.front();
		q.pop();
		sorted.pb(node);
		for(auto i: adj[node]){
			in[i]--;
			if(in[i]==0){
				q.push(i);
			}
		}
	}
	// checking if the sort is valid, i.e. if the graph contains cycle 
	// all the nodes will not be present in the final sort
	return sorted.size()==n;
}

int main()
{
	fastIO;
//	freopen("input.txt","r",stdin);
//	freopen("output.txt","w",stdout);
	int t=1;
	// cin>>t;
	while(t--){
		int n,m,x,y;
		cin>>n>>m;
		for(int j=0;j<m;j++){
			cin>>x>>y;
			adj[x].pb(y);
			in[y]++;
		}
	}

return 0;
}