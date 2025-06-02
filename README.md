## Lab 1.4

### Introduction
The purpose of this lab is to learn how to access data from an API using pagination in Python. 

### Part 1
Using the same API from Lab 1.3, get a token and authenticate to the API. Verify this by hitting `/people`. Do this in Postman first. 

### Part 2
Add query string params `offset` and `limit` to the call in order to get a subset of the results back.  Note here that the API is set to a max number of **50** results. Do this in Postman first. 

### Part 3
You have now proven that the API is accessible. Checking your code first in Postman helps you determine if it is the API that is not working versus your code.

Now repeat Parts 1 and 2 using Python. 

### Part 4
Once can read data from the API using Python, save the data to a `.json` file 10 records at a time. Do not hold any more than 10 records in memory at once. 

### Part 5 
Instead of writing this to a json file, reformat to write to a `.csv` file still holding only 10 records at a time in memory. 
