// Problem link:- https://atcoder.jp/contests/dp/submissions/23918553
#include <bits/stdc++.h>
using namespace std;

#define MOD 1000000007
typedef long long int ll;
//#define int ll 
 
typedef pair<ll, ll> ii;
typedef vector<ll> vi;
typedef vector<bool> vb;
typedef vector<vi> vvi;
typedef vector<ii> vii;
typedef vector<vii> vvii;
#define ff first
#define ss second
#define pb push_back
#define all(s) s.begin(), s.end()
#define tc int t; cin>>t; while(t--)
#define file_read(x,y) freopen(x, "r", stdin); \
                        freopen(y, "w", stdout);
#define fightFight cin.tie(0) -> sync_with_stdio(0)
ll largest_digit(ll n) {
   ll max = n % 10; //assume that last digit is the smallest
   n /= 10; //to start from the second last digit
   while (n != 0) {
      if (max < n % 10)
         max = n % 10;
      n /= 10;
   }
   return max;
}

vector <ll> dp(100001,0);
vector<vector<ll>> adj(100001);
void dfs(ll x)
{ ll i;
   for(i=0;i<adj[x].size();i++)
   {
      if(dp[adj[x][i]]!=0){
      dp[x]=max(dp[x],dp[adj[x][i]]+1);continue;
      }
      else
      {  dfs(adj[x][i]);
      dp[x]=max(dp[x],(dp[adj[x][i]]+1));}
   }
}
int main()
{
   ll i,j,k,n,m,ans=0;
   cin>>n>>m;
   for(i=0;i<m;i++)
   {
      cin>>j>>k;
      adj[j].push_back(k);
   }
   for(i=1;i<=n;i++) dfs(i);
   for(i=1;i<=n;i++)
   {
ans=max(ans,dp[i]);
   }
   cout<<ans<<endl;
}
