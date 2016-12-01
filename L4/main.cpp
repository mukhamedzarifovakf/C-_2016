#include <cstdlib>
#include <iostream>
#include <cmath>

using namespace std;

struct Node       //Структура являющаяся звеном списка
{
    int x;//Значение x будет передаваться в список
    int y;
    Node *next, *prev; //Указатели на адреса следующего и предыдущего элементов списка
};


struct List   //Создаем тип данных Список
{
    Node *head;
    Node *tail;  //Указатели на адреса начала списка и его конца
};


void add( List *list, int x , int y)
{
    Node *temp = new Node(); // Выделение памяти под новый элемент структуры
    temp->next = NULL;       // Указываем, что изначально по следующему адресу пусто
    temp->x = x;             // Записываем значение в структуру
    temp->y = y;

    if ( list->head != NULL ) // Если список не пуст
    {
        temp->prev = list->tail; // Указываем адрес на предыдущий элемент в соотв. поле
        list->tail->next = temp; // Указываем адрес следующего за хвостом элемента
        list->tail = temp;       //Меняем адрес хвоста
    }
    else //Если список пустой
    {
        temp->prev = NULL; // Предыдущий элемент указывает в пустоту
        list->head = list->tail = temp;    // Голова=Хвост=тот элемент, что сейчас добавили
    }
}

void print( List * list )
{
    Node * temp = list->head;  // Временно указываем на адрес первого элемента
    while( temp != NULL )      // Пока не встретим пустое значение
    {
        cout << temp->x <<" " << temp->y << endl; //Выводим значение на экран
        temp = temp->next;     //Смена адреса на адрес следующего элемента
    }
    cout<<"\n";
}

void print(List * list, int number) {
    Node * temp = list->head;  // Временно указываем на адрес первого элемента
    while( (temp != NULL) && (number > 0))      // Пока не встретим пустое значение
    {
        cout << temp->x <<" " << temp->y << endl; //Выводим значение на экран
        temp = temp->next;     //Смена адреса на адрес следующего элемента
        number--;
    }
    cout<<"\n";
}

void findFirst (List *list, int check_x, int check_y){
    Node * temp = list->head;
    int i = 1;
    while (temp != NULL){
        if ((temp->x == check_x) && (temp->y == check_y)) {
            cout << "It's on the " << i << " place from the begin" << endl;
            break;
        }
        temp = temp->next;
        i++;
    }
}

void findLast (List *list, int check_x, int check_y) {
    Node * temp = list->tail;
    int i = 1;
    while (temp != NULL){
        if ((temp->x == check_x) && (temp->y == check_y)) {
            cout << "It's on the " << i << " place from the end" << endl;
            break;
        }
        temp = temp->prev;
        i++;
    }
}

void addIn (List *list, int index, int X, int Y) {
    Node * temp = list->head;
    for(int i = 1; i <= index; i++){
        if (temp->next != NULL)
            temp = temp->next;
        else
            break;
    }
    Node * newElem = new Node;
    newElem->x = X;
    newElem->y = Y;
    if (temp->prev != NULL) {
        temp->prev->next = newElem;
        newElem->prev = temp->prev;
        temp->prev = newElem;
        newElem->next = temp;
    } else if (temp == list->head) {
        newElem->next = temp;
        newElem->prev = temp->prev;
        temp->prev = newElem;
        list->head = newElem;
    }
}

void popIn(List *list, int index){
    Node * temp = list->head;
    for(int i = 2; i < index; i++){
        temp = temp->next;
    }
    Node * new_tmp = temp->next->next;
    temp->next = new_tmp;
    new_tmp->prev = temp;
}

bool evenElementX(int x){
    if (x % 2 == 0)
        return true;
    else
        return false;
}

List *criterion( List * list , bool (*func)(int))
{
    Node * temp = list->head;// Временно указываем на адрес первого элемента
    List * newList = new List;

    while( temp != NULL )      // Пока не встретим пустое значение
    {
        if (func(temp->x)){
            add(newList, temp->x, temp->y);
        }
        temp = temp->next;     //Смена адреса на адрес следующего элемента
    }
    return newList;
}

double centerMassX(List *list){
    Node *temp = list->head;
    double sum = 0;
    double n = 0;
    while( temp != NULL ){
        sum += temp->x;
        n += 1;
        temp = temp->next;
    }
    return sum/n;
}

double centerMassY(List *list){
    Node *temp = list->head;
    double sum = 0;
    double n = 0;
    while( temp != NULL ){
        sum += temp->y;
        n += 1;
        temp = temp->next;
    }
    return sum/n;
}

void sortListCenterMass (List *list){
    bool flag = 1;
    double cenY = centerMassY(list);
    double cenX = centerMassX(list);
    int t;
    while(flag){
        Node *temp = list->head;
        Node *nextTemp = temp->next;
        flag = 0;
        while (nextTemp != NULL){
            if(((temp->x - cenX) + (temp->y - cenY)) > ((nextTemp->x - cenX) + (nextTemp->y - cenY))){
                t = temp->x;
                temp->x=nextTemp->x;
                nextTemp->x=t;
                t = temp->y;
                temp->y=nextTemp->y;
                nextTemp->y=t;
                flag=1;
            }
            temp = temp->next;
            nextTemp = nextTemp->next;
        }
    }
}

int main(void){

    List *list = new List;
    for (int i = 0; i < 20; i++) {
        int x = rand()/1000000;
        int y = rand()/1000000;
        add(list, x, y);
    }
    List *new_list = criterion(list, evenElementX);
    print(new_list);
    addIn(list, 0, 2, 2);
    print(list);
//    sortListCenterMass(list);
//    print(list, 5);
    return 0;
}