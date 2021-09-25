import java.util.Scanner;
import java.io.*;
public class strings
{
    public static void main(String[] args)
    {  
        Scanner sc = new Scanner(System.in); 
        System.out.print("Enter : ");
        String s = sc.nextLine();
        // StringBuffer st = new StringBuffer(s);
        // st.reverse();
        for(int i = s.length()-1;i>=0;i--)
        {
            char ch = s.charAt(i);
            System.out.print(ch+" ");
        }
        sc.close();
    }
}