#include <iostream>
using namespace std;
//issue how to handle part where 1001 if u remove x>newint as condition but they create more loop so bad TE 
   
bool isPalindrome(int x) {
        int newint=0;
        int reminder=x,i=1;
        if(x<=10) return false;
        if(x%10==0) return false;
         while( x>newint){
              
              newint=newint*10+reminder%10;
              cout<<"step:"<<i<<"  "<<newint<<endl;
              i++;
               reminder=reminder/10;
         }
          cout<<newint<<endl;

         if(newint==x) {
           
            return true;
         }
         
            return false;
        }


int main(){
    cout<<isPalindrome(1234567899);

}