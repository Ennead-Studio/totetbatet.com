"""Génère les pages statiques du site totetbatet.com.

Usage : python _build/build.py   (depuis le dossier 07_site_web)
Chaque page = un fichier HTML dans _build/pages/ (corps seulement) ; ce script
ajoute l'en-tête, la navigation et le pied de page communs.
"""
import pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGES = ROOT / "_build" / "pages"

NAV = [
    ("application", "L'application"),
    ("about", "À propos"),
    ("espace-partenaires", "Éditeurs"),
    ("faq", "FAQ"),
    ("contact", "Contact"),
]

HEAD = """<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://www.totetbatet.com/assets/ecoutent-histoire.webp">
<meta property="og:type" content="website">
<link rel="icon" href="/assets/icone.webp">
<link rel="stylesheet" href="/assets/style.css">
</head>
<body>
<a class="skip" href="#contenu">Aller au contenu</a>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="/" aria-label="Tot &amp; Batet – accueil"><img src="/assets/logo-banner.webp" alt="Tot &amp; Batet" width="258" height="44"></a>
    <button class="menu-toggle" aria-expanded="false" aria-controls="nav">Menu</button>
    <nav class="nav" id="nav" aria-label="Navigation principale">
{nav}
    </nav>
  </div>
</header>
<div class="ribbon">L'application est en cours de développement. Tot &amp; Batet est un projet <a href="https://ennead-studio.github.io/">Ennead Studio</a>.</div>
<main id="contenu">
"""

FOOT = """</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="cols">
      <div>
        <h3>Tot &amp; Batet</h3>
        <p>La boîte à histoires sécurisée qui transforme le smartphone en conteur, écran éteint.</p>
        <p>Un projet <a href="https://ennead-studio.github.io/">Ennead Studio</a> · Paris, France</p>
      </div>
      <div>
        <h3>Contact</h3>
        <ul>
          <li><a href="mailto:contact@totetbatet.com">contact@totetbatet.com</a></li>
          <li><a href="mailto:partenaires@totetbatet.com">partenaires@totetbatet.com</a></li>
        </ul>
      </div>
      <div>
        <h3>Informations</h3>
        <ul>
          <li><a href="/mentions-legales">Mentions légales</a></li>
          <li><a href="/politique-de-confidentialite">Confidentialité</a></li>
          <li><a href="/conditions-dutilisation">Conditions d'utilisation</a></li>
        </ul>
      </div>
    </div>
    <p class="small">© 2025-2026 Tot &amp; Batet Media. Illustrations et textes protégés : toute reproduction sans autorisation est interdite.</p>
  </div>
</footer>
<script>
  (function(){var b=document.querySelector('.menu-toggle'),n=document.getElementById('nav');
  if(!b||!n)return;b.addEventListener('click',function(){var o=n.classList.toggle('open');b.setAttribute('aria-expanded',o);});})();
</script>
</body>
</html>
"""

def build():
    for src in sorted(PAGES.glob("*.html")):
        raw = src.read_text(encoding="utf-8")
        meta = dict(re.findall(r"<!--\s*(\w+):\s*(.*?)\s*-->", raw[:600]))
        body = re.sub(r"^(\s*<!--.*?-->\s*)+", "", raw, flags=re.S)
        slug = src.stem
        cur = ' aria-current="page"'
        nav = "\n".join(
            f'      <a href="/{s}"{cur if s == slug else ""}>{label}</a>'
            for s, label in NAV)
        html = HEAD.format(title=meta.get("title", "Tot & Batet"),
                           desc=meta.get("desc", ""), nav=nav) + body + FOOT
        out = ROOT / ("index.html" if slug == "index" else f"{slug}.html")
        out.write_text(html, encoding="utf-8")
        print("écrit", out.name)

    # anciennes adresses Squarespace -> nouvelles
    redirects = {"mentions-lgales": "/mentions-legales", "home": "/", "cart": "/"}
    for old, new in redirects.items():
        (ROOT / f"{old}.html").write_text(
            f'<!doctype html><html lang="fr"><head><meta charset="utf-8">'
            f'<meta http-equiv="refresh" content="0; url={new}"><link rel="canonical" href="{new}">'
            f'<title>Redirection</title></head><body><a href="{new}">Continuer</a></body></html>',
            encoding="utf-8")
        print("redirection", old, "->", new)

if __name__ == "__main__":
    build()
