// Author: HE-Arc

#ifndef EX_0029_TIME_H
#define EX_0029_TIME_H

// Standard includes

// Local includes
typedef struct
{
    int hh ;
    int mm ;
    int ss ;
} Time;
// Types

// Function prototypes
Time ex_0029_InitTime(int hh , int mm  ,int ss);
void ex_0029_PrintTime(Time t);
void ex_0029_Time(void);
#endif // EX_0029_TIME_H
