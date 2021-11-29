package com.herokuapp.theinternet.pages;

import org.apache.logging.log4j.Logger;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.Select;

public class DropdownPage extends BasePageObject {
    private final By dropdownLocator = By.id("dropdown");

    public DropdownPage(WebDriver driver, Logger log) {
        super(driver, log);
    }

    public void selectOption(int optionId) {
        log.info("Selecting option '" + optionId + "' from dropdown");
        WebElement dropdownElement = find(dropdownLocator);
        Select dropdown = new Select(dropdownElement);

//        dropdown.selectByIndex(optionId);
        dropdown.selectByValue(Integer.toString(optionId));
//        dropdown.selectByVisibleText("Option " + optionId);
    }

    public String getSelectedOption() {
        WebElement dropdownElement = find(dropdownLocator);
        Select dropdown = new Select(dropdownElement);
        String selectedOption = dropdown.getFirstSelectedOption().getText();
        log.info(selectedOption + " is selected in dropdown");
        return selectedOption;
    }
}
