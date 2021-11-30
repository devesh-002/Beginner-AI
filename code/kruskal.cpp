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
#define apes_together_strong          \
    ios_base::sync_with_stdio(false); \
    cin.tie(0);
vector<ll>parents(2e5+1,0),ranks(2e5+1,1);
struct edge
{
ll beg,end,w;
};
typedef struct edge edge;
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
bool compare(const edge &a, const edge &b)
{
    return a.w < b.w;
}
int main()
{    for(ll i=1;i<=2e5;i++) parents[i]=i;

   apes_together_strong
ll i,j,k,v,e;
cin>>v>>e;
vector<edge>edges;edge ed;
for(i=0;i<e;i++)
{ll w;
   cin>>j>>k>>w;
ed.beg=j;ed.end=k;ed.w=w;
edges.pb(ed);
}
sort(edges.begin(),edges.end(),compare);
ll size=0,cost=0;
for(i=0;i<e&&size<v;i++)
{
ll x=find(edges[i].beg),y=find(edges[i].end);
if(x!=y)
{
   Union(edges[i].beg,edges[i].end);
   cost+=edges[i].w;size++;
}
}
cout<<cost<<endl;
}
