#include <stdio.h>
int main()
{
    int vet[3][3],i,j;
    
    for(i = 0;i < 3;i++)
    /* ↓ enquanto for verdade ficará no looping,depois
    adiciona++ na variável i e começa tudo novamente ↓ */
        for(j = 0; j < 3;j++)
        {
            printf("Linha[%d] Coluna[%d]:  ",i,j);
            scanf("%d",&vet[i][j]);
        }
        for(i = 0;i < 3;i++)
            for(j = 0; j < 3;j++)
            {
                if(i == 0)
                {
                    printf("%d\t",vet[i][j]);
                    if(j == 2)
                        printf("\n");
                }
                if(i == 1)
                {
                    printf("%d\t",vet[i][j]);
                    if(j == 2)
                        printf("\n");
                }
                if(i == 2)
                {
                    printf("%d\t",vet[i][j]);
                    if(j == 2)
                        printf("\n");
                }
            }
}
