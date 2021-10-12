import java.io.IOException;
import java.util.Scanner; 

public class area
 {
 
    public static void main(String[] args) throws IOException
    {   
        double pi = 3.14159; 
        Scanner sc = new Scanner(System.in);
        double r = sc.nextDouble();
        
        double area = pi*r*r;
        
        System.out.println("A="+(String.format("%.4f", area)));
        sc.close();
    }
 
}