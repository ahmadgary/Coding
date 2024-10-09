import java.util.Scanner;

public class bilangan_prima {
    public static void main(String[] args) {
        try (Scanner input = new Scanner(System.in)) {
            System.out.print("Masukkan Angka: ");
            int angka = input.nextInt();
            String prima = "adalah bilangan prima";

            if (angka == 1 || angka == 0) {
                prima = "bukan bilangan prima";
            } else {
                for (int i = 2; i < angka; i++) {
                    if (angka % i == 0) {
                        prima = "bukan bilangan prima";
                        break;
                    }
                }
            }

            System.out.println(angka + " " + prima);
        }
    }
}
