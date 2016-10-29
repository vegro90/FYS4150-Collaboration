#ifndef ISING2D_H
#define ISING2D_H
#include <random>

class Ising2D
{
private:
    int nSpin;
    double energy;
    double magneticMoment;

public:
    Ising2D();
    void InitializeGroundState();
    void InitializeRandomState();
    void Metropolis(int nSpin,int maxCycles, double temperature);
};

#endif // ISING2D_H
