import java.io.*;
import java.util.*;

public class Solution {
    static int findTerm(int n) 
{ 
    if (n == 1) 
    return n; 
  
    else { 
    int term = 7; 
    for (int i = 2; i <= n; i++) 
        term = term * 2 + (i - 1); 
  
    return term; 
    } 
} 

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc=new Scanner(System.in);
        int n = sc.nextInt(); 
        System.out.print(findTerm(n));
    }
}