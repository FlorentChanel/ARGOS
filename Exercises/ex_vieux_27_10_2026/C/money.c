 #include <stdio.h>
 #include <math.h>

 int main(void)
 {
    float money;
    printf("What is your initial asset?: \n");
    scanf("%f",&money);

    float rate;
    printf("What is your yearly interest rate (in pourcent)?: \n");
    scanf("%f",&rate);

    int temps;
    printf("Duration in years?: \n");
    scanf("%d",&temps);

    printf("After %d years, your assets (with interest) will be %.2f: \n",temps,money * pow(1+(rate/100),temps));

    bool a = !true;
    printf("%b \n",a);
    //double par defaut
    return 0;
 }
