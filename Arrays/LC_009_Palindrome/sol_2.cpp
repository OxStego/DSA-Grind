 #include <iostream>
using namespace std;

 bool isPalindrome(long x) {
        long newint=0;
        long reminder=x;
    
        if( x%10==0 || x<0) return false;
        cout<<"hello";
        
         while(reminder>0){
             
            //reminder>0 gives length of number means last element of reversed number
              newint=newint*10+reminder%10;
              cout<<newint<<endl;
               reminder=reminder/10;
         }
          
          return x==newint ;
   }



int main(int argc, char const *argv[])
{
    // cout<<isPalidromeNumber(1111112111111);
    cout<<isPalindrome(1111112111111)<<endl;
    cout<<isPalindrome(121);
    return 0;
}
