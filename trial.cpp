#include <iostream>
//#include <string>

using namespace std;

int add();
int main()
{
//int add = 0; 
//int a,b;
  // add = add();    
    return ::add();
}

// Function definition
int add()
{
    int add,x,y;
	//string name;
    //cout<<"Enter numbers";
    cin>>x>>y;
    add = x + y;
	//cout<<add;
    // Return statement
    return add;
}