#include<iostream>

using namespace std;

template<int K, int L, int M, int N, int P, int R, int S>
class DimQ
{
    double value;

public:
    DimQ<K, L, M, N, P, R, S>(double _value = 0.0)
    {
        value = _value;
    };
    double get_value()
    {
        return this->value;
    }
    //перегрузка операторов
    DimQ<K, L, M, N, P, R, S>  operator-()
    {
        value = -value;
    };

    DimQ<K, L, M, N, P, R, S> operator= (const DimQ<K, L, M, N, P, R, S> & other)
    {
        value = other.value;
    };

    DimQ<K, L, M, N, P, R, S> operator+ (const DimQ<K, L, M, N, P, R, S> & other)
    {
        value = value + other.value;
    };

    DimQ<K, L, M, N, P, R, S> operator- (const DimQ<K, L, M, N, P, R, S> & other)
    {
        value = value - other.value;
    };

    template<int k, int l, int m, int n, int p, int r, int s>
    DimQ<K+k, L+l, M+m, N+n, P+p, R+r, S+s> operator* (DimQ<k, l, m, n, p, r, s> &other)
    {
        return DimQ<K+k, L+l, M+m, N+n, P+p, R+r, S+s>(this->value * other.get_value());
    };

    template<int k, int l, int m, int n, int p, int r, int s>
    DimQ<K-k, L-l, M-m, N-n, P-p, R-r, S-s> operator/ (DimQ<k, l, m, n, p, r, s> &other)
    {
        return DimQ<K-k, L-l, M-m, N-n, P-p, R-r, S-s>(this->value / other.get_value());
    };
};

typedef DimQ<1, 0, 0, 0, 0, 0, 0> Length;
typedef DimQ<1, 0, -1, 0, 0, 0, 0> Velocity;
typedef DimQ<1, 0, -2, 0, 0, 0, 0> Acceleration;
typedef DimQ<0, 0, 0, 0, 0, 0, 0> Dimensionless;
typedef DimQ<0, 1, 0, 0, 0, 0, 0> Mass;
typedef DimQ<0, 0, 1, 0, 0, 0, 0> Time;
typedef DimQ<0, 0, 0, 1, 0, 0, 0> Current;
typedef DimQ<0, 0, 0, 0, 1, 0, 0> Tempreture;
typedef DimQ<0, 0, 0, 0, 0, 1, 0> Amount;
typedef DimQ<0, 0, 0, 0, 0, 0, 1> Light;

int main()
{
    // Длина
    Length l = {100};
    // Время
    Time t = {20};

    // Скорость
    Velocity v = l / t;

    // Ускорение
    Acceleration a = v / t;

    // Размерная величина
    auto smth = v*a*a/t;
    // Безразмерная величина
    auto dimensionless = v/v;

// Ошибка компиляции!
    Dimensionless d = v;
// Mass m = v;
    Amount a = d;
}