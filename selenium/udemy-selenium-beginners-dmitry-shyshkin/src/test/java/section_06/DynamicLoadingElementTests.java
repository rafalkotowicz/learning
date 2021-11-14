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

public class DynamicLoadingElementTests {
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

    @Test(priority = 400, groups = {"exceptions", "negative"})
    public void dynamicallyLoadedElementTest() {
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/1");
        WebElement startButton = driver.findElement(By.xpath("//*[@id=\"start\"]/button"));
        startButton.click();
        WebElement message = driver.findElement(By.xpath("//*[@id=\"finish\"]/h4"));
        WebDriverWait waitForMessage = new WebDriverWait(driver, Duration.ofMillis(10000));
        waitForMessage.until(ExpectedConditions.visibilityOf(message));
        String actualMessage = message.getText();
        String expectedMessage = "Hello World!";

        Assert.assertEquals(actualMessage, expectedMessage);
    }
}
