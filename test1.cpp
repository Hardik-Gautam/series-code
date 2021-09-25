#include<bits/stdc++.h>
using namespace std;

// Befor using two pointer alogrithm we must be care
// that an array must be sort 

int main()
{
    int n,flag;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        if(i==0||i==1)
        continue;
        
        flag=1;
        
        for (int j = 2; j <= i/2; j++)
            if(i%j==0)
            {
                flag=0;
                break;
            }
    
        if(flag==1)
        cout<<i<<" ";
    }


    return 0;
}