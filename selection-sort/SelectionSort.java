import java.util.Arrays;

public class SelectionSortArr {

    public void sort(int[] array) {
        for (int i = 0; i < array.length; i++) {
            int min = i;
            for (int j = i + 1; j < array.length; j++) {
                int lhs = array[j];
                int rhs = array[min];
                if (lhs < rhs) {
                    min = j;
                }
            }
            int temp = array[i];
            array[i] = array[min];
            array[min] = temp;
        }
    }

    public static void main(String... args) {
        int[] array = {-2, 10, -3, 5, 12, 0, 15};
        SelectionSort selectionSort = new SelectionSort();
        selectionSort.sort(array);
        System.out.println(Arrays.toString(array));
    }

}



