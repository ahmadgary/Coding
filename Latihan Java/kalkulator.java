import java.util.InputMismatchException;
import java.util.Scanner;

public class kalkulator {
    public static void main(String[] args) {
        System.out.println("Kalkulator");
        System.out.println("1. Penjumlahan");
        System.out.println("2. Pengurangan");
        System.out.println("3. Perkalian");
        System.out.println("4. Pembagian");

        try (Scanner scanner = new Scanner(System.in)) {
            System.out.print("Masukkan Pilihan (1/2/3/4): ");
            int p = scanner.nextInt();

            System.out.print("Masukkan Bilangan Pertama: ");
            double bilanganPertama = scanner.nextDouble();

            System.out.print("Masukkan Bilangan Kedua: ");
            double bilanganKedua = scanner.nextDouble();

            String result = switch (p) {
                case 1 -> {
                    double jlh = bilanganPertama + bilanganKedua;
                    yield bilanganPertama + " + " + bilanganKedua + " = " + jlh;
                }
                case 2 -> {
                    double krg = bilanganPertama - bilanganKedua;
                    yield bilanganPertama + " - " + bilanganKedua + " = " + krg;
                }
                case 3 -> {
                    double kali = bilanganPertama * bilanganKedua;
                    yield bilanganPertama + " x " + bilanganKedua + " = " + kali;
                }
                case 4 -> {
                    if (bilanganKedua != 0) {
                        double bagi = bilanganPertama / bilanganKedua;
                        yield bilanganPertama + " / " + bilanganKedua + " = " + bagi;
                    } else {
                        yield "Pembagian dengan nol tidak diperbolehkan.";
                    }
                }
                default -> "Pilihan tidak valid.";
            };

            System.out.println(result);
        } catch (InputMismatchException e) {
            System.out.println("Input tidak valid. Harap masukkan angka.");
        }
    }
}
