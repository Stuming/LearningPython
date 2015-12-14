#include<stdio.h>

int main()
    {
        int a,b,max;
        printf("input two numbers:\n");
        printf("a=");
        scanf("%d",&a);
        printf("b=");
        scanf("%d",&b);
        max=a;
        if (max<b)
            max=b;
        printf("max=%d\n",max );
        return 0;
    }