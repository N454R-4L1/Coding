import java.util.*;

public class arrayst
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int n;
        n = sc.nextInt();

        String st[] = new String[n+1];

        for (int i = 0; i <st.length; i++) 
        {   
            st[i] = sc.nextLine();
        }
        for (int i = 0; i <st.length; i++) 
        {   
            System.out.println(st[i]);
        }
        sc.close();
    }

}