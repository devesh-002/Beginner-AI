#include <stdio.h>
void merge(int arr[],int first,int mid,int last,int n)
{
int i=first,mi=mid+1,first1=first,arr1[n];
for(i=first;first1<=mid&&mi<=last;i++)
{
    if(arr[first1]<=arr[mi])
    {
        arr1[i]=arr[first1];first1++;
    }
    else
    {
        arr1[i]=arr[mi];mi++;
        }
}
int k;
if (first1 > mid)
    {
        for (k = mi; k <= last; k++)
        {
            arr1[i] = arr[k];
            i++;
        }
    }
    else
    {
        for (k = first1; k <= mid; k++)
        {
             arr1[i] = arr[k];
             i++;
        }
    }
 
    for (k = first; k <= last; k++)
    {
        arr[k] = arr1[k];
    }
}

void part(int arr[],int first,int last,int n)
{
int mid;
if(first<last)
{
    mid=(first+last)/2;
    part(arr,first,mid,n);
    part(arr,mid+1,last,n);
    merge(arr,first,mid,last,n);
}    
}
//n=length of array

int main()
{
int arr[]={5,1,3,4,1,2};
part(arr,0,5,6);
int i;for(i=0;i<6;i++) printf("%d ",arr[i]);
printf("\n");
}
