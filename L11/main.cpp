#include <iostream>
#include <vector>

template <typename T>
class CircularBuffer
{
public:

    CircularBuffer( int size )
    {
        head = tail = 0;
        arr.reserve(size);
    }


    // Добавить элемент
    void put( const T & value )
    {
        if ( tail == arr.capacity() )
        {
            tail = 0;
        }

        arr.push_back(value);
        ++tail;
    }


    // Извлечь последний элемент
    T & pop()
    {

        T & elem = arr[head];
        ++head;
        if ( head == arr.capacity() ) {
            head = 0;
        }
        arr.resize(head);
        return elem;
    }

    // Кол-во элементов в буфере
    size_t size() const
    {
        return arr.size();
    }

    // Ёмкость буфера
    size_t capacity() const
    {
        return arr.capacity();
    }

    //operator[]
    T & operator[](int i)
    {
        T & elem = arr[i];
        return elem;
    }

    //printBuffer
    void printBuffer()
    {
        std::cout << "BUFFER:" << head << " " << tail << " " << arr.size() << " " << arr.capacity() <<"{";
        for (int i=head; i<tail;i++)
        {
            std::cout << " " << arr[i] << ",";

        }
        std::cout << "}" << std::endl;

    }
