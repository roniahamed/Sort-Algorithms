#include<bits/stdc++.h>
using namespace std;


void display(vector<int> vm)
{
    for(int i=0; i<5; i++)
    {
        cout<<vm[i]<<" ";
    }
    cout<<endl;

}

int main()
{
    vector<int> ve;
    for( int i=0; i<5; i++)
    {
        int val;
        cin>>val;
        ve.push_back(val);
    }



    for(int i=0; i<5-1; i++)
    {
        for(int j=i+1; j<5; j++)
        {
            if(ve[i]>ve[j])
            {
                int temp = ve[i];
                ve[i] = ve[j];
                ve[j] = temp;
            }
            display(ve);
        }
        cout<<endl<<endl<<i<<endl<<endl;
    }


    return 0;
}
