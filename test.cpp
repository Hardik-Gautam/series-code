#include<bits/stdc++.h>

// given array [2,3,4,9,1,4]
// find the sum of L to R index values 
using namespace std;
int main()
{
    int arr[]={2,3,4,9,1,4};
    int size = sizeof(arr)/sizeof(arr[0]);    
    int q=3,l,r;
    int count=0;
    while (q--)
    { cout<<"\nEnter Range\n";
        cin>>l;
        cin>>r;
        for(int i=l;i<=r;++i)
            count = count + arr[i];
        cout<<count;
        count=0;
    }
    

    return 0;
}