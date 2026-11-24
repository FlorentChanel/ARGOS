// Author: HE-Arc

// Standard includes
#include <stdio.h>

// Local includes
#include "ex_0027_Array2DSum.h"

// Function definitions
// TODO: implement ex_0027_Array2DSum
void ex_0027_Array2DSum(void)
{
    int tab[50][50];
    int status;
    int lines;
    int columns;

    do
    {
        printf("Nb lines (max.50): ");
        status = scanf(" %d",&lines);
        if (status == EOF)
        {
            return;
        }
        int x;
        while((x= getchar()) != '\n' && x != EOF);

    }
    while(status != 1 || lines < 0 || lines > 50);

    do
    {
        printf("Nb columns (max.50): ");
        status = scanf(" %d",&columns);
        if (status == EOF)
        {
            return;
        }
        int x;
        while((x= getchar()) != '\n' && x != EOF);

    }
    while(status != 1 || columns < 0 || columns > 50);


    for(int i=0; i < lines ; i++)    
    {
        for(int j=0; j < columns; j++)
        {
            do
            {
                printf("array[%d][%d]: ",i,j);
                status = scanf(" %d",&tab[i][j]);
                if (status == EOF)
                {
                    return;
                }
                int x;
                while((x= getchar()) != '\n' && x != EOF);
            }
            while(status != 1);
        }
    }
 
    int Sum =0;
    for(int i=0; i < lines ; i++)
    {
        for(int j=0; j < columns; j++)
        {
            Sum = Sum + tab[i][j];
        }
    }
    printf("Total sum: %d\n",Sum);
}