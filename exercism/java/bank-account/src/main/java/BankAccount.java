import java.util.concurrent.atomic.AtomicInteger;

class BankAccount {
    private final AtomicInteger balance;
    private boolean isOpen;

    public BankAccount() {
        this.balance = new AtomicInteger(0);
        isOpen = false;
    }

    public void open() {
        isOpen = true;
    }

    public int getBalance() throws BankAccountActionInvalidException {
        bankMustBeOpenToDoThat();
        return balance.get();
    }

    private void bankMustBeOpenToDoThat() throws BankAccountActionInvalidException {
        if (!isOpen) {
            throw new BankAccountActionInvalidException("Account closed");
        }
    }

    private void validateIncomingChange(int value) throws BankAccountActionInvalidException {
        if (value < 0) {
            throw new BankAccountActionInvalidException("Cannot deposit or withdraw negative amount");
        }
    }

    public void deposit(int value) throws BankAccountActionInvalidException {
        bankMustBeOpenToDoThat();
        validateIncomingChange(value);
        balance.addAndGet(value);
    }

    public void withdraw(int value) throws BankAccountActionInvalidException {
        bankMustBeOpenToDoThat();
        validateIncomingChange(value);
        if (balance.get() == 0) {
            throw new BankAccountActionInvalidException("Cannot withdraw money from an empty account");
        } else if (value > balance.get()) {
            throw new BankAccountActionInvalidException("Cannot withdraw more money than is currently in the account");
        }
        balance.addAndGet(-value);
    }

    public void close() {
        isOpen = false;
    }

}