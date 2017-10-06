#include <iostream>
#include <vector>

using namespace std;

#include "polyops.cpp"

int main()
{ 

  int Alen,Blen;

  cin >> Alen >> Blen;

  Poly A(Alen,0),B(Blen,0);

  for (auto& e : A)
     cin >> e;
  
  for (auto& e : B)
     cin >> e;

  /*for(int i = 0; i < A.size() || i < B.size(); i++) {
      cout << A[i] << " " << B[i] << endl;
  }*/

  for (auto e : add_poly(A,B))
     cout << e << " ";
  cout << endl;


  for (auto e : multiply_poly(A,B))
     cout << e << " ";
  cout << endl;  


}