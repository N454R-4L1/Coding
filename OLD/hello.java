import java.util.*;

public class hello 
{
    static Scanner sc = new Scanner(System.in);

    void un_cipher(final String str) {
        String t = "";
        char c, ch;
        for (int i = 0; i < str.length(); i++) 
        {
            ch = str.charAt(i);
            if(((int)ch ==  122 ))  
            {
              c = 'b';
            }
            else if( ((int)ch ==121))
            {
                c = 'a';
            }
            else if( ((int)ch == 32))
            {
                c = ' ';
            }
            else
            {
               c = (char) ((int) ch + 2);
            }

            t += c;

        }

        System.out.println(t);
    }

    public static void main(final String[] args) {
        System.out.println("String : ");
        final String txt = sc.nextLine();

        final hello h = new hello();
        h.un_cipher(txt);
     }
    
}