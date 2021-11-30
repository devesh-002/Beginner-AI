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
#define tc   \
   int t;    \
   cin >> t; \
   while (t--)
#define file_read(x, y)    \
   freopen(x, "r", stdin); \
   freopen(y, "w", stdout);
#define fightFight cin.tie(0)->sync_with_stdio(0)
//long double dp[3001][3001];
int main()
{
ll i,j,k,n;
cin>>n;
vector <ll> vec,dp;vector<ll>::iterator it;
for(i=0;i<n;i++){cin>>j;vec.pb(j);}dp.pb(vec[0]);
for(i=1;i<n;i++)
{
it=lower_bound(dp.begin(),dp.end(),vec[i]);
if(it==dp.end())
{
   dp.push_back(vec[i]);continue;
}
*it=vec[i];
}
cout<<dp.size()<<endl;
}
