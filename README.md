# Economic_Algo_Matala7_Ques2

Given a function that represents a rule of choice. <br />
Function title: <br />
def choices (values: List [float]) → List [bool]: .. <br />
The function receives as input a vector of numbers representing the values of the players (in shekels). <br />
Returns as a Boolean vector output that returns, for each player, whether or not he is selected. <br />

I Wrote a function that represents the appropriate payment rule, <br />
according to Myerson's theorem.  <br />
Function title: <br />
def payments (values: List [float]) → List [float]: ... <br />
The function receives as input the values vector (as the previous function),  <br />
and returns the payments vector,In shekels, with an accuracy of one penny (NIS 01.0). <br />
If the rule of choice is not monotonic - the function payments throws an appropriate exception. <br />
<br />
I have tested my function on several different selection functions:<br />
The first function:<br />
Takes all the values that are over 7 <br />
input: <br />
[10, 9, 8, 7, 6, 5, 4] <br />
output: <br />
Payment of each one is= [7, 7, 7, 0, 0, 0, 0] <br />
<br />
<br />
The Second function: <br />
Takes the second max value - (not monotonic) <br />
 <br />
The Third function:<br />
Algorithm Chamdany A- from class. <br />
[10, 9, 8, 7, 6, 5, 4] <br />
Payment of each one is= [5, 5, 5, 5, 5, 0, 0] <br />

