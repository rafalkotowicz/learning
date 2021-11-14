package section_03;

import common.Constants;
import org.openqa.selenium.By;
import org.openqa.selenium.NoSuchElementException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.Assert;
import org.testng.annotations.Test;

public class LoginPagePositiveTests {
    @Test
    public void successfulLoginTest() {
        System.setProperty("webdriver.chrome.driver","src/main/resources/chromedriver.exe");
        WebDriver driver = new ChromeDriver();
        driver.manage().window().maximize();
        driver.get("http://the-internet.herokuapp.com/login");
        driver.findElement(By.xpath("//input[@id=\"username\"]")).sendKeys(Constants.valid_user);
        driver.findElement(By.xpath("//input[@id=\"password\"]")).sendKeys(Constants.valid_password);
        driver.findElement(By.xpath("//*[text()=\" Login\"]/parent::button")).click();

        //Assertions
        String expectedUrl = "http://the-internet.herokuapp.com/secure";
        String actualUrl = driver.getCurrentUrl();
        Assert.assertEquals(actualUrl, expectedUrl);

        try {
            WebElement logoutButton = driver.findElement(By.xpath("//*[@href=\"/logout\"]"));
            Assert.assertTrue(logoutButton.isDisplayed());
        } catch (NoSuchElementException e) {
            Assert.fail("Logout button not found");
        }

        String expectedLoginMessage = "You logged into a secure area!";
        String actualLoginMessage = driver.findElement(By.xpath("//div[@id=\"flash\"]")).getText();
        Assert.assertTrue(actualLoginMessage.contains(expectedLoginMessage), "Successful login message not found!");

        driver.quit();
    }
}
