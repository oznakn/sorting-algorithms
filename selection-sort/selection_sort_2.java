import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class SelectionSort {

    public <T extends Comparable<? super T>> void sort(List<T> list) {
        for (int i = 0; i < list.size(); i++) {
            int min = i;

            for (int j = i + 1; j < list.size(); j++) {
                T lhs = list.get(j);
                T rhs = list.get(min);
                if (lhs.compareTo(rhs) < 0) {
                    min = j;
                }
            }

            Collections.swap(list, i, min);
        }
    }

    public static void main(String... args) {
        List<Integer> list = Arrays.asList(-2, 10, -3, 5, 12, 0, 15);

        SelectionSort selectionSort = new SelectionSort();
        selectionSort.sort(list);

        System.out.println(list);
    }

}