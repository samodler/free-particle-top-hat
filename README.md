# Numerical calculation of Ψ(x,t) for a free particle

This project computes the time evolution of a free quantum particle in one dimension whose initial wavefunction is a square "top-hat". 

The wavefunction Ψ(x,t) is given by an oscillatory integral over wavenumber k, which is evaluated with numerical integration methods implemented from scratch rather than with library routines.

```
Ψ(x,t) = 1/(π√(2a)) ∫_{-∞}^{∞} f(k; x, t) dk
f(k; x, t) = [sin(ka)/k] · exp[i(kx − ħk²t/(2m))]
```

The problem has a known solution in terms of Fresnel integrals, which will serve as an independent reference for verifying the numerical results.

## Status 

* The mathematical problem, its assumptions and the known numerical difficulties are specified in `docs/specification.md`. 
* No code has been written yet. The next step is a minimal numerical integration engine (trapezoidal rule) tested on integrals with known exact answers.

## Requirements
Python 3.12. No third-party packages are needed at this stage.

## Repository layout
- `docs/specification.md`: mathematical specification of the problem
