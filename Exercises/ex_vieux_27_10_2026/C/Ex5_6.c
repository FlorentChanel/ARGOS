#include <stdio.h>

int main (void)
    {

        int a, b ,c ,status;
        do
        {
            printf("enter 3 int : ");
            status = scanf("%d %d %d",&a,&b,&c);
            if (status == EOF)
            {
                return 1;
            }
            int x;
            while((x= getchar()) != '\n' && x != EOF);
        }
        while( status != 3);

        if(a > b && a > c)
        {
            printf("%d",a);
        }
        else if (b>c)
        {
            printf("%d",b);
        }
        else 
        {
            printf("%d",c);
        }

        //-------------------------------------------------
        int max=a;
        if (max<b)
         {
            max=b;
         }
         if (max<c)
         {
            max = c;
         }
         printf("%d",max);

         //--------------------------------

         int max1=a;
         max1=(max1<b && b>c)? b : (max1<c)? c : max1;
         printf("%d",max1);
         //----------------------------

         printf("%d",(a>b&&a>c)?a:(b>c)?b:c);
        return 0;
    }