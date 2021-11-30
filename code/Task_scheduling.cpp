
#include <bits/stdc++.h>
using namespace std;

#define MOD 1000000007
typedef long long int ll;
//#define int ll
#define apes_together_strong          \
    ios_base::sync_with_stdio(false); \
    cin.tie(0);

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
#define tc    \
    int t;    \
    cin >> t; \
    while (t--)
#define file_read(x, y)     \
    freopen(x, "r", stdin); \
    freopen(y, "w", stdout);
// list<ll>l;set<ll>s;
bool cmp(const pair<ll,ll> &a,const pair<ll,ll> &b)
{
    return (a.second < b.second);
}
 
int main()
{
    apes_together_strong
vii vec,ans;
ll i,j,k,n;
cin>>n;
for(i=0;i<n;i++)
{
    cin>>j>>k;vec.pb({j,k});
}
sort(vec.begin(),vec.end(),cmp);
ans.pb(vec[0]);j=0;
for(i=1;i<n;i++)
{
if(ans[j].second<= vec[i].first)
{
    ans.pb(vec[i]);j++;
}
}
cout<<ans.size()<<"\n";
}
