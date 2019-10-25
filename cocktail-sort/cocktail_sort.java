public class CocktailSort {

    int leftBorder;
    int rightBorder;

    public int[] sort(int[] toSort) {
        leftBorder = 0;
        rightBorder = toSort.length - 1;

        while (leftBorder < rightBorder) {
            forwardPass(toSort);
            backwardPass(toSort);
        }

        return toSort;
    }

    private void backwardPass(int[] toSort) {
        int toCompareBackwardPass1 = rightBorder;
        int toCompareBackwardPass2 = toCompareBackwardPass1 - 1;

        while (toCompareBackwardPass2 >= leftBorder) {
            if(toSort[toCompareBackwardPass1] < toSort[toCompareBackwardPass2]) {
                swap(toSort, toCompareBackwardPass1, toCompareBackwardPass2);
            }
            toCompareBackwardPass1--;
            toCompareBackwardPass2--;
        }
        leftBorder++;
    }

    private void swap(int[] toSort, int toCompareBackwardPass1, int toCompareBackwardPass2) {
        int tmp = toSort[toCompareBackwardPass1];
        toSort[toCompareBackwardPass1] = toSort[toCompareBackwardPass2];
        toSort[toCompareBackwardPass2] = tmp;
    }

    private void forwardPass(int[] toSort) {
        int toCompareForwardPass1 = leftBorder;
        int toCompareForwardPass2 = toCompareForwardPass1 + 1;

        while (toCompareForwardPass1 < rightBorder) {
            if(toSort[toCompareForwardPass1] > toSort[toCompareForwardPass2]) {
                swap(toSort, toCompareForwardPass1, toCompareForwardPass2);
            }
            toCompareForwardPass1++;
            toCompareForwardPass2++;
        }
        rightBorder--;
    }
}
