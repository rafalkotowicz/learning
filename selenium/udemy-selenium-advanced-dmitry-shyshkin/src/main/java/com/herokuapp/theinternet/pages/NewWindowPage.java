package com.herokuapp.theinternet.pages;

import org.apache.logging.log4j.Logger;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class NewWindowPage extends BasePageObject {

    private By h3DivLocator = By.xpath("//h3[text()=\"New Window\"]");

    public NewWindowPage(WebDriver driver, Logger log) {
        super(driver, log);
    }

    public String getH3Div() {
        return find(h3DivLocator).getText();
    }
}