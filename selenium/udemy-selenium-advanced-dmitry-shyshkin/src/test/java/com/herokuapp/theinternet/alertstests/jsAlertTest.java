package com.herokuapp.theinternet.alertstests;

import com.herokuapp.theinternet.base.TestUtilities;
import com.herokuapp.theinternet.pages.JavaScriptAlertsPage;
import com.herokuapp.theinternet.pages.WelcomePage;
import org.testng.annotations.Test;
import org.testng.asserts.SoftAssert;

public class jsAlertTest extends TestUtilities {
    @Test
    public void jsBasicAlertTest() {
        log.info("Starting jsAlertTest");
        SoftAssert softAssert = new SoftAssert();

        //open main page
        WelcomePage welcomePage = new WelcomePage(driver, log);
        welcomePage.openPage();

        //click on 'JavaScript Alerts' link
        JavaScriptAlertsPage javaScriptAlertsPage = welcomePage.clickJavaScriptAlertsLink();

        //click JS Alert button
        javaScriptAlertsPage.openJSAlert();

        //get alert text
        String actualAlertMessage = javaScriptAlertsPage.getAlertText();

        //click ok button
        javaScriptAlertsPage.acceptAlert();

        //get result text
        String actualResultMessage = javaScriptAlertsPage.getResultText();

        //VERIFICATION
        //1.  Alert text is as expected
        final String expectedAlertMessage = "I am a JS Alert";
        softAssert.assertEquals(actualAlertMessage, expectedAlertMessage, "Invalid Alert message found");

        //2.  Result text is as expected
        final String expectedResultText = "You successfully clicked an alert";
        softAssert.assertEquals(actualResultMessage, expectedResultText, "Invalid result text found");
        softAssert.assertAll();
    }

    @Test
    public void jsConfirmDismissTest() {
        log.info("Starting jsConfirmDismissTest");
        SoftAssert softAssert = new SoftAssert();

        WelcomePage welcomePage = new WelcomePage(driver, log);
        welcomePage.openPage();
        JavaScriptAlertsPage javaScriptAlertsPage = welcomePage.clickJavaScriptAlertsLink();
        javaScriptAlertsPage.openJSConfirm();
        String actualAlertMessage = javaScriptAlertsPage.getAlertText();
        javaScriptAlertsPage.dismissAlert();
        String actualResultMessage = javaScriptAlertsPage.getResultText();

        //VERIFICATION
        final String expectedAlertMessage = "I am a JS Confirm";
        softAssert.assertEquals(actualAlertMessage, expectedAlertMessage, "Invalid Alert message found");
        final String expectedResultText = "You clicked: Cancel";
        softAssert.assertEquals(actualResultMessage, expectedResultText, "Invalid result text found");
        softAssert.assertAll();
    }

    @Test
    public void jsConfirmAcceptTest() {
        log.info("Starting jsConfirmAcceptTest");
        SoftAssert softAssert = new SoftAssert();

        WelcomePage welcomePage = new WelcomePage(driver, log);
        welcomePage.openPage();
        JavaScriptAlertsPage javaScriptAlertsPage = welcomePage.clickJavaScriptAlertsLink();
        javaScriptAlertsPage.openJSConfirm();
        String actualAlertMessage = javaScriptAlertsPage.getAlertText();
        javaScriptAlertsPage.acceptAlert();
        String actualResultMessage = javaScriptAlertsPage.getResultText();

        //VERIFICATION
        final String expectedAlertMessage = "I am a JS Confirm";
        softAssert.assertEquals(actualAlertMessage, expectedAlertMessage, "Invalid Alert message found");
        final String expectedResultText = "You clicked: Ok";
        softAssert.assertEquals(actualResultMessage, expectedResultText, "Invalid result text found");
        softAssert.assertAll();
    }

    @Test
    public void jsPromptTest() {
        log.info("Starting jsPromptTest");
        SoftAssert softAssert = new SoftAssert();

        //open main page
        WelcomePage welcomePage = new WelcomePage(driver, log);
        welcomePage.openPage();

        //click on 'JavaScript Alerts' link
        JavaScriptAlertsPage javaScriptAlertsPage = welcomePage.clickJavaScriptAlertsLink();

        //click JS Prompt button
        javaScriptAlertsPage.openJSPrompt();

        //get alert text
        String actualAlertMessage = javaScriptAlertsPage.getAlertText();

        //type text into alert
        final String sentMessageToAlert = "Hello Alerts, I am Kotu and I am learning Selenium FW";
        javaScriptAlertsPage.typeTextIntoAlert(sentMessageToAlert);

        //get result text
        String actualResultMessage = javaScriptAlertsPage.getResultText();

        //VERIFICATION
        //1.  Alert text is as expected
        final String expectedAlertMessage = "I am a JS prompt";
        softAssert.assertEquals(actualAlertMessage, expectedAlertMessage, "Invalid Alert message found");

        //2.  Result text is as expected
        final String expectedResultText = "You entered: " + sentMessageToAlert;
        softAssert.assertEquals(actualResultMessage, expectedResultText, "Invalid result text found");
        softAssert.assertAll();
    }
}
