import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.util.Optional;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatExceptionOfType;

public class ErrorHandlingTest {

    private final ErrorHandling errorHandling = new ErrorHandling();
    private static final String SAMPLE_EXCEPTION_MESSAGE = "This is the detail message.";

    @Test
    @DisplayName("Throws IllegalArgumentException")
    public void testThrowIllegalArgumentException() {
        assertThatExceptionOfType(IllegalArgumentException.class)
                .isThrownBy(errorHandling::handleErrorByThrowingIllegalArgumentException);
    }

    @Test
    @DisplayName("Throws IllegalArgumentException with provided detail message")
    public void testThrowIllegalArgumentExceptionWithDetailMessage() {
        assertThatExceptionOfType(IllegalArgumentException.class)
                .isThrownBy(() -> errorHandling.handleErrorByThrowingIllegalArgumentExceptionWithDetailMessage(
                        SAMPLE_EXCEPTION_MESSAGE))
                .withMessage(SAMPLE_EXCEPTION_MESSAGE);
    }

    @Test
    @DisplayName("Throws any checked exception")
    public void testThrowAnyCheckedException() {
        assertThatExceptionOfType(Exception.class)
                .isThrownBy(errorHandling::handleErrorByThrowingAnyCheckedException)
                .isNotInstanceOf(RuntimeException.class);
    }

    @Test
    @DisplayName("Throws any checked exception with provided detail message")
    public void testThrowAnyCheckedExceptionWithDetailMessage() {
        assertThatExceptionOfType(Exception.class)
                .isThrownBy(() -> errorHandling.handleErrorByThrowingAnyCheckedExceptionWithDetailMessage(
                        SAMPLE_EXCEPTION_MESSAGE))
                .isNotInstanceOf(RuntimeException.class)
                .withMessage(SAMPLE_EXCEPTION_MESSAGE);
    }

    @Test
    @DisplayName("Throws any unchecked exception")
    public void testThrowAnyUncheckedException() {
        assertThatExceptionOfType(RuntimeException.class)
                .isThrownBy(errorHandling::handleErrorByThrowingAnyUncheckedException);
    }

    @Test
    @DisplayName("Throws any unchecked exception with provided detail message")
    public void testThrowAnyUncheckedExceptionWithDetailMessage() {
        assertThatExceptionOfType(RuntimeException.class)
                .isThrownBy(() -> errorHandling.handleErrorByThrowingAnyUncheckedExceptionWithDetailMessage(
                        SAMPLE_EXCEPTION_MESSAGE))
                .withMessage(SAMPLE_EXCEPTION_MESSAGE);
    }

    @Test
    @DisplayName("Throws custom checked exception")
    public void testThrowCustomCheckedException() {
        assertThatExceptionOfType(CustomCheckedException.class)
                .isThrownBy(errorHandling::handleErrorByThrowingCustomCheckedException);
    }

    @Test
    @DisplayName("Throws custom checked exception with provided detail message")
    public void testThrowCustomCheckedExceptionWithDetailMessage() {
        assertThatExceptionOfType(CustomCheckedException.class)
                .isThrownBy(() -> errorHandling.handleErrorByThrowingCustomCheckedExceptionWithDetailMessage(
                        SAMPLE_EXCEPTION_MESSAGE))
                .withMessage(SAMPLE_EXCEPTION_MESSAGE);
    }

    @Test
    @DisplayName("Throws custom unchecked exception")
    public void testThrowCustomUncheckedException() {
        assertThatExceptionOfType(CustomUncheckedException.class)
                .isThrownBy(errorHandling::handleErrorByThrowingCustomUncheckedException);
    }

    @Test
    @DisplayName("Throws custom unchecked exception with provided detail message")
    public void testThrowCustomUncheckedExceptionWithDetailMessage() {
        assertThatExceptionOfType(CustomUncheckedException.class)
                .isThrownBy(() -> errorHandling.handleErrorByThrowingCustomUncheckedExceptionWithDetailMessage(
                        SAMPLE_EXCEPTION_MESSAGE))
                .withMessage(SAMPLE_EXCEPTION_MESSAGE);
    }

    @Test
    @DisplayName("Handles error by throwing Optional instance")
    public void testReturnOptionalInstance() {
        Optional<Integer> successfulResult = errorHandling.handleErrorByReturningOptionalInstance("1");
        assertThat(successfulResult).isPresent().hasValue(1);

        Optional<Integer> failureResult = errorHandling.handleErrorByReturningOptionalInstance("a");
        assertThat(failureResult).isNotPresent();

    }

}
