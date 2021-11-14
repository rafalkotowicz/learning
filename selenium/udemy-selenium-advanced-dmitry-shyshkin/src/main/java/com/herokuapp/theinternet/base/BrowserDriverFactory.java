package com.herokuapp.theinternet.base;

import org.apache.logging.log4j.Logger;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

public class BrowserDriverFactory {
    private final ThreadLocal<WebDriver> driver = new ThreadLocal<>();
    private final String browser;
    private Logger log;

    public BrowserDriverFactory(String browser, Logger log) {
        this.browser = browser.toLowerCase();
        this.log = log;
    }

    public WebDriver createDriver() {
        log.info("Create driver: " + browser);

        switch (browser) {
            case "chrome" -> {
                System.setProperty("webdriver.chrome.driver", "src/main/resources/chromedriver.exe");
                driver.set(new ChromeDriver());
            }
            case "firefox" -> {
                System.setProperty("webdriver.gecko.driver", "src/main/resources/geckodriver.exe");
                driver.set(new FirefoxDriver());
            }
            default -> {
                log.info("Do not know how to start: " + browser + ", starting chrome.");
                System.setProperty("webdriver.chrome.driver", "src/main/resources/chromedriver.exe");
                driver.set(new ChromeDriver());
            }
        }

        return driver.get();
    }
}
