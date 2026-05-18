#!/usr/bin/env python3
"""
md2html.py — Convert all .md files in docs/ to styled .html pages.
Usage: python3 tools/md2html.py
Requires: pip install markdown
"""
import os, re, glob
from pathlib import Path

try:
    import markdown
except ImportError:
    os.system("pip install markdown --break-system-packages -q")
    import markdown

DOCS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs")
MD_EXTENSIONS = ["tables", "fenced_code", "toc", "nl2br", "sane_lists", "smarty"]

def depth_prefix(md_path):
    rel = os.path.relpath(md_path, DOCS_DIR)
    d = rel.count(os.sep)
    return "../" * d if d > 0 else ""

def md_to_title(md_path):
    with open(md_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip().startswith("# "):
                return line.strip().lstrip("# ").strip()
    return Path(md_path).stem.replace("-", " ").replace("_", " ").title()

def detect_section(rel):
    if rel.startswith("method"): return "method"
    if rel.startswith("partner-mapping"): return "partners"
    if rel.startswith("absm-sprint"): return "absm"
    return "memo"

def sidebar_html(p):
    return f"""
<div class="sidebar__section">
  <button class="sidebar__heading"><span class="caret">▼</span> Memo</button>
  <ul class="sidebar__list"><li class="sidebar__item"><a href="{p}index.html">Homepage</a></li></ul>
</div>
<div class="sidebar__section">
  <button class="sidebar__heading"><span class="caret">▼</span> Method</button>
  <ul class="sidebar__list">
    <li class="sidebar__item"><a href="{p}method/index.html">Overview</a></li>
    <li class="sidebar__item"><a href="{p}method/spider-chart.html">Spider Chart</a></li>
    <li class="sidebar__item"><a href="{p}method/scorecard-template.html">Scorecard Template</a></li>
  </ul>
</div>
<div class="sidebar__section">
  <button class="sidebar__heading"><span class="caret">▼</span> Partner Mapping</button>
  <ul class="sidebar__list">
    <li class="sidebar__item"><a href="{p}partner-mapping/index.html">Overview</a></li>
    <li class="sidebar__item"><a href="{p}partner-mapping/dach-landscape.html">DACH Landscape</a></li>
    <li class="sidebar__item"><a href="{p}partner-mapping/pursue-five/all-five-profiles.html">Pursue Five</a></li>
    <li class="sidebar__item"><a href="{p}partner-mapping/entanglement/entanglement-matrix.html">Entanglement</a></li>
  </ul>
</div>
<div class="sidebar__section">
  <button class="sidebar__heading"><span class="caret">▼</span> ABSM Sprint</button>
  <ul class="sidebar__list">
    <li class="sidebar__item"><a href="{p}absm-sprint/index.html">Overview</a></li>
    <li class="sidebar__item"><a href="{p}absm-sprint/01-targeting/icp-definition.html">Targeting</a></li>
    <li class="sidebar__item"><a href="{p}absm-sprint/02-strategy/sweet-spot-profile.html">Strategy</a></li>
    <li class="sidebar__item"><a href="{p}absm-sprint/03-clients/hoermann/company-brief.html">Clients</a></li>
    <li class="sidebar__item"><a href="{p}absm-sprint/05-infrastructure/crm-spec-hubspot.html">Infrastructure</a></li>
  </ul>
</div>"""

def nav_html(prefix, active):
    items = [("memo","index.html","Memo"),("method","method/index.html","Method"),
             ("partners","partner-mapping/index.html","Partners"),("absm","absm-sprint/index.html","ABSM")]
    return "\n".join(f'    <li><a href="{prefix}{h}"{" class=\"active\"" if k==active else ""}>{l}</a></li>' for k,h,l in items)

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | Partner Program OS</title>
  <link rel="stylesheet" href="{prefix}assets/css/main.css">
</head>
<body>
<nav class="top-nav">
  <button class="hamburger" aria-label="Toggle navigation">
    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
  </button>
  <a href="{prefix}index.html" class="top-nav__logo">Partner Program <span>OS</span></a>
  <ul class="top-nav__links">
{nav}
  </ul>
</nav>
<div class="sidebar-overlay"></div>
<aside class="sidebar">{sidebar}</aside>
<div class="layout">
  <main class="content">
    <h1 class="mt-0">{title}</h1>
    {body}
  </main>
</div>
<footer class="site-footer">
  <p>A. Marushevsky &middot; Amsterdam &middot; All partner research is a first pass from public sources.</p>
</footer>
<script src="{prefix}assets/js/sidebar.js"></script>
</body>
</html>"""

MD_LINK_RE = re.compile(r'(href=["\'])([^"\']+?)(\.md)(["\'])')

def convert_all():
    md_files = glob.glob(os.path.join(DOCS_DIR, "**", "*.md"), recursive=True)
    if not md_files:
        print(f"No .md files found in {DOCS_DIR}")
        return
    mc = markdown.Markdown(extensions=MD_EXTENSIONS)
    n = 0
    for md_path in sorted(md_files):
        rel = os.path.relpath(md_path, DOCS_DIR)
        if rel.upper() == "README.MD" or rel == "index.md":
            continue
        with open(md_path, "r", encoding="utf-8") as f:
            content = f.read()
        content = content.replace("Alex M.", "A. Marushevsky").replace("Alex Marushevsky", "A. Marushevsky")
        mc.reset()
        body = mc.convert(content)
        body = MD_LINK_RE.sub(r"\1\2.html\4", body)
        body = body.replace("Alex M.", "A. Marushevsky")
        title = md_to_title(md_path)
        prefix = depth_prefix(md_path)
        active = detect_section(rel)
        page = TEMPLATE.format(
            title=title, prefix=prefix,
            nav=nav_html(prefix, active),
            sidebar=sidebar_html(prefix),
            body=body)
        html_path = md_path.rsplit(".", 1)[0] + ".html"
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(page)
        n += 1
        print(f"  ✓ {rel} → {os.path.relpath(html_path, DOCS_DIR)}")
    print(f"\nDone: {n} files converted.")

if __name__ == "__main__":
    print(f"MD → HTML converter\\nScanning: {DOCS_DIR}\\n")
    convert_all()
