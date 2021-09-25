import java.util.*;

public class statico 
{
    static 
    {   
        Scanner sc = new Scanner(System.in);

        int h = sc.nextInt();
        int b = sc.nextInt();

        if(((h>=0)&&(h<=100))&&((b>=0)&&(b<=100)))
        {
            System.out.println("Area = "+(h*b));
        }
        else if ((h<0)||(b<0)) 
        {
            System.out.println("java.lang.Exception: Breadth and height must be positive");
        }

       sc.close();
    }
    public static void main(String[] args)
    {

    }
    
}