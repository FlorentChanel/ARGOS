#include <stdio.h>
#include <math.h>

int main (void)
    {

        int a, b ,c ,status;
        printf("Compute solutions of an equation of the form ax^2 + bx + c = 0 \n");
        do
        {
            printf("Please enter coefficients a, b, and c: ");
            status = scanf("%d %d %d",&a,&b,&c);
            if (status == EOF)
            {
                return 1;
            }
            int x;
            while((x= getchar()) != '\n' && x != EOF);
        }
        while( status != 3);

        double x1, x2;
        if (a == 0 && b == 0 && c == 0)
        {
             printf("Any real is solution of this equation.");
        }
        else if(a == 0 && b == 0)
        {
            printf("This equation has no real solution.");
        }
        else if(a == 0)
        {
            x1 = -c/b;
            printf("The real solutions of this equation are: \nx1 = %.4f",x1);
        }
        else
        {
            if ((pow(b,2)-4*a*c)<0)
            {
                printf("This equation has no real solution.");
            }
            else
            {
                x1 = ((-b + sqrt(pow(b,2)-(4*a*c)))/(2*a));
                x2 = ((-b - sqrt(pow(b,2)-(4*a*c)))/(2*a));
                printf("The real solutions of this equation are: \nx1 = %.4f \nx2 = %.4f",x1,x2);
            }
        }
        return 0;
    }
