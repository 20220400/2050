#include <stdio.h>
#include <stdlib.h>

int oddSumHelp(int count, int bound, int value)
{
	//fill in your code below
    //count-- number of values needed
    //bound-- upper bound of values
    //value-- total sum need to be this

    if (count==0 && value==0)
    {
        // printf("%i ",bound);
        return 1;
    }

    // count<0, bound<0 or bound=0,value<0,


    if (count<=0)
    {
        return 0;
    }
    if (bound<=0)
    {
        return 0;
    }
    if (value<0)
    {
        return 0;
    }

    if (oddSumHelp(count-1,bound-2,value-bound)==1)
    {
        printf("%i ",bound);
        return 1;
    }
    else{
        oddSumHelp(count,bound-2, value);
    }
    

    

    

	
// cc -o oddSum oddSum.c
// ./oddSum 12 50 200



}

//Do not change the code below
void oddSum(int count, int bound, int value)
{
    	if(value <= 0 || count <= 0 || bound <= 0) return;
    
    	if(bound % 2 == 0) bound -= 1;

    	if(!oddSumHelp(count, bound, value)) printf("No solutions.\n");
	else printf("\n");
}

int main(int argc, char *argv[])
{
	if(argc != 4) return -1;

	int count = atoi(argv[1]);
	int bound = atoi(argv[2]);
	int value = atoi(argv[3]);

	//oddSum(12,30,200);
	//oddSum(10,20,100);
	//oddSum(20,20,200);
	oddSum(count, bound, value);
	return 0;
}
