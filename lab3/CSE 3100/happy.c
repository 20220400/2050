#include <stdio.h>
#include <stdlib.h>

int main()
{
	int n;

	printf("n = ");
	scanf("%d", &n);

	int m = n;
    int n1=0;
	//TODO
	//add code below
    while (m!=1 && m!=4)
    {
        n1=0;
        while(m > 0) //do till n greater than  0
        {
            
            int mod = m % 10;  //split last digit from number
            n1=n1+(mod*mod);
            
        
            m = m / 10;    //divide num by 10. num /= 10 also a valid one 

        }

        printf("%d\n",n1);
        

        m=n1;
        

    }
    


	if(n1==1) printf("%d is a happy number.\n", n);
	if(n1==4) printf("%d is NOT a happy number.\n", n);
    
	return 0;
}
