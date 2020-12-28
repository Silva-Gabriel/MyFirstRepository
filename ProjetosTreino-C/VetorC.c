#include <stdio.h>
#include <stdlib.h>
int main()
{
    int X[10],i,num;
    
    for(i = 0;i < 10;i++)
    {
        scanf("%d",&num);
        X[i] = num;
    }
    for(i = 0;i < 10;i++)
    {
        if(X[i] == 0 || X[i] < 0)
        {
            X[i] = 1;
        }
        printf("X[%d] = %d\n",i,X[i]);
    }
    
}