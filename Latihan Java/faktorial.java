import java.util.Scanner;

public class faktorial {
    public static void main(String[] args) {
        try (Scanner input = new Scanner(System.in)) {
            System.out.print("Masukkan nilai: ");
            int n = input.nextInt();
            long faktorial = 1;

            for (int i = 1; i <= n; i++) {
                faktorial *= i;
            }

            System.out.println(n + "! = " + faktorial);
        }
    }
}
