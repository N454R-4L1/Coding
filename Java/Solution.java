import java.util.*;

public class Solution {

    public static void main(String[] args) 
    {
        Scanner s = new Scanner(System.in);
        int i = s.nextInt();
        s.close();
        if((i>=1)&&(i<=100))
        {
         if((i%2!=0)||(i==1))
            {
                System.out.println("Weird");
            }
         else if((i>=2)&&(i<=5))
            {
                System.out.println("Not Weird");
            }
         else if((i>=6)&&(i<=20))
            {
                System.out.println("Weird");
            }
         else if(i>20)  
            {
                System.out.println("Not Weird");
            } 
        }        
    }
}