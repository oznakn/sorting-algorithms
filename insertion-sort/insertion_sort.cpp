#include <iostream>
#include <vector>

int main()
{

    std::vector<int> array{20, 4, 2, 8, 33, 79, 5, 56, 29}; // Sample array

    for (int index = 1; index < array.size(); index++)
    {
        int position_marker = index; // variable to store the moving position of the current item
        int item = array[index];     // the actual number

        for (int jndex = index - 1; jndex >= 0; jndex--)
        {
            int other_item = array[jndex]; // the item being compared to

            if (item < other_item)
            {
                // swap the items, and decrement the position
                array[position_marker] = other_item;
                array[jndex] = item;
                position_marker -= 1;
            }
        }
    }

    // print out the array
    for (int value : array)
    {
        std::cout << value << "\n";
    }
}