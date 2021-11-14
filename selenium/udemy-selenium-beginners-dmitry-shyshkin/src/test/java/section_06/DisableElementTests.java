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

public class DisableElementTests {
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
                System.out.println("Do not know how to start \"" + browser + "\" browser (or it was not provided)! " +
                        "Starting Chrome.");
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

    @Test(priority = 401, groups = {"exceptions", "negative"})
    public void disableElementTest() {
        driver.get("https://the-internet.herokuapp.com/dynamic_controls");

        WebElement enableButton = driver.findElement(By.xpath("//button[text()='Enable']"));
        WebElement textField = driver.findElement(By.xpath("//form[@id='input-example']/input"));
        enableButton.click();
        WebDriverWait waitForTextField = new WebDriverWait(driver, Duration.ofMillis(10000));
        waitForTextField.until(ExpectedConditions.elementToBeClickable(textField));
        
        String expectedText = "Test message.";
        textField.sendKeys(expectedText);
        String actualText = textField.getAttribute("value");
        
        Assert.assertEquals(actualText, expectedText, "Text field does not contain expected message.");
    }
}
