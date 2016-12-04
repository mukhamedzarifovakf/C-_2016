#include <iostream>
using namespace std;

struct Node       //��������� ���������� ������ ������
{
    int x;
    int y;     //�������� x ����� ������������ � ������
    Node *next,*prev; //��������� �� ������ ���������� � ����������� ��������� ������
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


struct List   //������� ��� ������ ������
{
    Node *head;
    Node *tail;  //��������� �� ������ ������ ������ � ��� �����
    List()
    {
        head = tail = nullptr;
    }
};


void add( List *list, int x, int y )
{
    Node *temp = new Node(); // ��������� ������ ��� ����� ������� ���������
    temp->next = nullptr;       // ���������, ��� ���������� �� ���������� ������ �����
    temp->x = x;
    temp->y = y;             // ���������� �������� � ���������

    if ( list->head != nullptr ) // ���� ������ �� ����
    {
        temp->prev = list->tail; // ��������� ����� �� ���������� ������� � �����. ����
        list->tail->next = temp; // ��������� ����� ���������� �� ������� ��������
        list->tail = temp;       //������ ����� ������
    }
    else //���� ������ ������
    {
        temp->prev = nullptr; // ���������� ������� ��������� � �������
        list->head = list->tail = temp;    // ������=�����=��� �������, ��� ������ ��������
    }
}


void print( List * list )
{
    Node * temp = list->head;  // �������� ��������� �� ����� ������� ��������
    while( temp != nullptr )      // ���� �� �������� ������ ��������
    {
        cout << "(" << temp->x << ";" << temp->y << ")" << " "; //������� �������� �� �����
        cout << "\n";
        temp = temp->next;     //����� ������ �� ����� ���������� ��������
    }
}



void search_node_last (List *list, int check_x, int check_y) //���������� 3
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



void search_node_first (List *list, int check_x, int check_y) //���������� 3
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



void insert_in (List *list, Node *node, int i)  // ���������� 4
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

void  delete_from (List *list, int i)  // ���������� 5
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
