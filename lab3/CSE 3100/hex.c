
//In this assignment, we write code to convert decimal integers into hexadecimal numbers
//We pratice using arrays in this assignment
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

//convert the decimal integer d to hexadecimal, the result is stored in hex[]
void dec_hex(int d, char hex[])
{
	char digits[] ={'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B',
					'C', 'D', 'E', 'F'};

	int k = 0;
    int counter=1;
	//Fill in your code below
	//It should not be hard to obtain the last digit of a hex number
	//Then what?
	//If we are getting the digits in a reverse order, what should we do in the end?
    
	while (d>0)
	{
		int holder=d%16; //finds remainder
		hex[k]=digits[holder]; //adds remoander to the array[k] index
		d=d/16; //divides by 16 to remove the 16 power 1 each time. as int it acts as //
		k=k+1; // increement
        counter++;

	}
    char hell; // holder array to inverse
    int m=0;
    int n=k-1;
    for (m,n;m<n;m++,n--)
    {
        hell=hex[m]; // hold the value
        hex[m]=hex[n]; //swap the value of one side
        hex[n]=hell; //swap value of other side

    
    }
    


	//Make sure the last character is a zero so that we can print the string correctly
	hex[k] = '\0';
}


// Do not change the code below
int main()
{
	int d;
	char hex[80];
    char ye[80];
	
	printf("Enter a positive integer : ");
	scanf("%d", &d); 
	dec_hex(d, hex);
	printf("%s\n", hex);
	return 0;
}