package com.herokuapp.theinternet.alertstests;

import com.herokuapp.theinternet.base.TestUtilities;
import com.herokuapp.theinternet.pages.JavaScriptAlertsPage;
import com.herokuapp.theinternet.pages.WelcomePageObject;
import org.testng.Assert;
import org.testng.annotations.Test;

public class jsAlertTest extends TestUtilities {

    @Test
    public void jsBasicAlertTest() {
        log.info("Starting jsAlertTest");

        //open main page
        WelcomePageObject welcomePageObject = new WelcomePageObject(driver, log);
        welcomePageObject.openPage();

        //click on 'JavaScript Alerts' link
        JavaScriptAlertsPage javaScriptAlertsPage = welcomePageObject.clickJavaScriptAlertsLink();

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
        Assert.assertEquals(actualAlertMessage, expectedAlertMessage, "Invalid Alert message found");

        //2.  Result text is as expected
        final String expectedResultText = "You successfully clicked an alert";
        Assert.assertEquals(actualResultMessage, expectedResultText, "Invalid result text found");
    }

    @Test
    public void jsConfirmDismissTest() {
        log.info("Starting jsConfirmDismissTest");

        WelcomePageObject welcomePageObject = new WelcomePageObject(driver, log);
        welcomePageObject.openPage();
        JavaScriptAlertsPage javaScriptAlertsPage = welcomePageObject.clickJavaScriptAlertsLink();
        javaScriptAlertsPage.openJSConfirm();
        String actualAlertMessage = javaScriptAlertsPage.getAlertText();
        javaScriptAlertsPage.dismissAlert();
        String actualResultMessage = javaScriptAlertsPage.getResultText();

        //VERIFICATION
        final String expectedAlertMessage = "I am a JS Confirm";
        Assert.assertEquals(actualAlertMessage, expectedAlertMessage, "Invalid Alert message found");
        final String expectedResultText = "You clicked: Cancel";
        Assert.assertEquals(actualResultMessage, expectedResultText, "Invalid result text found");
    }

    @Test
    public void jsConfirmAcceptTest() {
        log.info("Starting jsConfirmAcceptTest");

        WelcomePageObject welcomePageObject = new WelcomePageObject(driver, log);
        welcomePageObject.openPage();
        JavaScriptAlertsPage javaScriptAlertsPage = welcomePageObject.clickJavaScriptAlertsLink();
        javaScriptAlertsPage.openJSConfirm();
        String actualAlertMessage = javaScriptAlertsPage.getAlertText();
        javaScriptAlertsPage.acceptAlert();
        String actualResultMessage = javaScriptAlertsPage.getResultText();

        //VERIFICATION
        final String expectedAlertMessage = "I am a JS Confirm";
        Assert.assertEquals(actualAlertMessage, expectedAlertMessage, "Invalid Alert message found");
        final String expectedResultText = "You clicked: Ok";
        Assert.assertEquals(actualResultMessage, expectedResultText, "Invalid result text found");
    }

    @Test
    public void jsPromptTest() {
        log.info("Starting jsPromptTest");

        //open main page
        WelcomePageObject welcomePageObject = new WelcomePageObject(driver, log);
        welcomePageObject.openPage();

        //click on 'JavaScript Alerts' link
        JavaScriptAlertsPage javaScriptAlertsPage = welcomePageObject.clickJavaScriptAlertsLink();

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
        Assert.assertEquals(actualAlertMessage, expectedAlertMessage, "Invalid Alert message found");

        //2.  Result text is as expected
        final String expectedResultText = "You entered: " + sentMessageToAlert;
        Assert.assertEquals(actualResultMessage, expectedResultText, "Invalid result text found");
    }
}
