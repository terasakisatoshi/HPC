#include <iostream>
using namespace std;
int main(int argc,char **argv){
    if(argc<=1){
        cout<<"error"<<endl;
    }
    else{
        cout<<"HelloWorld! arg "<<argv[1]<<" comes"<<endl;
    }
    return 0;
}