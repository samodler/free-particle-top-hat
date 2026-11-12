## MODEL
  1D, non-relativistic, spinless particle of mass m.
  V(x) = 0 for all x when t > 0 (box removed instantly at t = 0).

## PARAMETERS
```
a > 0 (half-width, m),  m > 0 (kg),  ħ (J·s),  t ≥ 0 (s),  x (m)
```

## INITIAL STATE
```
Ψ(x,0) = 1/√(2a)   for |x| < a
         0         for |x| > a
        1/2√(2a)   at  |x| = a   (value of the Fourier integral, by Dirichlet's theorem; not physically meaningful)
```

## MOMENTUM AMPLITUDE
```
φ(k) = sin(ka) / (k √(πa)),    φ(0) = √(a/π)   (limit)
|φ(k)|² dk = probability of wavenumber in [k, k+dk]
```

## QUANTITY TO COMPUTE
```
Ψ(x,t) = 1/(π√(2a)) ∫_{-∞}^{∞} f(k; x, t) dk
f(k; x, t) = [sin(ka)/k] · exp[ i(kx − ħk²t/(2m)) ],   f(0; x, t) = a  (limit)
```

Units: 
`Ψ in m^(-1/2)`; the integral is dimensionless.

## EXACT RESULTS AVAILABLE FOR VERIFICATION
```
t = 0: 1/√(2a) inside, 0 outside, 1/(2√(2a)) at the edges
```
```
∫|Ψ(x,t)|² dx = 1 for all t
```

## KNOWN DIFFICULTIES
```
|φ(k)|² ~ 1/k² → slow convergence in the cutoff K
```

```
⟨E⟩ = ∞ → the sharp top-hat is an idealization, not a preparable state
```

Integrand oscillates in `k` (more rapidly for large `|x|` and large `t`)

## UNITS
The code works in dimensionless variables:

```
ξ = x/a,  κ = ka,  τ = t/T  with  T = m a²/ħ
```
The quantity computed is

```
ψ(ξ,τ) = 1/(π√2) ∫ (sin κ/κ) · exp[i(κξ − κ²τ/2)] dκ,  integrand → 1 at κ = 0
```

Box edges at `ξ = ±1`. `ψ` is dimensionless; `|ψ|²` is probability per unit `ξ`.

Conversion back to SI units:

```
x = aξ,  t = Tτ,  Ψ = ψ/√a
```