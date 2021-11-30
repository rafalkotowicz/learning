package com.herokuapp.theinternet.keypressestests;

import com.herokuapp.theinternet.base.TestUtilities;
import com.herokuapp.theinternet.pages.KeyPressesPage;
import org.openqa.selenium.Keys;
import org.testng.Assert;
import org.testng.annotations.Test;

public class KeyPressesTests extends TestUtilities {

    @Test
    public void pressKeyTest() {
        log.info("Starting pressKeyTest");

        KeyPressesPage keyPressesPage = new KeyPressesPage(driver, log);
        keyPressesPage.openPage();
        keyPressesPage.pressKey(Keys.ENTER);
        String actualMessage = keyPressesPage.getResultText();
        String expectedMessage = "You entered: ENTER";
        Assert.assertEquals(actualMessage, expectedMessage, "Invalid button clicked or message returned");
    }

    @Test
    public void pressKeyWithActionsTest() {
        log.info("Starting pressKeyWithActionsTest");

        KeyPressesPage keyPressesPage = new KeyPressesPage(driver, log);
        keyPressesPage.openPage();
        keyPressesPage.pressKeyWithActions(Keys.SPACE);
        String actualMessage = keyPressesPage.getResultText();
        String expectedMessage = "You entered: SPACE";
        Assert.assertEquals(actualMessage, expectedMessage, "Invalid button clicked or message returned");
    }
}