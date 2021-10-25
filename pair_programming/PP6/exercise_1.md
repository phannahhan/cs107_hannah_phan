# File       : exercise_1.md
# Created    : Friday October 8
# Groupmates: Hannah, Neil, Arno, Jie


| trace | elem op. | value       | elem der.     | dx              | dy                      |
|-------|----------|-------------|---------------|-----------------|-------------------------|
| V-1   | pi/2     | pi/2        | 1             | 1               | 0                       |
| V0    | pi/3     | pi/3        | 1             | 0               | 1                       |
| V1    | sin(V-1) | 1           | cos(V1)*DpV-1 | cos(pi/2)*1 = 0 | cos(pi/2)*0 = 0         |
| V2    | Cos(V0)  | .5          | -sin(V0)*DpV0 | 0               | -sin(pi/3)*1=-sqrt(3)/2 |
| V3    | -1*V2    | -.5         | -1*DpV2       | 0               | sqrt(3)/2               |
| V4    | V3+V1    | .5          | DpV3 + DpV1   | cos(pi/2)*1 = 0 | sqrt(3)/2               |
| V5    | V4^2     | .025        | 2*V4*DpV4     | 0               | sqrt(3)/2               |
| V6    | -1*V5    | -.025       | -1*DpV5       | 0               | -sqrt(3)/2              |
| V7    | exp(V6)  | 0.778800783 | exp(V6)*DpV6  | 0               | .778*-sqrt(3)/2         |
