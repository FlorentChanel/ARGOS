#include <stdio.h>
int main (void)

{
    unsigned char x = 0xAA ;
    x = x && 0x3F;
    x = x && 0xFC;

    x = 0x99;
    x = x<< 2;
    x = x>> 5;
    printf("%d \n",x);


    unsigned int b= 0x03020100,b0,b1,b2,b3;
    b0 = b & 0xff;
    b1 = (b>>8) & 0xff;
    b2 = (b>>16) & 0xff;
    b3 = (b>>24) & 0xff;
    printf("%x \n",b0);
    printf("%x \n",b1);
    printf("%x \n",b2);
    printf("%x \n",b3);

    return 0;

}