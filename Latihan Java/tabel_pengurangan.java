import java.util.Scanner;

public class tabel_pengurangan {
    public static void main(String[] args) {
        try (Scanner input = new Scanner(System.in)) {
            System.out.print("Menampilkan Tabel Pengurangan dari: ");
            int angka = input.nextInt();

            for (int i = 1; i <= 10; i++) {
                System.out.println(angka + " - " + i + " = " + (angka - i));
            }

            System.out.print("Menampilkan Tabel Pengurangan dari: ");
            angka = input.nextInt();

            for (int i = 1; i <= 10; i++) {
                System.out.println(angka + " - " + i + " = " + (angka - i));
            }
        }
    }
}
