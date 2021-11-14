package section_06;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.Assert;
import org.testng.annotations.*;

import java.time.Duration;

public class StaleElementTests {
    private WebDriver driver;

    @Parameters({"browser"})
    @BeforeTest(alwaysRun = true)
    private void setUp(@Optional("defaultChrome") String browser) {
        switch (browser) {
            case "chrome" -> {
                System.setProperty("webdriver.chrome.driver", "src/main/resources/chromedriver.exe");
                driver = new ChromeDriver();
            }
            case "firefox" -> {
                System.setProperty("webdriver.gecko.driver", "src/main/resources/geckodriver.exe");
                driver = new FirefoxDriver();
            }
            default -> {
                System.out.println("Do not know how to start \"" + browser + "\" browser! Starting Chrome.");
                System.setProperty("webdriver.chrome.driver", "src/main/resources/chromedriver.exe");
                driver = new ChromeDriver();
            }
        }
        driver.manage().window().minimize();
    }

    @AfterTest(alwaysRun = true)
    private void tearDown() {
        driver.quit();
    }

    @SuppressWarnings("CommentedOutCode")
    @Test(priority = 401, groups = {"exceptions", "negative"})
    public void staleElementsTest() {
        driver.get("https://the-internet.herokuapp.com/dynamic_controls");

        WebElement checkbox = driver.findElement(By.id("checkbox"));
        WebElement removeButton = driver.findElement(By.xpath("//button[text()='Remove']"));

        WebDriverWait waitForCheckboxDisappear = new WebDriverWait(driver, Duration.ofMillis(10000));
        removeButton.click();
//        waitForCheckboxDisappear.until(ExpectedConditions.invisibilityOf(checkbox));
//        Assert.assertFalse(checkbox.isDisplayed());

//        Assert.assertTrue(waitForCheckboxDisappear.until(ExpectedConditions.invisibilityOf(checkbox)), "Checkbox did not disappear");

        Assert.assertTrue(waitForCheckboxDisappear.until(ExpectedConditions.stalenessOf(checkbox)), "Checkbox did not disappear");

        WebElement addButton = driver.findElement(By.xpath("//button[text()='Add']"));
        addButton.click();

        checkbox = waitForCheckboxDisappear.until(ExpectedConditions.visibilityOfElementLocated(By.id("checkbox")));
        Assert.assertTrue(checkbox.isDisplayed(), "Checkbox did not appear");
    }
}
