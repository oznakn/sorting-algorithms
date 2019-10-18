public class MergeSort {

    public void mergeSort(int[] unsorted) {
        if (unsorted == null) {
            return;
        }

        if (unsorted.length > 1) {
            int middle = unsorted.length / 2;

            int[] leftPart = new int[middle];
            int[] rightPart = new int[unsorted.length - middle];

            for (int i = 0; i < middle; i++) {
                leftPart[i] = unsorted[i];
            }

            for (int i = middle; i < unsorted.length; i++) {
                rightPart[i - middle] = unsorted[i];
            }

            mergeSort(leftPart);
            mergeSort(rightPart);

            int comparePosLeft = 0;
            int comparePosRight = 0;
            int replacementPos = 0;

            while (comparePosLeft < leftPart.length && comparePosRight < rightPart.length) {
                if (leftPart[comparePosLeft] <= rightPart[comparePosRight]) {
                    unsorted[replacementPos] = leftPart[comparePosLeft];
                    comparePosLeft++;
                } else {
                    unsorted[replacementPos] = rightPart[comparePosRight];
                    comparePosRight++;
                }
                replacementPos++;
            }

            collectRemainingValues(unsorted, leftPart, comparePosLeft, replacementPos);
            collectRemainingValues(unsorted, rightPart, comparePosRight, replacementPos);
        }
    }

    private void collectRemainingValues(int[] unsorted, int[] part, int comparePos, int replacementPos) {
        if (comparePos < part.length) {
            for (int i = comparePos; i < part.length; i++) {
                unsorted[replacementPos] = part[i];
                replacementPos++;
            }
        }
    }
}

