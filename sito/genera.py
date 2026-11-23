"""Generate the two static pages from contenuti.json."""
import json
import re
from html import escape
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent
DATA = json.loads((ROOT / "contenuti.json").read_text(encoding="utf-8"))
GUIDE = (ROOT.parent / "COSA_SA_FARE.md").read_text(encoding="utf-8")
COMMAND_GROUPS = re.findall(
    r"^## ([^\n]+)\n(.*?)(?=^## |\Z)", GUIDE.split("\n## Miniguida:", 1)[0], re.M | re.S
)
ICONS = [
    '<rect x="9" y="3" width="6" height="12" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3m-3 0h6"/>',
    '<path d="M3 12h2l2-5 3 10 3-14 3 17 2-8h3"/>',
    '<path d="m13 2-8 12h6l-1 8 9-12h-6z"/>',
    '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9h18m-14 5h4"/>',
    '<path d="M3 9h4l5-4v14l-5-4H3zM16 9a4 4 0 0 1 0 6m3-9a8 8 0 0 1 0 12"/>',
    '<path d="M4 9V4h5m6 0h5v5m0 6v5h-5m-6 0H4v-5"/><circle cx="12" cy="12" r="3"/>',
    '<rect x="3" y="5" width="18" height="14" rx="2"/><circle cx="12" cy="12" r="3"/>',
    '<path d="M4 6h16M4 12h16M4 18h16"/><path d="M8 4v4m8 2v4m-6 2v4" stroke-width="3"/>',
]


def valid_video_url(url):
    if not url or any(char.isspace() or char == "\\" for char in url):
        return False
    try:
        parts = urlsplit(url)
        return parts.scheme == "https" and bool(parts.hostname) and parts.username is None and parts.port != 0
    except ValueError:
        return False


