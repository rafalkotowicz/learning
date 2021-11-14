package section_05;

import common.Constants;
import org.openqa.selenium.By;
import org.openqa.selenium.NoSuchElementException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.testng.Assert;
import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Parameters;
import org.testng.annotations.Test;

public class LoginPageTests {
    private WebDriver driver;

    @Parameters({"browser"})
    @BeforeTest(alwaysRun = true)
    private void setUp(String browser) {
        switch (browser) {
            case "chrome" -> {
                System.setProperty("webdriver.chrome.driver", "src/main/resources/chromedriver.exe");
                driver = new ChromeDriver();
            }
            case "firefox" -> {
                System.setProperty("webdriver.gecko.driver", "src/main/resources/geckodriver.exe");
                driver = new FirefoxDriver();
            }
            default -> System.out.println("Do not know how to start \"" + browser + "\" browser!");
        }
        driver.manage().window().minimize();
        driver.get("http://the-internet.herokuapp.com/login");
    }

    @AfterTest(alwaysRun = true)
    private void tearDown() {
        driver.quit();
    }

    @Test(priority = 400, groups = {"positive", "sanity"})
    public void successfulLoginTest() {
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
    }

    @Test(priority = 100, groups = {"negative", "sanity"})
    public void invalidUserNotLoggedInTest() {
        login("invalid_user", Constants.valid_password);

        String expectedUrl = "http://the-internet.herokuapp.com/login";
        String actualUrl = driver.getCurrentUrl();
        Assert.assertEquals(actualUrl, expectedUrl);
    }

    @Test(priority = 110, groups = {"negative"})
    public void invalidUserMessagesTest() {
        login("invalid_user", Constants.valid_password);

        String expectedLoginMessage = "Your username is invalid!";
        String actualLoginMessage = driver.findElement(By.xpath("//div[@id=\"flash\"]")).getText();
        Assert.assertTrue(actualLoginMessage.contains(expectedLoginMessage), "Failed login message not found!");
    }

    @Test(priority = 120, groups = {"negative"}, expectedExceptions = {NoSuchElementException.class})
    public void invalidUserNoLogoutButtonTest() {
        login("invalid_user", Constants.valid_password);
        driver.findElement(By.xpath("//*[@href=\"/logout\"]"));
    }

    @Test(priority = 200, groups = {"negative", "sanity"})
    public void invalidPasswordNotLoggedInTest() {
        login(Constants.valid_user, "invalid_password");

        String expectedUrl = "http://the-internet.herokuapp.com/login";
        String actualUrl = driver.getCurrentUrl();
        Assert.assertEquals(actualUrl, expectedUrl);
    }

    @Test(priority = 210, groups = {"negative"})
    public void invalidPasswordMessagesTest() {
        login(Constants.valid_user, "invalid_password");

        String expectedLoginMessage = "Your password is invalid!";
        String actualLoginMessage = driver.findElement(By.xpath("//div[@id=\"flash\"]")).getText();
        Assert.assertTrue(actualLoginMessage.contains(expectedLoginMessage), "Failed login message not found!");
    }

    @Test(priority = 220, groups = {"negative"}, expectedExceptions = {NoSuchElementException.class})
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
