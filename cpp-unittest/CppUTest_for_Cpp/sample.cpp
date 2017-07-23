
#include "sample.h"

using namespace std;


int add(int a, int b)
{
	return a+b;
}

int mul(int a, int b)
{
	return a*b;
}

int mode(int a, int b)
{
	return a%b;
}


#ifndef CPPUTEST
int main(void)
{
	int a=25, b=10;
	add(a,b);
	mul(a,b);
	mode(a,b);
	return 0;
}
#endif