## Monopolin sovelluslogiikka

```mermaid  
classDiagram  
Pelaaja "*" -- Ruutu "1"  
Pelilauta "1" -- Ruutu "*"  
Ruutu "1" -- "1"  
Pelaaja "1" -- "1" Pelinappula  
Pelinappula "1" -- "1" Ruutu  
```
