#include <stdio.h>
int main(void)
{
        
    double x,total,average,c;

    

    c = 1;



    while (scanf("%lf", &x) == 1) {  // pay attention to %lf

    total=total+x;
            
    average= total/c;
    c++;
    printf("Total=%f Average=%f\n", total, average); // pay attention to %f
    };

    // total=total+i;
    // checker+=1
    // average= total/checker
}