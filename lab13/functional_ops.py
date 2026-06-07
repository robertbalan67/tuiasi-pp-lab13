"""
Operații funcționale pe HashMap — exclusiv map, filter, lambda, dict comprehension.
Fără bucle for/while explicite.
"""

from __future__ import annotations
from math import isqrt


# ─── Funcții auxiliare ────────────────────────────────────────────────────────

def is_prime(n: int) -> bool:
    """
    Returnează True dacă n este număr prim.

    is_prime(1)  == False
    is_prime(2)  == True
    is_prime(3)  == True
    is_prime(4)  == False
    is_prime(7)  == True
    is_prime(9)  == False
    is_prime(49) == False
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    # Verificăm divizori impari până la √n
    return all(n % i != 0 for i in range(3, isqrt(n) + 1, 2))


def make_even(n: int) -> int:
    """
    Dacă n este impar → returnează n × 2.
    Dacă n este par   → returnează n neschimbat.

    make_even(3) == 6
    make_even(4) == 4
    make_even(9) == 18
    """
    return n * 2 if n % 2 != 0 else n


# ─── Prelucrare HashMap ───────────────────────────────────────────────────────

def process_hashmap(data: dict[str, int]) -> dict[str, int]:
    """
    Aplică simultan două transformări pe valorile dict-ului:

      1. Elimină perechile cu valori prime.
      2. Dublează valorile impare non-prime (cu make_even).

    Implementare EXCLUSIV funcțională: filter + dict comprehension + lambda.

    Tabel de referință:
      Valoare | Prim? | Impar? | Rezultat
        2     |  DA   |  DA    | eliminat
        4     |  NU   |  NU    | 4 (nemodificat)
        9     |  NU   |  DA    | 18 (dublat)
       49     |  NU   |  DA    | 98 (dublat)
        5     |  DA   |  DA    | eliminat

    Exemplu:
        process_hashmap({'a': 4, 'c': 5, 'd': 9})
        # 4  non-prim par → 4
        # 5  prim → eliminat
        # 9  non-prim impar → 18
        # → {'a': 4, 'd': 18}
    """
    # Pas 1: filtrăm perechile cu valori NON-prime
    non_prime_items = filter(lambda kv: not is_prime(kv[1]), data.items())

    # Pas 2: aplicăm make_even pe fiecare valoare non-primă
    return {k: make_even(v) for k, v in non_prime_items}
