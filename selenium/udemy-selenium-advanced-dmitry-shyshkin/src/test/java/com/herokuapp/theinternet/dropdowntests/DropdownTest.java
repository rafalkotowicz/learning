package com.herokuapp.theinternet.dropdowntests;

import com.herokuapp.theinternet.base.TestUtilities;
import com.herokuapp.theinternet.pages.DropdownPage;
import com.herokuapp.theinternet.pages.WelcomePage;
import org.testng.Assert;
import org.testng.annotations.Test;

public class DropdownTest extends TestUtilities {

    @Test
    public void optionTwoTest() {
        log.info("Starting optionTwoTest");

        //open main page
        WelcomePage welcomePage = new WelcomePage(driver, log);
        welcomePage.openPage();

        //clock on 'Dropdown' link
        DropdownPage dropdownPage = welcomePage.clickDropdownLink();

        //select 'Option 2'
        dropdownPage.selectOption(2);

        //verify 'Option 2' is selected
        String actuallySelectedOption = dropdownPage.getSelectedOption();
        String expectedSelectedOption = "Option 2";
        Assert.assertEquals(actuallySelectedOption, expectedSelectedOption, "Unexpected option selected.");
    }
}
