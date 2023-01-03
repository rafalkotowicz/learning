class Darts {
    int score(double xOfDart, double yOfDart) {
        double radius = Math.sqrt(Math.pow(xOfDart, 2) + Math.pow(yOfDart, 2));
        if (radius <= 1) {
            return 10;
        }
        if (radius <= 5) {
            return 5;
        }
        if (radius <= 10) {
            return 1;
        }
        return 0;
    }
}
