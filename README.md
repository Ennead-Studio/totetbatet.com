# Site totetbatet.com — version statique

Remplace le site Squarespace (17 € HT/mois) par un site statique gratuit hébergé sur GitHub Pages.
Les adresses des pages sont les mêmes que sur Squarespace (`/about`, `/application`, `/faq`, `/contact`,
`/espace-partenaires`, `/politique-de-confidentialite`, `/conditions-dutilisation`) ; l'ancienne
`/mentions-lgales` redirige vers `/mentions-legales`.

## Modifier le site

1. Modifier le contenu dans `_build/pages/*.html` (le corps de chaque page ; les 2 premières lignes
   `<!-- title: … -->` et `<!-- desc: … -->` donnent le titre et la description).
2. En-tête, menu et pied de page communs : `_build/build.py`. Styles : `assets/style.css`.
3. Régénérer : `python _build/build.py` (depuis ce dossier).

Aperçu local : n'importe quel petit serveur (les liens sont absolus, `/assets/...`), par exemple
`python -m http.server` puis http://localhost:8000/ (sur ce serveur, ajouter `.html` aux adresses).

## Mise en ligne (une fois)

1. Créer un dépôt **public** sur GitHub (GitHub Pages gratuit = dépôt public) et y pousser ce dossier.
2. Dépôt > Settings > Pages : *Deploy from a branch*, branche `main`, dossier `/ (root)`.
   *Custom domain* : `www.totetbatet.com` (le fichier `CNAME` est déjà là).
3. DNS du domaine (Squarespace Domains, ex-Google Domains) — **ne toucher qu'à ces lignes** :
   - `www` : CNAME → `<compte>.github.io` (au lieu de `ext-sq.squarespace.com`)
   - `@` (apex) : 4 enregistrements A → `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
     (à la place des A Squarespace `198.185.159.145`, `198.49.23.144`, `198.49.23.145`)
   - **Ne pas modifier** les MX (`smtp.google.com`), ni les TXT (SPF, DKIM, vérification Google) :
     ce sont eux qui font marcher la messagerie @totetbatet.com.
4. Attendre la propagation (quelques minutes à quelques heures), puis cocher *Enforce HTTPS* dans Settings > Pages.
5. Vérifier www.totetbatet.com et totetbatet.com, puis **résilier l'abonnement « Site web » Squarespace
   avant le 04/12/2026** (le domaine, lui, reste : il est facturé à part jusqu'au 27/10/2027).

## À savoir

- Plus de formulaire de contact : les visiteurs écrivent à contact@ / partenaires@totetbatet.com
  (alias Google Workspace à conserver).
- Polices (Alice, Work Sans) hébergées localement : aucun appel à des services tiers, aucun cookie.
- Mentions légales : mettre à jour le siège social après le transfert à Versailles.
