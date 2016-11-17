#include<iostream>

template<int K, int L, int M, int N, int P, int R, int S>
class DimQ
{
    double value;

public:
    DimQ<K, L, M, N, P, R, S>(double _value = 0.0)
    {
        value = _value;
    };
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

}