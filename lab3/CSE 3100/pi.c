#include <stdio.h>
#include <stdlib.h>


int main()
{
	int n, i,j;

	printf("n = ");
	scanf("%d", &n);

	int m = n;
	double pi = 0.;
    double eugh=1.;

	//TODO
	//add code below 
    for(i=0;i<m+1;++i)
    {
        for (j=0;j<i+1;++j)
        {
            if(j==0) eugh=1.;
            else eugh=eugh*16.;
        }

        
        pi= pi + 
        (
            (
                (4./((8.*i)+1.))
                    -(2./((8.*i)+4.))
                    -(1./((8.*i)+5.))
                    -(1./((8.*i)+6.))
                    )
                    *(1./eugh)
                    );
        




    }
	







	printf("PI = %.10f\n", pi);
	return 0;
}
