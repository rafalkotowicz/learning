package section_06.challenges;

import java.util.UUID;

public class BankAccount {
    private String number;
    private String customerName;
    private double balance;
    private String email = "";
    private String phoneNumber = "";

    public BankAccount() {
        this("DEFAULT_NUMBER", "DEFAULT_NAME", 0.00, "DEFAULT_EMAIL", "DEFAULT_PHONE_NUMBER");
    }

    public BankAccount(String name, String email, String phone) {
        this(UUID.randomUUID().toString(), name, 0.00, email, phone);
    }

    public BankAccount(String number, String customerName, double balance, String email, String phoneNumber) {
        this.number = number;
        this.customerName = customerName;
        this.balance = balance;
        this.email = email;
        this.phoneNumber = phoneNumber;
    }

    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }

    public double getBalance() {
        return balance;
    }

    private void setBalance(double balance) {
        this.balance = balance;
    }

    public String getCustomerName() {
        return customerName;
    }

    public void setCustomerName(String customerName) {
        this.customerName = customerName;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getPhoneNumber() {
        return phoneNumber;
    }

    public void setPhoneNumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }

    public void deposit(double deposit) {
        this.balance += deposit;
    }

    public void witdraw(double withdraw) {
        if (withdraw > this.balance) {
            throw new IllegalArgumentException("Cannot withdraw more than balance");
        } else {
            this.balance -= withdraw;
        }
    }
}
