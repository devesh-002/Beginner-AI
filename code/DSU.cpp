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
#define inp                    \
   for (int i = 0; i < n; i++) \
   {                           \
      ll j;                    \
      cin >> j;                \
      vec.pb(j);               \
   }

#define file_read(x, y)    \
   freopen(x, "r", stdin); \
   freopen(y, "w", stdout);
#define fightFight cin.tie(0)->sync_with_stdio(0)
//long double dp[3001][3001];

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

vector<ll>parents(1e5+1,0),ranks(1e5+1,1);

ll find(ll x)
{
    if(parents[x]!=x)
    {
        parents[x]=find(parents[x]);
    }
    return parents[x];
}
ll Union(ll x,ll y)
{
ll xset=find(x);
ll yset=find(y);
if(xset==yset)
return 0;
  if (ranks[xset] < ranks[yset]) {
            parents[xset] = yset;
        }
        else if (ranks[xset] > ranks[yset]) {
            parents[yset] = xset;
        }
  
    
        else {
            parents[yset] = xset;
            ranks[xset] = ranks[xset] + 1;
        }
return 0;
}

int main()
{string s;
    ll n,m;
    cin>>n>>m;
    for(ll i=0;i<1e5;i++) parents[i]=i;

while(m--)
{ll x,y;
    cin>>s>>x>>y;
    if(s=="union")
    {
Union(x-1,y-1);
    }
    else
    {
        if(find(x-1)==find(y-1))cout<<"YES\n";
        else cout<<"NO\n";
    }
    
}
}
