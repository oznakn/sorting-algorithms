public class ShellSort {

    int gap;
    int end;
    int toCompareHead;
    int toCompareTail;

    public int[] sort(int[] toSort) {
        computeGap(toSort.length);
        computeCompareAndEndPositions();

        while (gap > 0)
            performPass(toSort);

        return toSort;
    }

    private void performPass(int[] toSort) {
        while (end < toSort.length) {
            compareHeadAndEnd(toSort);
            compareHeadAndTail(toSort);

            end++;
            toCompareHead = end - gap;
            toCompareTail = toCompareHead - gap;
        }

        computeGap(gap);
        computeCompareAndEndPositions();
    }

    private void compareHeadAndEnd(int[] toSort) {
        if (toSort[toCompareHead] > toSort[end])
            swap(toSort, end);
    }

    private void compareHeadAndTail(int[] toSort) {
        while (toCompareHead > 0 && toCompareTail >= 0) {
            if (toSort[toCompareTail] > toSort[toCompareHead])
                swap(toSort, toCompareTail);

            toCompareHead = toCompareHead - gap;
            toCompareTail = toCompareTail - gap;
        }
    }

    private void swap(int[] toSort, int end) {
        int tmp = toSort[end];
        toSort[end] = toSort[toCompareHead];
        toSort[toCompareHead] = tmp;
    }

    private void computeGap(int gapBaseBefore) {
        gap = gapBaseBefore / 2;
    }

    private void computeCompareAndEndPositions() {
        end = gap;
        toCompareHead = gap - 1;
        toCompareTail = toCompareHead - gap;
    }
}
