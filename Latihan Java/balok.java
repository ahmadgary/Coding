import java.util.Scanner;

public class balok {
    public static void main(String[] args) {
        System.out.println("Menghitung Luas & Volume Balok");

        // Menggunakan try-with-resources untuk memastikan Scanner ditutup
        try (Scanner input = new Scanner(System.in)) {
            // Meminta input dari pengguna
            System.out.print("\nMasukkan Panjang: ");
            double panjang = input.nextDouble();

            System.out.print("Masukkan Lebar: ");
            double lebar = input.nextDouble();

            System.out.print("Masukkan Tinggi: ");
            double tinggi = input.nextDouble();

            // Menghitung luas dan volume balok
            double luas = (2 * panjang * lebar) + (2 * panjang * tinggi) + (2 * lebar * tinggi);
            double volume = panjang * lebar * tinggi;

            // Menampilkan hasil
            System.out.println("\nLuas Balok \t\t: " + luas);
            System.out.println("Volume Balok \t\t: " + volume);
        } // Scanner akan otomatis ditutup di sini
    }
}
