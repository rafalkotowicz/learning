package playground

final File file = new File("./", "input.csv")
Scanner scanner = new Scanner(file);

while (scanner.hasNext()) {
    println(scanner.next())
}
