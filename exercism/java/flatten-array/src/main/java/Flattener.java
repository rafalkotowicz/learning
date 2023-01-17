import java.util.ArrayList;
import java.util.List;

class Flattener {

    public List<Object> flatten(List<Object> elements) {
        List<Object> flattened = new ArrayList<>();
        for (Object element : elements) {
            if (element instanceof List) {
                flattened.addAll(flatten((List<Object>) element));
            } else if (element != null) {
                flattened.add(element);
            }
        }
        return flattened;
    }
}