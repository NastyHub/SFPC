#include <stdio.h>
int main(){
  long long int n,a,b,c,na;
  scanf("%lld",&n);
  scanf("%lld %lld %lld",&a,&b,&c);
  na=n/12;
  na*=a;
  na/=8;
  na*=b;
  na/=5;
  na*=c;
  printf("%lld",na);
}