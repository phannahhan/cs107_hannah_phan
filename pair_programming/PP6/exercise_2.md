# File       : exercise_2.md
# Created    : Friday October 8
# Groupmates: Hannah, Neil, Arno, Jie

| trace | elem op. | value | elem der.      | dx          | dy          |
|-------|----------|-------|----------------|-------------|-------------|
| V-1   | x        | 1     | Dp* V-1        | 1           | 0           |
| V0    | y        | 1     | Dp*V0          | 0           | 1           |
| V1    | V-1 + V0 | 2     | Dp*V-1 + Dp*V0 | 1           | 1           |
| V2    | exp(V1)  | e^2   | exp(V1)*Dp*V1  | e^2*(1)=e^2 | e^2*(1)=e^2 |


| trace | elem op. | value | elem der.                 | dx | dy |
|-------|----------|-------|---------------------------|----|----|
| V-1   | x        | 1     | Dp* V-1                   | 1  | 0  |
| V0    | y        | 1     | Dp*V0                     | 0  | 1  |
| V1    | V-1^2    | 1     | 2*V-1*DpV-1               | 2  | 0  |
| V2    | V2^2     | 1     | 2*V2*DpV2                 | 0  | 2  |
| V3    | V1+V2    | 2     | 2 *V-1* DpV-1+2 *V2* DpV2 | 2  | 2  |
