#include<stdio.h>

int fun_max(int a,int b)
{
	if (a<b)
		return b;
	return a;
}

int main()
    {
        int a,b;
        printf("input two numbers:\n");
        printf("a=");
        scanf("%d",&a);
        printf("b=");
        scanf("%d",&b);
        printf("max=%d\n",fun_max(a,b) );
        return 0;
    }