## Monopolin sovelluslogiikka

```mermaid
	classDiagram
		Pelilauta "1" -- "*" Ruutu
		Ruutu "1" -- "1" Ruutu
		Pelaaja "1" -- "1" Pelinappula
		Pelinappula "1" -- "1" Ruutu
		Pelaaja "1" .. "1" Nopat
```
