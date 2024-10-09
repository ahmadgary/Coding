import java.util.Scanner;

public class kerucut {
    public static void main(String[] args) {
        System.out.println("Menghitung Luas dan Volume Kerucut");

        try (Scanner scanner = new Scanner(System.in)) {
            System.out.print("Masukkan Jari-Jari: ");
            double r = scanner.nextDouble();

            System.out.print("Masukkan Tinggi: ");
            double t = scanner.nextDouble();

            System.out.print("Masukkan Luas Alas: ");
            double luasAlas = scanner.nextDouble();

            System.out.print("Masukkan Luas Selimut: ");
            double luasSelimut = scanner.nextDouble();

            double phi = 22.0 / 7.0;

            double volume = (1.0 / 3.0) * (phi * r * r * t);
            double luas = luasAlas + luasSelimut;

            System.out.println("\nLuasnya \t\t: " + luas);
            System.out.println("\nVolumenya \t\t: " + volume);
        }
    }
}