# BIG-O NOTATION AND ALGORITHMS ANALYSIS

## Big-O notation explanation

Big O notation is used to analyze the efficiency of an algorithm as its input approaches inifinity, which means that as the size of the input grows, how drastically do the space or time requirements grow with it.
For example lets say that we have a dentist and she takes 30 minutes to treat one patient.As her line of patients increases , the time that it takes for her to treat all of the patients will scale linearly with the number of patients waiting in line.
This is because it always takes her a constant amount of time to treat each individual patient which is 30 minutes. This gives us a general understanding of how long our dentist would take to treat 10 patients, 20 patients or even 100,000 patients. This is beacuse since we know that the dentist takes a contant amount of time, which is 30 minutes to treat each patient, we can always calculate the amount of time it would take for her to treat any number of patients by multiplying the number of patients times 30 minutes.
With this in mind, we can categorize her efficiency as being linear O(n). where n is the number of patients.
The amount of work it takes for her to finish her work scales linearly or proportionally with the number of patients., We use the same technique to determine the efficiency of algorithms.
We can get a general idea of how functions time efficiency scales by categorizing a given functions efficiency the same way that we categorize the dentist efficiency

## ORDER OF GROWTH HIERARCHY

    O(1) => constant time
                |                                                          
               V
    O(log n) => logarithmic time
                |
               V
    O(n)=> linear time
                |
               V
    O(n log n)=> linearithmic time
                |
               V
    O(n ^ 2) => Quadratic time
                |
               V
    O(n ^ 3) => cubic time
                |
               V
    O(2 ^ n) => exponential
                |
               V
    O(n!) => factorial