package com.herokuapp.theinternet.editortests;

import com.herokuapp.theinternet.base.TestUtilities;
import com.herokuapp.theinternet.pages.EditorPage;
import com.herokuapp.theinternet.pages.WelcomePageObject;
import org.testng.Assert;
import org.testng.annotations.Test;

public class EditorTests extends TestUtilities {

    @Test
    public void defaultEditorValueTest() {
        log.info("Starting defaultEditorValueTest");

        WelcomePageObject welcomePage = new WelcomePageObject(driver, log);
        welcomePage.openPage();
        EditorPage editorPage = welcomePage.clickWYSIWYGEditorLink();

        //Then
        String actualEditorText = editorPage.getEditorText();
        String expectedEditorText = "Your content goes here.";
        Assert.assertEquals(actualEditorText, expectedEditorText, "Default editor text has not been found");
    }
}