#include <iostream>

void bubbleSort(int integerArray[], int arraySize)
{
    int i, j, temp;
    for (i = 0; i < arraySize - 1; i++)
    {
        for (j = 0; j < arraySize - i - 1; j++)
        {
            if (integerArray[j] > integerArray[j + 1])
            {
                temp = integerArray[j];
                integerArray[j] = integerArray[j + 1];
                integerArray[j + 1] = temp;
            }
        }
    }
}

void displaySortedArray(int integerArray[], int arraySize)
{
    std::cout<<"Sorted Array: ";
    for (int i = 0; i < arraySize; i++)
    {
        std::cout << integerArray[i] << " ";
    }

    std::cout << '\n';
}

int main()
{
    int arraySize;
    std::cout << "Enter the size of the array: ";
    std::cin >> arraySize;
    int integerArray[arraySize];
    std::cout << "Enter the value of the array : \n";
    for (int i = 0; i < arraySize; i++)
    {
        std::cin >> integerArray[i];
    }

    bubbleSort(integerArray, arraySize);
    displaySortedArray(integerArray, arraySize);
    return 0;
}