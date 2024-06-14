#include <stdio.h>
int main(void)
{
    int i, j;
    i=0;
    printf("Hello, World!\n");
    while (i<200)
    {
    j=j+i;
    i=i+2;
    }
    printf("%d",j);
    return 0;
}
