#include <iostream>
using namespace std;

struct Node       //Структура являющаяся звеном списка
{
    int x;
    int y;     //Значение x будет передаваться в список
    Node *next,*prev; //Указатели на адреса следующего и предыдущего элементов списка
    Node()
    {
        x = 0;
        y = 0;
        next = nullptr;
        prev = nullptr;
    }
    Node(int a, int b)
    {
        x = a;
        y = b;
        next = nullptr;
        prev = nullptr;
    }
};


struct List   //Создаем тип данных Список
{
    Node *head;
    Node *tail;  //Указатели на адреса начала списка и его конца
    List()
    {
        head = tail = nullptr;
    }
};


void add( List *list, int x, int y )
{
    Node *temp = new Node(); // Выделение памяти под новый элемент структуры
    temp->next = nullptr;       // Указываем, что изначально по следующему адресу пусто
    temp->x = x;
    temp->y = y;             // Записываем значение в структуру

    if ( list->head != nullptr ) // Если список не пуст
    {
        temp->prev = list->tail; // Указываем адрес на предыдущий элемент в соотв. поле
        list->tail->next = temp; // Указываем адрес следующего за хвостом элемента
        list->tail = temp;       //Меняем адрес хвоста
    }
    else //Если список пустой
    {
        temp->prev = nullptr; // Предыдущий элемент указывает в пустоту
        list->head = list->tail = temp;    // Голова=Хвост=тот элемент, что сейчас добавили
    }
}


void print( List * list )
{
    Node * temp = list->head;  // Временно указываем на адрес первого элемента
    while( temp != nullptr )      // Пока не встретим пустое значение
    {
        cout << "(" << temp->x << ";" << temp->y << ")" << " "; //Выводим значение на экран
        cout << "\n";
        temp = temp->next;     //Смена адреса на адрес следующего элемента
    }
}



void search_node_last (List *list, int check_x, int check_y) //упражнение 3
{
    Node * temp = list->tail;
    int i = 1;
    while (temp != NULL){
        if ((temp->x == check_x) && (temp->y == check_y)) {
            cout << i << "from the end" << endl;
            break;
        }
        temp = temp->prev;
        i++;
    }
}



void search_node_first (List *list, int check_x, int check_y) //упражнение 3
{
    Node * temp = list->head;
    int i = 1;
    while (temp != NULL){
        if ((temp->x == check_x) && (temp->y == check_y)) {
            cout << i << "from the beginning" << endl;
            break;
        }
        temp = temp->next;
        i++;
    }
}



void insert_in (List *list, Node *node, int i)  // упражнение 4
{
    Node *temp = list->head;
    while ((i > 1) && (temp))
    {
        temp= temp->next;
        i--;
    }
    if (temp)
    {
        if (list->tail == temp)
        {
            list->tail = node;
        }
        if (list->head == temp)
        {
            list->head = node;
        }
        node->prev = temp->prev;
        node->next = temp;
        if (temp->prev != nullptr)
        {
            temp->prev->next = node;
        }
        temp->prev = node;
    }
    else
    {
        add(list, node->x, node->y);
    }
}

void  delete_from (List *list, int i)  // упражнение 5
{
    Node *temp = list->head;
    while ((i > 1) && (temp))
    {
        temp= temp->next;
        i--;
    }
    if (temp != nullptr)
    {
        if (list->tail == temp)
        {
            list->tail = temp->prev;
        }
        if (list->head == temp)
        {
            list->head = temp->next;
        }
        if (temp->prev != nullptr)
        {
            temp->prev->next = temp->next;
        }
        if(temp->next != nullptr)
        {
            temp->next->prev = temp->prev;
        }
        delete temp;
    }
}


int main ()
{
    List list = List();
    for (int i = 0; i < 10; i++)
    {
        add(&list, rand()%10, rand()%10);
    }
    print(&list);
}
