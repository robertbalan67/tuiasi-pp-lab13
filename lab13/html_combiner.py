"""
Combinator de fișiere HTML cu expresii regulate.

Extrage body-urile din fișiere HTML individuale și le îmbină
într-un singur document HTML valid.
"""

from __future__ import annotations
import re


# ─── Funcții individuale ──────────────────────────────────────────────────────

def extract_body(html: str) -> str:
    """
    Extrage conținutul dintre <body> și </body>.
    Ignoră <html>, <head>...</head> și orice atribute din <body ...>.

    Exemplu:
        extract_body("<html><body><p>test</p></body></html>")
        # "<p>test</p>"

        extract_body("<html><head><title>T</title></head><body><p>text</p></body></html>")
        # "<p>text</p>"
    """
    match = re.search(r"<body[^>]*>(.*?)</body>", html, re.DOTALL)
    if match:
        return match.group(1)
    # Dacă nu există tag <body>, returnăm html-ul întreg (fallback)
    return html


def build_combined_html(bodies: list[str], source_names: list[str]) -> str:
    """
    Construiește un document HTML complet din mai multe body-uri extrase.

    - <head> conține un meta 'description' cu numele surselor
    - <body> conține toate body-urile concatenate în ordine

    Exemplu:
        build_combined_html(["<p>A</p>", "<p>B</p>"], ["a.html", "b.html"])
        # '<!DOCTYPE html><html>\\n  <head>...'
    """
    sources      = ", ".join(source_names)
    combined_body = "".join(bodies)

    return (
        f"<!DOCTYPE html><html>\n"
        f"  <head>"
        f"<meta name='description' content='Combinat din: {sources}'>"
        f"</head>\n"
        f"  <body>{combined_body}</body>\n"
        f"</html>"
    )


def combine_files(input_paths: list[str], output_path: str) -> None:
    """
    Combină mai multe fișiere HTML într-un singur fișier de ieșire.

    Pipeline pentru fiecare fișier:
      1. Citire fișier
      2. extract_body → body content
      3. build_combined_html → document complet
      4. Scriere la output_path

    Exemplu:
        combine_files(["a.html", "b.html"], "combined.html")
    """
    # Pas 1 + 2: citire și extragere body pentru fiecare fișier
    bodies = list(map(
        lambda path: extract_body(open(path, encoding="utf-8").read()),
        input_paths
    ))

    # Pas 3: construiește documentul combinat
    source_names = [path.split("/")[-1] for path in input_paths]
    combined = build_combined_html(bodies, source_names)

    # Pas 4: scriere la output
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(combined)
