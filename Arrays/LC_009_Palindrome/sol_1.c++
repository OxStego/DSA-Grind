#include <iostream>
using namespace std;

bool isPalidromeNumber(long x){
            long reversed=0;
            while (x>reversed)
            {
                reversed=reversed*10 + x%10;
                x=x/10;
            }
            return x==reversed || x==reversed/10;
            
}


int main(int argc, char const *argv[])
{
    // cout<<isPalidromeNumber(1111112111111);
    cout<<isPalidromeNumber(111111211111);
    return 0;
}
