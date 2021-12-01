package com.herokuapp.theinternet.windowstests;

import com.herokuapp.theinternet.base.TestUtilities;
import com.herokuapp.theinternet.pages.NewWindowPage;
import com.herokuapp.theinternet.pages.WelcomePage;
import com.herokuapp.theinternet.pages.WindowsPage;
import org.testng.Assert;
import org.testng.annotations.Test;

public class WindowsTests extends TestUtilities {

    @Test
    public void newWindowTest() {
        log.info("Starting newWindowTest");

        WelcomePage welcomePage = new WelcomePage(driver, log);
        welcomePage.openPage();
        WindowsPage windowsPage = welcomePage.clickMultipleWindowsLink();
        windowsPage.openNewWindow();
        NewWindowPage newWindowPage = windowsPage.switchToNewWindowPage();

        String actualNewPageHeader = newWindowPage.getH3Div();
        String expectedNewPageHeader = "New Window";
        Assert.assertEquals(actualNewPageHeader, expectedNewPageHeader, "Invalid text found on New Page");
    }
}
