package section_06.exercises;

public class Wall {
    private double width;
    private double height;

    public Wall() {
    }

    public Wall(double width, double height) {
        if (0 > width) {
            this.width = 0;
        } else {
            this.width = width;
        }
        if (0 > height) {
            this.height = 0;
        } else {
            this.height = height;
        }
    }

    public double getWidth() {
        return width;
    }

    public void setWidth(double width) {
        this.width = 0 > width ? 0 : width;
    }

    public double getHeight() {
        return height;
    }

    public void setHeight(double height) {
        this.height = 0 > height ? 0 : height;
    }

    public double getArea() {
        return height * width;
    }
}