def render(lang):
    tr = {key: escape(value) for key, value in DATA[lang].items() if isinstance(value, str)}
    name = escape(DATA["nome"])
    title = f"{name} — {tr['titolo_hero']}"
    prefix = "./" if lang == "it" else "../"
    base = DATA["url"].rstrip("/") + "/"
    canonical = base if lang == "it" else base + "en/"
    links = {key: escape(value) for key, value in DATA["link"].items()}
    buttons = {key: escape(value) for key, value in DATA["pulsanti"].items()}
    logo = escape(prefix + DATA["logo"])
    page_locale = "it_IT" if lang == "it" else "en_US"
    other_locale = "en_US" if lang == "it" else "it_IT"

    def screenshot(item):
        width, height = item["misure"]
        retina = item.get("file_2x")
        srcset = f' srcset="{escape(prefix + retina)} 2x"' if retina else ""
        return (f'<img src="{escape(prefix + item["file"])}"{srcset} width="{int(width)}" '
                f'height="{int(height)}" alt="{escape(item[lang])}" fetchpriority="high">')

    nav = "".join(f'<a href="#{section}">{escape(label)}</a>' for section, label in zip(
        ("funzionalita", "installazione", "supporto"), DATA[lang]["nav"], strict=True))
    command_panels = []
    for category, content in COMMAND_GROUPS:
        commands = "".join(
            f'<li><strong>{escape(label)}</strong><p>{escape(description)}</p></li>'
            for label, description in re.findall(r"^- \*\*(.+?):\*\* (.+)$", content, re.M)
        )
        command_panels.append(f'<section class="command-group"><h3>{escape(category)}</h3><ul>{commands}</ul></section>')
    current = ' aria-current="page"'
    languages = "".join(
        f'<a href="{prefix}{path}" lang="{code}" hreflang="{code}"'
        f'{current if code == lang else ""}>{code.upper()}</a>'
        for code, path in (("it", "index.html"), ("en", "en/index.html")))
    cards = "".join(
        f'<li class="card"><svg viewBox="0 0 24 24" aria-hidden="true">{icon}</svg>'
        f'<h3>{escape(name)}</h3><p>{escape(body)}</p></li>'
        for icon, (name, body) in zip(ICONS, DATA[lang]["schede"], strict=True))
    distros = "".join(f'<li><strong>{escape(name)}</strong><span>{escape(de)}</span></li>'
                     for name, de in DATA["distribuzioni"])
    steps = []
    for number, (step_name, body) in enumerate(DATA[lang]["passi"], 1):
        command = '<code>bash installa.sh</code>' if number == 2 else ""
        steps.append(f'<li><span class="step-number" aria-hidden="true">{number}</span>'
                     f'<h3>{escape(step_name)}</h3><p>{escape(body)}</p>{command}</li>')
    social = DATA["social"]
    og_image = escape(base + social["file"])
    image_width, image_height = social["misure"]
    image_alt = escape(social[lang])
    examples = "".join(f'<li>«{escape(example)}»</li>' for example in DATA["esempi_vocali"])
    video_url = DATA["link"].get("video", "").strip()
    video = (f'\n            <a class="button secondary" href="{escape(video_url)}">{tr["guarda_video"]}</a>'
             if valid_video_url(video_url) else "")
    footer = "".join(f'<a href="{links[key]}">{label}</a>' for key, label in
                     (("github", "GitHub"), ("release", "Release"), ("licenza", "GPLv3"), ("autore", "Kapaklia")))
    return f"""<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{tr['descrizione']}">
  <meta name="theme-color" content="#101d24">
  <link rel="canonical" href="{escape(canonical)}">
  <link rel="alternate" hreflang="it" href="{escape(base)}">
  <link rel="alternate" hreflang="en" href="{escape(base + 'en/')}">
  <link rel="alternate" hreflang="x-default" href="{escape(base)}">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{tr['descrizione']}">
  <meta property="og:locale" content="{page_locale}">
  <meta property="og:locale:alternate" content="{other_locale}">
  <meta property="og:url" content="{escape(canonical)}">
  <meta property="og:image" content="{og_image}">
  <meta property="og:image:width" content="{image_width}">
  <meta property="og:image:height" content="{image_height}">
  <meta property="og:image:alt" content="{image_alt}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{tr['descrizione']}">
  <meta name="twitter:image" content="{og_image}">
  <meta name="twitter:image:alt" content="{image_alt}">
  <link rel="icon" href="{logo}">
  <link rel="stylesheet" href="{prefix}tema.css">
  <link rel="stylesheet" href="{prefix}stile.css">
</head>
<body>
  <a class="skip" href="#contenuto">{tr['salta']}</a>
  <header class="top">
    <div class="wrap top-inner">
      <nav class="site-nav" aria-label="{ 'Sezioni' if lang == 'it' else 'Sections' }">
        <a class="brand" href="#home"><img src="{logo}" width="36" height="36" alt="">{name}</a>{nav}
      </nav>
      <nav class="languages" aria-label="{ 'Lingua' if lang == 'it' else 'Language' }">{languages}</nav>
    </div>
  </header>
  <main id="contenuto" tabindex="-1">
    <section class="hero" id="home" aria-labelledby="titolo">
      <div class="atmosfera" aria-hidden="true"></div>
      <div class="wrap hero-inner">
        <div class="hero-copy">
          <img class="hero-logo" src="{logo}" alt="" width="88" height="88">
          <h1 id="titolo">{name} <span class="title-dash">—</span> <span class="title-sub">{tr['titolo_hero']}</span></h1>
          <p class="lead">{tr['sottotitolo']}</p>
          <div class="actions">
            <a class="button primary" href="{links['release_attuale']}">{buttons['download']}</a>
            <a class="button secondary" href="{links['github']}">{buttons['github']}</a>{video}
          </div>
          <ul class="hero-facts"><li>{tr['gratuito']}</li><li>Open source</li><li>{tr['voce']}</li></ul>
          <div class="voice-examples">
            <p>{tr['esempi']}</p>
            <ul lang="it">{examples}</ul>
          </div>
        </div>
        <div class="hero-preview">{screenshot(DATA['schermate'][0])}</div>
      </div>
    </section>
    <section class="wrap section" id="funzionalita">
      <h2>{tr['funzioni']}</h2>
      <ul class="features">{cards}</ul>
      <details class="commands">
        <summary>{tr['tutti_comandi']}</summary>
        <div class="command-groups" lang="it">{''.join(command_panels)}</div>
      </details>
    </section>
    <section class="wrap section" id="installazione">
      <h2>{tr['installazione']}</h2>
      <ol class="steps">{''.join(steps)}</ol>
      <div class="distro-panel" id="compatibilita">
        <h2>{tr['compatibilita']}</h2>
        <ul>{distros}</ul>
      </div>
    </section>
    <section class="wrap section" id="supporto">
      <div class="support-panel">
        <div><h2>{tr['supporto']}</h2>{''.join(f'<p>{paragraph}</p>' for paragraph in tr['storia'].splitlines() if paragraph)}</div>
        <a class="button secondary" href="{links['paypal']}">{tr['donazione']}</a>
      </div>
    </section>
  </main>
  <footer class="foot">
    <div class="wrap"><nav aria-label="{ 'Link del progetto' if lang == 'it' else 'Project links' }">{footer}</nav></div>
  </footer>
</body>
</html>
"""


if __name__ == "__main__":
    for language, directory in (("it", ROOT / "dist"), ("en", ROOT / "dist" / "en")):
        directory.mkdir(parents=True, exist_ok=True)
        (directory / "index.html").write_text(render(language), encoding="utf-8")
