package com.herokuapp.theinternet.pages;

import org.apache.logging.log4j.Logger;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class LoginPage extends BasePageObject {
    private final String pageUrl = "http://the-internet.herokuapp.com/login";

    private final By usernameLocator = By.id("username");
    private final By passwordLocator = By.name("password");
    private final By logInButtonLocator = By.tagName("button");
    private final By errorMessageLocator = By.id("flash");


    public LoginPage(WebDriver driver, Logger log) {
        super(driver, log);
    }

    public String getErrorMessageText() {
        return find(errorMessageLocator).getText();
    }

    public SecureAreaPage logInSuccessfully(final String username, final String password) {
        log.info("Executing Log In with valid data - username [" + username + "] and password [" + password + "]");
        type(username, usernameLocator);
        type(password, passwordLocator);
        click(logInButtonLocator);
        return new SecureAreaPage(driver, log);
    }

    public void logInWithInvalidData(final String username, final String password) {
        log.info("Executing Log In with invalid data - username [" + username + "] and password [" + password + "]");
        type(username, usernameLocator);
        type(password, passwordLocator);
        click(logInButtonLocator);
    }

    public void waitForErrorMessage() {
        waitForVisibilityOf(errorMessageLocator, 5);
    }
}
