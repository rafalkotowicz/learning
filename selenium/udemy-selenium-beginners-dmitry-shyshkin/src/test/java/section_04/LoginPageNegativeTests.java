package section_04;

import common.Constants;
import org.openqa.selenium.By;
import org.openqa.selenium.NoSuchElementException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.Assert;
import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Test;

public class LoginPageNegativeTests {
    private WebDriver driver;

    @BeforeTest(groups = {"PL1", "PL2", "PL3"})
    private void setup() {
        System.setProperty("webdriver.chrome.driver", "src/main/resources/chromedriver.exe");
        driver = new ChromeDriver();
        driver.manage().window().maximize();
        driver.get("http://the-internet.herokuapp.com/login");
    }

    @AfterTest(groups = {"PL1", "PL2", "PL3"})
    private void cleanUp() {
        driver.quit();
    }

    @Test(priority = 100, groups = {"PL1", "PL2", "PL3"})
    public void invalidUserNotLoggedInTest() {
        login("invalid_user", Constants.valid_password);

        String expectedUrl = "http://the-internet.herokuapp.com/login";
        String actualUrl = driver.getCurrentUrl();
        Assert.assertEquals(actualUrl, expectedUrl);
    }

    @Test(priority = 110, groups = {"PL2", "PL3"})
    public void invalidUserMessagesTest() {
        login("invalid_user", Constants.valid_password);

        String expectedLoginMessage = "Your username is invalid!";
        String actualLoginMessage = driver.findElement(By.xpath("//div[@id=\"flash\"]")).getText();
        Assert.assertTrue(actualLoginMessage.contains(expectedLoginMessage), "Failed login message not found!");
    }

    @Test(priority = 120, groups = {"PL3"}, expectedExceptions = {NoSuchElementException.class})
    public void invalidUserNoLogoutButtonTest() {
        login("invalid_user", Constants.valid_password);
        driver.findElement(By.xpath("//*[@href=\"/logout\"]"));
    }

    @Test(priority = 200, groups = {"PL1", "PL2", "PL3"})
    public void invalidPasswordNotLoggedInTest() {
        login(Constants.valid_user, "invalid_password");

        String expectedUrl = "http://the-internet.herokuapp.com/login";
        String actualUrl = driver.getCurrentUrl();
        Assert.assertEquals(actualUrl, expectedUrl);
    }

    @Test(priority = 210, groups = {"PL2", "PL3"})
    public void invalidPasswordMessagesTest() {
        login(Constants.valid_user, "invalid_password");

        String expectedLoginMessage = "Your password is invalid!";
        String actualLoginMessage = driver.findElement(By.xpath("//div[@id=\"flash\"]")).getText();
        Assert.assertTrue(actualLoginMessage.contains(expectedLoginMessage), "Failed login message not found!");
    }

    @Test(priority = 220, groups = {"PL3"}, expectedExceptions = {NoSuchElementException.class})
    public void invalidPasswordNoLogoutButtonTest() {
        login(Constants.valid_user, "invalid_password");
        driver.findElement(By.xpath("//*[@href=\"/logout\"]"));
    }

    private void login(final String user, final String password) {
        driver.findElement(By.xpath("//input[@id=\"username\"]")).sendKeys(user);
        driver.findElement(By.xpath("//input[@id=\"password\"]")).sendKeys(password);
        driver.findElement(By.xpath("//*[text()=\" Login\"]/parent::button")).click();
    }
}
