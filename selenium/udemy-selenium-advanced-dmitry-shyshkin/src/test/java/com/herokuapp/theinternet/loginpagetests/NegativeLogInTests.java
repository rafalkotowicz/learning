package com.herokuapp.theinternet.loginpagetests;

import com.herokuapp.theinternet.base.TestUtilities;
import com.herokuapp.theinternet.pages.LoginPage;
import com.herokuapp.theinternet.pages.WelcomePage;
import org.testng.Assert;
import org.testng.annotations.Parameters;
import org.testng.annotations.Test;

public class NegativeLogInTests extends TestUtilities {

    @Parameters({"username", "password", "expectedMessage"})
    @Test(priority = 1)
    public void negativeTest(String username, String password, String expectedErrorMessage) {
        log.info("Starting negativeTest");

        // open main page
        WelcomePage welcomePage = new WelcomePage(driver, log);
        welcomePage.openPage();

        // Click on Form Authentication link
        LoginPage loginPageObject = welcomePage.clickFormAuthenticationLink();

        // enter invalid username and/or password
        loginPageObject.logInWithInvalidData(username, password);

        // Verification
        loginPageObject.waitForErrorMessage();
        String actualErrorMessage = loginPageObject.getErrorMessageText();
        Assert.assertTrue(actualErrorMessage.contains(expectedErrorMessage),
                "actualErrorMessage [" + actualErrorMessage + "] does not contain expectedErrorMessage " +
                        "[" + expectedErrorMessage + "]");
    }
}
