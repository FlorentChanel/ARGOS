 #include <stdio.h>
  int main(void)
  {
    int i, j, x = 0 ;
    for (i = 0 ; i < 5 ; ++i)
    for (j = 0; j < i; ++j)
    {
      switch(i + j - 1)
      {
      case -1 :
      case 0  : x += 1;
                break;
      case 1  :
      case 2  :
      case 3  : x += 2;
                break;
      default : x += 3;
      }
   printf("%d ", x);
   }
   printf("\nx = %d\n", x);
   return 0;
}
//1 3 5 7 9 12 14 17 20 23
//x = 23
//