package com.herokuapp.theinternet.pages;

import org.apache.logging.log4j.Logger;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class WelcomePageObject extends BasePageObject {
    private final String pageUrl = "http://the-internet.herokuapp.com/";

    private final By formAuthenticationLinkLocator = By.linkText("Form Authentication");
    private final By checkboxesLinkLocator = By.linkText("Checkboxes");
    private final By dropdownLinkLocator = By.linkText("Dropdown");

    public WelcomePageObject(WebDriver driver, Logger log) {
        super(driver, log);
    }

    public void openPage() {
        log.info("Opening page: " + pageUrl);
        openUrl(pageUrl);
        log.info("Page opened: " + pageUrl);
    }

    public LoginPage clickFormAuthenticationLink() {
        log.info("Clicking 'Form Authentication' link on Welcome Page");
        click(formAuthenticationLinkLocator);
        return new LoginPage(driver, log);
    }

    public CheckboxesPage clickCheckboxesLink() {
        log.info("Clicking 'Checkboxes' link on Welcome Page");
        click(checkboxesLinkLocator);
        return new CheckboxesPage(driver, log);
    }

    public DropdownPage clickDropdownLink() {
        log.info("Clicking 'Dropdown' link on Welcome Page");
        click(dropdownLinkLocator);
        return new DropdownPage(driver, log);
    }
}
