package com.herokuapp.theinternet.windowstests;

import com.herokuapp.theinternet.base.TestUtilities;
import com.herokuapp.theinternet.pages.NewWindowPage;
import com.herokuapp.theinternet.pages.WelcomePageObject;
import com.herokuapp.theinternet.pages.WindowsPage;
import org.testng.Assert;
import org.testng.annotations.Test;

public class WindowsTests extends TestUtilities {

    @Test
    public void newWindowTest() {
        log.info("Starting newWindowTest");

        WelcomePageObject welcomePageObject = new WelcomePageObject(driver, log);
        welcomePageObject.openPage();
        WindowsPage windowsPage = welcomePageObject.clickMultipleWindowsLink();
        windowsPage.openNewWindow();
        NewWindowPage newWindowPage = windowsPage.switchToNewWindowPage();

        String actualNewPageHeader = newWindowPage.getH3Div();
        String expectedNewPageHeader = "New Window";
        Assert.assertEquals(actualNewPageHeader, expectedNewPageHeader, "Invalid text found on New Page");
    }
}
