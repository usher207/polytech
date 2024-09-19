public class MathTasks {

    public static void main(String[] args) {
        // Аргументи для завдання 5
        double a5 = 2.54;
        double b5 = 1.23;
        double c5 = -2.14;
        double d5 = -0.23;

        // Аргументи для завдання 15
        double a15 = 1.25;
        double b15 = 3.09;
        double d15 = 4.25;

        // Аргументи для завдання 25
        double a25 = 2.98;
        double b25 = 5.55;
        double c25 = 0.045;
        double d25 = 0.129;

        // Обчислення результату для завдання 5
        System.out.println("Завдання 5 результат: " + task5(a5, b5, c5, d5));

        // Обчислення результату для завдання 15
        System.out.println("Завдання 15 результат: " + task15(a15, b15, d15));

        // Обчислення результату для завдання 25
        System.out.println("Завдання 25 результат: " + task25(a25, b25, c25, d25));
    }

    // Завдання 5
    public static double task5(double a, double b, double c, double d) {
        if (d <= 0) {
            System.out.println("Помилка: d повинне бути додатнім для кореня.");
            return Double.NaN;
        }

        double sqrtD = Math.sqrt(d);

        double acosArg = -c / sqrtD;
        if (acosArg < -1 || acosArg > 1) {
            System.out.println("Помилка: аргумент для Math.acos виходить за межі [-1, 1].");
            return Double.NaN;
        }

        return 2 * Math.cos(Math.pow(a, b)) + Math.acos(acosArg);
    }

    // Завдання 15
    public static double task15(double a, double b, double d) {
        if (b < -1 || b > 1) {
            System.out.println("Помилка: b повинне бути в межах [-1, 1] для Math.acos.");
            return Double.NaN;
        }

        double acosB = Math.acos(b);
        double sqrtAcosB = Math.sqrt(acosB);

        return 2 * (Math.sin(a) / sqrtAcosB) - 3 * Math.cbrt(Math.exp(-a) * Math.sinh(d));
    }

    // Завдання 25
    public static double task25(double a, double b, double c, double d) {
        if (d <= 0) {
            System.out.println("Помилка: d повинне бути додатнім для кореня.");
            return Double.NaN;
        }

        double fifthRootD = Math.pow(d, 1.0 / 5.0); // Корінь 5-го степеня з d
        double lgC = Math.log10(c); // lg(c) - десятковий логарифм

        return Math.pow(a, b) / Math.cosh(b) + 4 * (lgC / fifthRootD);
    }
}
