package section_07

import java.security.InvalidParameterException

class Account {
    BigDecimal balance = 0.0

    void deposit(BigDecimal amount) {
        if (amount > 0) {
            balance += amount
        } else {
            throw new InvalidParameterException("Cannot deposit 0 or less")
        }
    }

    void deposit(List<BigDecimal> amounts) {
        amounts.forEach({ deposit(it) })
    }
}
