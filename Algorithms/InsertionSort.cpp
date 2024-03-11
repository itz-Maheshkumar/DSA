#include <iostream>

void insertionSort(int integerArray[], int arraySize)
{
    int i, key, j;
    for (i = 1; i < arraySize; i++)
    {
        key = integerArray[i];
        j = i - 1;
        while (j >=0 && integerArray[j] > key)
        {
            integerArray[j + 1] = integerArray[j];
            j = j - 1;
        }

        integerArray[j + 1] = key;
    }
}

void printSortedArray(int integerArray[], int arraySize)
{
    for (int i = 0; i < arraySize; i++)
    {
        std::cout << integerArray[i] << " ";
    }

    std::cout << '\n';
}
int main()
{
    int arraySize;
    std::cout << "Enter the arraySize: ";
    std::cin >> arraySize;
    int integerArray[arraySize];
    std::cout << "Enter the array elements:\n";
    for (int i = 0; i < arraySize; i++)
    {
        std::cin >> integerArray[i];
    }

    insertionSort(integerArray, arraySize);
    printSortedArray(integerArray, arraySize);
    return 0;
}
