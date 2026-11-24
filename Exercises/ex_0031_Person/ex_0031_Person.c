// Author: HE-Arc

// Standard includes
#include <stdio.h>
#include <string.h>

// Local includes
#include "ex_0031_Person.h"

// Function definitions
// TODO: implement ex_0031_Person
void ex_0031_Person(void)
{
    Person tab[10]= {
        {"Knuth", "Donald", 1938},
        {"Kernighan", "Brian", 1942},
        {"Ritchie", "Dennis", 1941},
        {"Thompson", "Ken", 1943},
        {"Minsky", "Marvin", 1927},
        {"Dijkstra", "Edsger", 1930},
        {"Stroustrup", "Bjarne", 1950}
    };
    int nb=0;
    while (tab[nb].Nom[0] != '\0')
    {
        nb++;
    }
    printf("%d Persons\n",nb);
    //
    printf("Persons less than 80 years old:\n");
    for(int i=0; i < nb; i++)
    {
        if (tab[i].birthYear > (2020-80))
        {
            printf("%s %s %d years\n",tab[i].Prenom,tab[i].Nom,(2020-tab[i].birthYear));
        }
    }
    //
    printf("\nAlphabetic order:\n");
    int first = 0;
    for (int i=1; i<nb ; i++)
    {
        if (0 < strcmp(tab[first].Nom,tab[i].Nom))
        {
            first = i;
        }
    }
    printf("The first is: %s\n",tab[first].Nom);
    int last = 0;
    for (int i=1; i<nb ; i++)
    {
        if (0 > strcmp(tab[last].Nom,tab[i].Nom))
        {
            last = i;
        }
    }
    printf("The last is: %s\n",tab[last].Nom);
}