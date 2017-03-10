# Palindrome

My way to get the biggest palyndrome in a given string.  
(easy to write solution but not optimal at the moment)

Todo: 
- optimize `is_pal` which is around O(n²). Should be a O(n/2) function by comparing start of the string to the end directly.
- optimize `biggest_pal` function by checking directly with is_pal and then test the next etc.. instead of building the whole list of string before testing
