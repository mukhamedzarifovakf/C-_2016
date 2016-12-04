#include <iostream>
#include <stdexcept>
#include <cstdlib>
#include <cmath>

class Fraction {
        private:
                int numerator;
                int denominator;

                void simplify()
                {
                        if (denominator < 0) {
                                numerator *= -1;
                                denominator *= -1;
                        }
                        if ( abs(numerator) < 2 ) return;
                        int gcd = GCD( abs(numerator), denominator );
                        numerator /= gcd;
                        denominator /= gcd;
                }
        public:
                Fraction( int n, int d ) : numerator(n), denominator(d) {
                        simplify();
                }

                Fraction() : numerator(0), denominator(1) {}
                Fraction( const Fraction &other ) : numerator( other.getNumerator() ), denominator( other.getDenominator() ) {}
                Fraction( int value ) : numerator(value), denominator(1) {}

                int getNumerator() const { return this->numerator; }
                int getDenominator() const { return denominator; }

                double getValue() const
                {
                        return static_cast<double>(getNumerator()) / static_cast<double>(getDenominator());
                }

                int compareTo( const Fraction &other ) const
                {
                        return getNumerator() * other.getDenominator() - getDenominator() * other.getNumerator();
                }

                int GCD( int a, int b )
                {
                        while( a != b ) {
                                if (a > b)
                                {
                                    a -= b;
                                }
                                else
                                {
                                     b -= a;
                                }

                        }
                        return a;
                }


                Fraction operator- (const Fraction &a)
                {
                        int commonDenominator = abs(a.getDenominator() * getDenominator());
                        int commonNumerator = a.getNumerator() * getDenominator() - getNumerator() * a.getDenominator();
                        return Fraction(commonNumerator, commonDenominator);
                }


                Fraction operator+ (const Fraction &a)
                {
                        int commonDenominator = a.getDenominator() * getDenominator();
                        int commonNumerator = a.getNumerator() * getDenominator() + getNumerator() * a.getDenominator();
                        return Fraction(commonNumerator, commonDenominator);
                }

                Fraction operator* (const Fraction &a)
                {
                        return Fraction(getNumerator() * a.getNumerator(), getDenominator() * a.getDenominator());
                }

                Fraction operator/ (const Fraction &a)
                {
                        return Fraction(getNumerator() * a.getDenominator(), getDenominator() * a.getNumerator());
                }

                bool operator== (const Fraction &a)
                {
                    return compareTo(a) == 0;
                }

                bool operator< (const Fraction &a)
                {
                    return compareTo(a)<0;
                }

                bool operator> (const Fraction &a)
                {
                    return compareTo(a)>0;
                }

                bool operator<= (const Fraction &a)
                {
                     return compareTo(a)<=0;
                }

                bool operator>= (const Fraction &a)
                {
                    return compareTo(a)>=0;
                }
    };

Fraction operator* (Fraction a, int b)
{
    return a*Fraction(b);
}
Fraction operator* (int b, Fraction a)
{
    return Fraction(b)*a;
}

Fraction operator+ (Fraction a, int b)
{
    return a + Fraction(b);
}
Fraction operator+ (int b, Fraction a)
{
    return Fraction(b) + a;
}

Fraction operator- (Fraction a, int b)
{
    return a + Fraction(-b);
}
Fraction operator- (int b, Fraction a)
{
    return Fraction(b) + (a*(-1));
}

Fraction operator/ (int b, Fraction a)
{
    return Fraction(b) / a;
}
Fraction operator/(Fraction a, int b)
{
    return a / Fraction(b);
}

std::ostream &operator<<(std::ostream &stream, const Fraction& a) {
        return stream
         << a.getNumerator() << "/" << a.getDenominator();
}

int main()
{

}
