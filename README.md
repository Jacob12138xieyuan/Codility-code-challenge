# Codility-code-challenge

We consider alphabet with only three letters: "a","b" and "c". A string is called diverse if no three consecutive letters are the same. In other words, a diverse string may not contain any of strings "aaa","bbb" or "ccc".

Write a function:
  def solution(A, B, C)
  
that,given three integers A, B and C, returns any longest possible diverse string containing at most A letters 'a', at most B letters 'b' and at most C letters 'c'. If there is no possibility of building any string, return empty string.
 
Example:
1. Given A = 6, B = 1 and C = 1, your function may return "aabaacaa". Note that "aacaabaa" would also be a correct answer. Your function may return any correct answer.

Assume that:
  A,B and C are integers within the range [0..100];
  A+B+C>0
