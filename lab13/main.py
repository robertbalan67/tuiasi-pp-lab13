from lab13.functional_ops import is_prime, make_even, process_hashmap
from lab13.html_combiner import extract_body

def main() -> None:
    print("=== Operații funcționale pe HashMap ===\n")

    nums = list(range(1, 12))
    primes = list(filter(is_prime, nums))
    print(f"Numere prime din {nums}:\n  {primes}\n")

    evened = list(map(make_even, range(1, 11)))
    print(f"make_even aplicat pe [1..10]:\n  {evened}\n")

    sample = {'a': 4, 'b': 7, 'c': 5, 'd': 9, 'e': 11, 'f': 6}
    result = process_hashmap(sample)
    print(f"Input:  {sample}")
    print(f"Output: {result}\n")

    print("=== Combinator HTML ===\n")
    html = "<html><body><p>Conținut</p></body></html>"
    print(f"extract_body: {repr(extract_body(html))}")

if __name__ == "__main__":
    main()
