## Monopolin sovelluslogiikka

```mermaid
	classDiagram
		Pelaaja "*" -- "1" Ruutu
		Pelilauta "1" -- "*" Ruutu
		Ruutu "1" -- "1" Ruutu
		Pelaaja "1" -- "1" Pelinappula
		Pelinappula "1" -- "1" Ruutu
```
