// Timing Code
// 
// This is a simple example of using the clock() function of <ctime>
// to measure how long a code block took to run.
//

#include <iostream>
#include <ctime>

using namespace std;

int main()
{
	
	clock_t start_clock,end_clock;

	start_clock = clock();  // Timing starts here

	signed int i = 0;

	while ( i < 1'000'000'000 ) 
	{
		 i++;
	}

	end_clock = clock();    // Timing stops here
	

	double seconds = (double)(end_clock-start_clock) / CLOCKS_PER_SEC;
    

    cout << "counting to one billion took " << seconds << " seconds" << endl;

}