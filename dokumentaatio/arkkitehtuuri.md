```mermaid
classDiagram
  UserRepository "1" -- "*" User
  Crossword "*" -- "1" User
  User "*" -- "1" Crossword

```
