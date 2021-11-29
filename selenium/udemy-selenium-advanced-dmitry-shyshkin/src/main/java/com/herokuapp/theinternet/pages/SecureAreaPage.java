package com.herokuapp.theinternet.pages;

import org.apache.logging.log4j.Logger;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class SecureAreaPage extends BasePageObject {
    private String pageUrl = "http://the-internet.herokuapp.com/secure";

    private By logOutButton = By.xpath("//a[@class='button secondary radius']");
    private By message = By.id("flash");

    public SecureAreaPage(WebDriver driver, Logger log) {
        super(driver, log);
    }

    /** Get URL from PageObject */
    public String getPageUrl() {
        return pageUrl;
    }

    public boolean isLogoutButtonVisible() {
        return find(logOutButton).isDisplayed();
    }

    public String getSuccessMessageText() {
        return find(message).getText();
    }
}
