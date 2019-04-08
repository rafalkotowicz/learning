package section_07.challenges;

public class Printer {
    private static double TONER_PER_PAGE = 0.1;

    private double tonerLevel = 50;
    private int printedPagesCounter = 0;
    private int usedSheetsCount = 0;

    public Printer() {}

    public Printer(double tonerLevel) {
        if (tonerLevel > 0 && tonerLevel <= 100) {
            this.tonerLevel = tonerLevel;
        }
    }

    public Printer(double tonerLevel, int printedPagesCounter, int usedSheetsCout) {
        this(tonerLevel);
        this.printedPagesCounter = printedPagesCounter;
        this.usedSheetsCount = usedSheetsCout;
    }

    public double getTonerLevel() {
        return tonerLevel;
    }

    public void refilToner() {
        this.tonerLevel = 100;
    }

    public int getPrintedPagesCount() {
        return printedPagesCounter;
    }

    public void printPages(int noOfPages) {
        boolean defaultDuplexPrinting = false;
        printPages(noOfPages, defaultDuplexPrinting);
    }

    public void printPages(int noOfPages, boolean duplex) {
        double newTonerLevel = this.tonerLevel - noOfPages * TONER_PER_PAGE;
        if(newTonerLevel > 0) {
            this.tonerLevel = newTonerLevel;
        } else {
            int onlyThisManyPagesPrinted = (int)Math.floor(this.tonerLevel/TONER_PER_PAGE);
            System.out.print("Toner empty! Printed only " + onlyThisManyPagesPrinted + " out of " + noOfPages + " requested pages");
            noOfPages = onlyThisManyPagesPrinted;
            this.tonerLevel = 0;
        }
        int duplexVal = duplex ? 2 : 1;
        this.printedPagesCounter += noOfPages;
        this.usedSheetsCount += noOfPages / duplexVal + noOfPages % 2;
    }

    public int usedSheetsOfPaper() {
        return usedSheetsCount;
    }
}
