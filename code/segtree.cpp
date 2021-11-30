#include <bits/stdc++.h>
using namespace std;
#define MOD 1000000007
typedef long long int ll;

#define INF 1e17
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
   scanf("%d",&t); \
   while (t--)
#define inp                    \
   for (int i = 0; i < n; i++) \
   {                           \
      ll j;                    \
      cin >> j;                \
      vec.pb(j);               \
   }
ll segtree [100001 *4];
ll vec[100001];
#define file_read(x, y)    \
   freopen(x, "r", stdin); \
   freopen(y, "w", stdout);
// void build(ll v,ll l,ll r)
// {
//     if(l==r)
//     {
//         segtree[v]=vec[l];return ;
//     }
//     else
//     {
//         ll m=(l+r)/2;
//         build(v*2,l,m);
//         build(v*2+1,m+1,r);
//         segtree[v]=segtree[v*2]+segtree[v*2+1];
//     }
    
// }
void buildmin(ll v,ll l,ll r)
{
   if(l==r)
    {
        segtree[v]=vec[l];return ;
    }
    else
    {
        ll m=(l+r)/2;
        buildmin(v*2,l,m);
        buildmin(v*2+1,m+1,r);
        segtree[v]=min(segtree[v*2],segtree[v*2+1]);
    }
    
}
ll sum( ll v,ll tl,ll tr,ll l,ll r)
{
if(l>r)
return 0;
if(l==tl&&r==tr)
return segtree[v];
ll tm=(tl+tr)/2;
return sum( v*2,tl,tm,l,min(r,tm))+sum(v*2+1,tm+1,tr,max(l,tm+1),r);
}
ll minfunc(ll v,ll tl,ll tr,ll l,ll r)
{
if(l>r)
return INF;
if(l==tl&&r==tr)
return segtree[v];
ll tm=(tl+tr)/2;
return min(minfunc(v*2,tl,tm,l,min(r,tm)),minfunc(v*2+1,tm+1,tr,max(l,tm+1),r));
}
void update( ll v, ll tl, ll tr, ll pos, ll new_val) {
    if (tl == tr) {
        segtree[v] = new_val;
    } else {
        ll tm = (tl + tr) / 2;
        if (pos <= tm)
            update( v*2, tl, tm, pos, new_val);
        else
            update( v*2+1, tm+1, tr, pos, new_val);
        segtree[v] = min(segtree[v*2] , segtree[v*2+1]);
    }
}

int main()
{
    ll i,j,k,n,m;
    scanf("%lld%lld",&n,&m);
    
    for(i=0;i<n;i++)
    {
       scanf("%lld",&j);vec[i]=j;
    }
buildmin(1,0,n-1);
while (m--)
{
ll s;
scanf("%lld%lld%lld",&s,&j,&k);
if(s==1)
{
    update(1,0,n-1,j,k);
}
else
{
   printf("%lld\n" ,minfunc(1,0,n-1,j,k-1));
}

}
}
