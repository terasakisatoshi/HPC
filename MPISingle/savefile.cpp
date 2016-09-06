#include <iostream>
#include <fstream>

int main(void){
    const int SIZE=10;
    int array[SIZE];
    for (int i = 0; i < SIZE; ++i)
    {
        array[i]=i;
    }
    std::ofstream ofs("data.dat");
    for (int i = 0; i < SIZE; ++i)
    {
        ofs<<array[i]<<std::endl;
    }
    ofs.close();
}