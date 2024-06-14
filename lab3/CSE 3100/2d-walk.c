#include <stdio.h>
#include <stdlib.h>

double two_d_random(int n)
{

	//Fill in code below
	//When deciding which way to go for the next step, generate a random number as follows.
	//r = rand() % 4;
	//Treat r = 0, 1, 2, 3 as up, right, down and left respectively.

	//The random walk should stop once the x coordinate or y coordinate reaches $-n$ or $n$. 
	//The function should return the fraction of the visited $(x, y)$ coordinates inside (not including) the square.


    int x= (2*n+1);
    double holder=0.0;
    int point_1x=n;
    int point_2y=n;
    int alreadyvisited[x][x]; // makes an array of (2n-1) and (2n-1) size
    double total_steps=0.0;
    double all_steps=(2*n-1)*(2*n-1);


//
    for (int i=0;i<x;i++)
        {
        for(int j=0;j<x;j++)
            {
                alreadyvisited[i][j]=0;// This initializes the array with all 0
            }
        }
//    


//
    while (point_1x>0 && point_2y>0 && point_1x<2*n && point_2y<2*n)
    
    
    {
        // alreadyvisited[point_1x][point_2y]=1; // changes the 0 in the array to 1 to show we went in here
        int r = rand() % 4; // gives 0,1,2,3 randomly
        alreadyvisited[point_1x][point_2y]=1;
        if (r==0) // This step is going up so y+ is increasing
        {
            point_2y++;
            

        }
        if (r==1) // This step is going right so x+ is increasing
        {
            point_1x++;
            
        }
        if (r==2) // This step is going down so y- is decreasing
        {
            point_2y=point_2y-1;
        }
        if (r==3) // This step is going left so x- is decreasing
        {
            point_1x=point_1x-1;

        }
    }
    



    for (int i=0;i<x;i++)
        {
        for(int j=0;j<x;j++)
            {
                
                    holder+=alreadyvisited[i][j];
                 // this is the opp os the array hting before. we see how many points are touched
            }
        }

    return holder/all_steps;

    
}


//Do not change the code below
int main(int argc, char* argv[])
{

    int trials = 1000;
    int i, n, seed;
    if (argc == 2) seed = atoi(argv[1]);
    else seed = 12345;
    srand(seed);
    for(n=1; n<=64; n*=2)
    {
            double sum = 0.;
            for(i=0; i < trials; i++)
            {
                    double p = two_d_random(n);
                    sum += p;
            }
            printf("%d %.3lf\n", n, sum/trials);
    }
    return 0;
}
