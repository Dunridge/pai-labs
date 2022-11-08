
'''

This exercise is to help teach the concepts of limits of sequences.
For a specific sequence like a_n = 1 + 1/n^(3/2), create lists containing:

- a few tens of integers 'n';
- a few tens of corresponding values a_n;
- a few tens of corresponding values of |a_n - g|

Allow the user to introduce her or his value of epsilon
and let the program find such an N that
|a_n - g| < epsilon if n > N.

Use 'input' or 'raw_input' to allow the user to provide their values, e.g.
eps = input("Please provide your epsilon").

'''

# TODO: figure out what does the g stand for

#   g is the limit of a sequence (for each series 1/n, g = 0 1 + 1/n g = e (n)^(1/n)=1)