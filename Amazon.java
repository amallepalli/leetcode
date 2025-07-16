import java.util.ArrayList;
import java.util.Collections;

public class Amazon {
    public static void main(String[] args) {
        int maxPoints = 0;
        ArrayList<Integer> points = new ArrayList<>();
        points.add(5);
        points.add(2);
        points.add(2);
        points.add(3);
        points.add(1);
        Collections.sort(points, Collections.reverseOrder());
        for (int i = 0; i < points.size(); i++) {
            if (points.get(i) - i > 0) 
                maxPoints += points.get(i) - i;
        }
        System.out.println(maxPoints);
    }
}