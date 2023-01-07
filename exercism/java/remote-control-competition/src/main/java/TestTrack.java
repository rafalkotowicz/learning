import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class TestTrack {

    public static void race(RemoteControlCar car) {
        car.race(car);
    }

    public static List<ProductionRemoteControlCar> getRankedCars(ProductionRemoteControlCar prc1,
                                                                 ProductionRemoteControlCar prc2) {
        List<ProductionRemoteControlCar> listOfCars = Arrays.asList(new ProductionRemoteControlCar[]{prc1, prc2});
        Collections.sort(listOfCars);
        return listOfCars;
    }
}
