#include<iostream>
using namespace std;

int maxSubarray(int arr[],int size)
{
    int count=0,max = 0;
    for(int i=0;i<size;i++)
    {
        count = count + arr[i];
        if(count > max)
        max = count;
        if(count < 0)
        count = 0;
    }
    return max;
}

int main()
{
    int a[] = {-2, -3, 4, -1, -2, 1, 5, -3};
    int n = sizeof(a)/sizeof(a[0]);
    int result = maxSubarray(a,n);
    cout<<"maximum sub array "<<result;
}