import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Bogosort {

    private <T extends Comparable<? super T>> boolean isSorted(List<T> list) {
        if (list.size() <= 1) {
            return true;
        }
        for (int i = 0; i < list.size() - 1; i++) {
            T lhs = list.get(i);
            T rhs = list.get(i + 1);
            if (lhs.compareTo(rhs) > 0) {
                return false;
            }
        }
        return true;
    }

    public <T extends Comparable<? super T>> void sort(List<T> list) {
        while (!isSorted(list)) {
            Collections.shuffle(list);
        }
    }


    public static void main(String... args) {
        List<Integer> list = Arrays.asList(7, 5, 6, 3, 1, 2);

        Bogosort bogosort = new Bogosort();
        bogosort.sort(list);

        System.out.println(list);
    }

}