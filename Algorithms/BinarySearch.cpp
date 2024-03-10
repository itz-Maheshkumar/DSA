#include <iostream>

bool isValueInArray(int intergerArray[], int valueToFind, int arrayLength)
{
    int low = 0;
    int high = arrayLength - 1;
    while (low <= high)
    {
        int mid = (low + high) / 2;
        if (intergerArray[mid] == valueToFind)
        {
            return true;
        }

        else if (intergerArray[mid] < valueToFind)
        {
            low = mid + 1;
        }

        else
        {
            high = mid - 1;
        }
    }
    return false;
}

void sort(int integerArray[], int arraySize)
{
    int temp;
    for (int i = 0; i < arraySize; i++)
    {
        for (int j = i + 1; j < arraySize; j++)
        {
            if (integerArray[i] > integerArray[j])
            {
                temp = integerArray[i];
                integerArray[i] = integerArray[j];
                integerArray[j] = temp;
            }
        }
    }
}
int main()
{
    std::cout << "Enter the size array: ";
    int arraySize;
    std::cin >> arraySize;
    int intergerArray[arraySize];
    std::cout << "Enter the array elements\n";
    for (int index = 0; index < arraySize; index++)
    {
        std::cin >> intergerArray[index];
    }

    sort(intergerArray, arraySize);
    std::cout<< "Enter the value to find: ";
    int valueToFind;
    std::cin >> valueToFind;
    int arrayLength = sizeof(intergerArray) / sizeof(intergerArray[0]);
    bool isFound = isValueInArray(intergerArray, valueToFind, arrayLength);
    if (isFound)
    {
        std::cout << "Found";
    }
    else
    {
        std::cout << "Not Found";
    }

    std::cout << '\n';
    return 0;
}
