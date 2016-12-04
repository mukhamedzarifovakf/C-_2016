#include <iostream>
using namespace std;

struct Pair       //Структура являющаяся звеном списка
{
    int key;
    int x;
    int y;     //Значение x будет передаваться в список
    Pair *next,*prev; //Указатели на адреса следующего и предыдущего элементов списка
    Pair()
    {
        x = 0;
        y = 0;
        next = nullptr;
        prev = nullptr;
    }
    Pair(int a, int b)
    {
        x = a;
        y = b;
        next = nullptr;
        prev = nullptr;
    }

    void print_pair()
{
        cout << "{" << key << ": " << "(" << x << ", " << y << ")"<< "} " << endl;
    }
};


struct List   //Создаем тип данных Список
{
    Pair *head;
    Pair *tail;  //Указатели на адреса начала списка и его конца
    List()
    {
        head = tail = nullptr;
    }


    void add(const int KEY, const int x, const int y)
    {
        Pair *temp = new Pair(); // Выделение памяти под новый элемент структуры
        temp->key = KEY;
        //temp->next = nullptr;       // Указываем, что изначально по следующему адресу пусто
        temp->x = x;
        temp->y = y;             // Записываем значение в структуру

        if (head) // Если список не пуст
        {
            temp->prev = tail; // Указываем адрес на предыдущий элемент в соотв. поле
            tail->next = temp; // Указываем адрес следующего за хвостом элемента
            tail = temp;       //Меняем адрес хвоста
        } else //Если список пустой
        {
            temp->prev = nullptr; // Предыдущий элемент указывает в пустоту
            head = tail = temp;    // Голова=Хвост=тот элемент, что сейчас добавили
        }
    }


    void print()
    {
        Pair *temp = head;  // Временно указываем на адрес первого элемента
        while (temp)      // Пока не встретим пустое значение
        {
            temp->print_pair();
            temp = temp->next;     //Смена адреса на адрес следующего элемента
        }
        cout << endl;
    }


    Pair *search_p(const int KEY)
    {
        Pair *temp = head;
        while (temp)
        {
            if (temp->key == KEY)
            {
                return temp;
            }
            temp = temp->next;
        }
        cerr << "Key error!";
        return temp;
    }


    void delete_p(int KEY)
    {
        Pair *temp = search_pair(KEY);

        if (temp != head and temp != tail)
        {
            temp->next->prev = temp->prev;
            temp->prev->next = temp->next;
        }
        else if (temp == tail)
        {
            tail = temp->prev;
            tail->next = nullptr;
        }
        else if (temp == head)
        {
            head = temp->next;
            head->prev = nullptr;
        }
        delete temp;
    }
};

int hash_h(int KEY)
{
    return KEY%10;
}

struct hash_table
{
    List *keys = new List[10];

    void add_h(int KEY, int x, int y)
    {
        int h = hash_h(KEY);
        keys[h].add(KEY, x, y);
    }

    Pair *search_h(int KEY)
    {
        int h = hash_h(KEY);
        return keys[h].search_p(KEY);
    }
    void delete_h(int KEY)
    {
        int h = hash_h(KEY);
        keys[h].delete_p(KEY);
    }
};


int main ()
{
    hash_table table;
    for(int i=0; i<20; i++)
    {
        table.add_h(i, i+1, i+2);
    }
    for(int i = 0; i < 10; i++)
    {
        table.keys[i].print();
    }
}

