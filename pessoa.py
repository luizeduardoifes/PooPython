from dataclasses import dataclass


@dataclass
class Pessoa:
    id = int
    nome: str
    idade: int
    altura: float
    peso: float
    sexo: str