#include <iostream>

bool isValueInArray(int intergerArray[], int valueToFind, int arrayLength)
{
    for (int index = 0; index < arrayLength; index++)
    {
        if (intergerArray[index] == valueToFind)
        {
            return true;
        }
    }

    return false;
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

    std::cout << "Enter the value to find: ";
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
    
    std::cout<<'\n';
    return 0;
}
