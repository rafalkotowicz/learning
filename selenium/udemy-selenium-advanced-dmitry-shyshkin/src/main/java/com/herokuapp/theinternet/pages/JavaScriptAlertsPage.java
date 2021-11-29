package com.herokuapp.theinternet.pages;

import org.apache.logging.log4j.Logger;
import org.openqa.selenium.Alert;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class JavaScriptAlertsPage extends BasePageObject {

    private final By clickForJSAlertButtonLocator = By.xpath("//button[@onclick='jsAlert()']");
    private final By clickForJSConfirmButtonLocator = By.xpath("//button[@onclick='jsConfirm()']");
    private final By clickForJSPromptButtonLocator = By.xpath("//button[@onclick='jsPrompt()']");
    private final By resultTextLocator = By.id("result");

    public JavaScriptAlertsPage(WebDriver driver, Logger log) {
        super(driver, log);
    }

    public void openJSAlert() {
        log.info("Clicking on 'Click for JS Alert' button to open alert");
        click(clickForJSAlertButtonLocator);
    }

    public void openJSConfirm() {
        log.info("Clicking on 'Click for JS Confirm' button to open alert");
        click(clickForJSConfirmButtonLocator);
    }

    public void openJSPrompt() {
        log.info("Clicking on 'Click for JS Prompt' button to open alert");
        click(clickForJSPromptButtonLocator);
    }

    public String getAlertText() {
        Alert alert = switchToAlert();
        String alertText = alert.getText();
        log.info("Alert says: " + alertText);
        return alertText;
    }

    public void acceptAlert() {
        log.info("Switching to alert and pressing OK");
        Alert alert = switchToAlert();
        alert.accept();
    }

    public void dismissAlert() {
        log.info("Switching to alert and pressing Cancel");
        Alert alert = switchToAlert();
        alert.dismiss();
    }

    public void typeTextIntoAlert(String text) {
        log.info("Switching to alert, typing text and pressing OK");
        Alert alert = switchToAlert();
        alert.sendKeys(text);
        alert.accept();
    }

    public String getResultText() {
        String resultText = find(resultTextLocator).getText();
        log.info("Found result text: " + resultText);
        return resultText;
    }
}
