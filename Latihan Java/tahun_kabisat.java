import java.util.Scanner;

public class tahun_kabisat {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Menginput Tahun
        System.out.print("Tulis Sebuah Tahun: ");
        int tahun = scanner.nextInt();

        // Perulangan Pertama
        if (tahun % 4 == 0) {
            // Perulangan Kedua
            if (tahun % 100 == 0) {
                // Perulangan Ketiga
                if (tahun % 400 == 0) {
                    // Tergolong Tahun Kabisat
                    System.out.println(tahun + " adalah Tahun Kabisat");
                } else {
                    // Bukan Tergolong Tahun Kabisat
                    System.out.println(tahun + " bukan Tahun Kabisat");
                }
            } else {
                // Tergolong Tahun Kabisat
                System.out.println(tahun + " adalah Tahun Kabisat");
            }
        } else {
            // Bukan Tergolong Tahun Kabisat
            System.out.println(tahun + " bukan Tahun Kabisat");
        }

        // Close the scanner to avoid resource leak
        scanner.close();
    }
}
