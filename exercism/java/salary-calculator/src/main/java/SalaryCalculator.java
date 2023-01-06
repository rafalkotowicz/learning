public class SalaryCalculator {
    public double multiplierPerDaysSkipped(int daysSkipped) {
        return daysSkipped > 5 ? 0.85 : 1;
    }

    public int multiplierPerProductsSold(int productsSold) {
        return productsSold > 20 ? 13 : 10;
    }

    public double bonusForProductSold(int productsSold) {
        return multiplierPerProductsSold(productsSold) * productsSold;
    }

    public double finalSalary(int daysSkipped, int productsSold) {
        final double salaryCap = 2000d;
        final double salaryBase = 1000d;
        final double salary = salaryBase * multiplierPerDaysSkipped(daysSkipped) + bonusForProductSold(productsSold);
        return salary > salaryCap ? salaryCap : salary;
    }
}
