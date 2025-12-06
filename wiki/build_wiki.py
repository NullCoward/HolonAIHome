"""Build wiki HTML pages from markdown files."""
import re
from pathlib import Path

WIKI_SOURCE = Path("C:/Users/Null/claude/HolonicEngine-Wiki")
WIKI_DEST = Path("C:/Users/Null/claude/HolonAIHome/wiki")

# Map of markdown files to HTML output names and titles
PAGES = {
    "architecture.md": ("architecture.html", "Architecture"),
    "memory-lattice.md": ("memory-lattice.html", "Memory Lattice"),
    "heartbeat-system.md": ("heartbeat.html", "Heartbeat System"),
    "trigger-scripts.md": ("triggers.html", "Trigger Scripts"),
    "token-hud.md": ("token-hud.html", "Token HUD"),
    "vision-creativity.md": ("creativity.html", "Cross-Domain Creativity"),
}

def md_to_html_content(md_content):
    """Convert markdown to HTML content."""
    html = md_content

    # Remove title (first # line)
    html = re.sub(r'^#[^#\n]+\n+', '', html)

    # Code blocks with ```
    def code_block(match):
        lang = match.group(1) or ''
        code = match.group(2)
        code = code.replace('<', '&lt;').replace('>', '&gt;')
        return f'<pre><code class="{lang}">{code}</code></pre>'
    html = re.sub(r'```(\w*)\n(.*?)```', code_block, html, flags=re.DOTALL)

    # Inline code
    html = re.sub(r'`([^`]+)`', r'<code>\1</code>', html)

    # Headers
    html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)

    # Bold and italic
    html = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', html)

    # Blockquotes
    html = re.sub(r'^> (.+)$', r'<blockquote><p>\1</p></blockquote>', html, flags=re.MULTILINE)

    # Horizontal rules
    html = re.sub(r'^---+$', '<hr>', html, flags=re.MULTILINE)

    # Tables (basic)
    def table_convert(text):
        lines = text.strip().split('\n')
        if len(lines) < 2:
            return text

        result = ['<table><thead><tr>']
        headers = [h.strip() for h in lines[0].split('|') if h.strip()]
        for h in headers:
            result.append(f'<th>{h}</th>')
        result.append('</tr></thead><tbody>')

        for line in lines[2:]:  # Skip header separator
            if '|' in line:
                result.append('<tr>')
                cells = [c.strip() for c in line.split('|') if c.strip()]
                for c in cells:
                    result.append(f'<td>{c}</td>')
                result.append('</tr>')
        result.append('</tbody></table>')
        return '\n'.join(result)

    # Find table blocks
    table_pattern = r'(\|[^\n]+\|\n\|[-:\| ]+\|\n(?:\|[^\n]+\|\n?)+)'
    html = re.sub(table_pattern, lambda m: table_convert(m.group(1)), html)

    # Lists
    lines = html.split('\n')
    in_list = False
    new_lines = []
    for line in lines:
        if re.match(r'^- ', line):
            if not in_list:
                new_lines.append('<ul>')
                in_list = True
            new_lines.append(f'<li>{line[2:]}</li>')
        elif re.match(r'^\d+\. ', line):
            if not in_list:
                new_lines.append('<ol>')
                in_list = True
            new_lines.append(f'<li>{re.sub(r"^\d+\. ", "", line)}</li>')
        else:
            if in_list and line.strip() == '':
                new_lines.append('</ul>' if new_lines[-2].startswith('<li>') else '</ol>')
                in_list = False
            new_lines.append(line)
    if in_list:
        new_lines.append('</ul>')
    html = '\n'.join(new_lines)

    # Paragraphs - wrap non-tag lines
    paragraphs = []
    for block in re.split(r'\n\n+', html):
        block = block.strip()
        if not block:
            continue
        if block.startswith('<') or block.startswith('#'):
            paragraphs.append(block)
        else:
            paragraphs.append(f'<p>{block}</p>')

    return '\n\n'.join(paragraphs)


def make_page(title, content, active_page):
    """Generate full HTML page."""
    nav_links = [
        ("/wiki/", "Overview", "index.html"),
        ("/wiki/holon.html", "What is a Holon?", "holon.html"),
        ("/wiki/architecture.html", "Architecture", "architecture.html"),
        ("/wiki/memory-lattice.html", "Memory Lattice", "memory-lattice.html"),
    ]
    nav_systems = [
        ("/wiki/heartbeat.html", "Heartbeat System", "heartbeat.html"),
        ("/wiki/triggers.html", "Trigger Scripts", "triggers.html"),
        ("/wiki/token-hud.html", "Token HUD", "token-hud.html"),
    ]
    nav_vision = [
        ("/wiki/creativity.html", "Cross-Domain Creativity", "creativity.html"),
        ("/wiki/glossary.html", "Glossary", "glossary.html"),
    ]

    def nav_link(href, text, page):
        active = ' class="nav-link active"' if page == active_page else ' class="nav-link"'
        return f'<a href="{href}"{active}>{text}</a>'

    core_links = '\n'.join(nav_link(*l) for l in nav_links)
    system_links = '\n'.join(nav_link(*l) for l in nav_systems)
    vision_links = '\n'.join(nav_link(*l) for l in nav_vision)

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - HolonicEngine Wiki</title>
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        :root {{
            --bg-void: #0a0a0f;
            --bg-surface: rgba(15, 15, 25, 0.8);
            --bg-elevated: rgba(20, 20, 35, 0.9);
            --foam-1: #00ffcc;
            --foam-2: #00d4ff;
            --text-primary: rgba(255, 255, 255, 0.95);
            --text-secondary: rgba(255, 255, 255, 0.7);
            --text-muted: rgba(255, 255, 255, 0.4);
            --border-subtle: rgba(255, 255, 255, 0.08);
            --border-glow: rgba(0, 212, 255, 0.3);
        }}
        body {{ background: var(--bg-void); min-height: 100vh; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; color: var(--text-primary); line-height: 1.6; }}
        .void-bg {{ position: fixed; inset: 0; background: radial-gradient(ellipse at 30% 20%, rgba(0, 100, 150, 0.08) 0%, transparent 50%), radial-gradient(ellipse at 50% 50%, #0d0d15 0%, var(--bg-void) 70%); z-index: 0; }}
        .wiki-container {{ position: relative; z-index: 10; display: flex; min-height: 100vh; }}
        .sidebar {{ width: 280px; background: var(--bg-surface); border-right: 1px solid var(--border-subtle); padding: 2rem 0 5rem 0; position: fixed; height: 100vh; overflow-y: auto; backdrop-filter: blur(20px); }}
        .sidebar-header {{ padding: 0 1.5rem 1.5rem; border-bottom: 1px solid var(--border-subtle); margin-bottom: 1rem; }}
        .sidebar-logo {{ display: flex; align-items: center; gap: 0.75rem; text-decoration: none; color: var(--text-primary); }}
        .sidebar-logo-icon {{ width: 36px; height: 36px; border-radius: 50%; background: linear-gradient(135deg, var(--foam-1), var(--foam-2)); display: flex; align-items: center; justify-content: center; font-weight: bold; color: var(--bg-void); }}
        .sidebar-logo-text {{ font-size: 1.1rem; font-weight: 600; }}
        .sidebar-tagline {{ margin-top: 0.5rem; font-size: 0.8rem; color: var(--foam-2); font-style: italic; }}
        .nav-section {{ padding: 1rem 1.5rem 0.5rem; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.1em; color: var(--text-muted); font-weight: 600; }}
        .nav-link {{ display: block; padding: 0.6rem 1.5rem; color: var(--text-secondary); text-decoration: none; font-size: 0.9rem; border-left: 2px solid transparent; transition: all 0.2s; }}
        .nav-link:hover {{ color: var(--text-primary); background: rgba(0, 212, 255, 0.05); border-left-color: var(--foam-2); }}
        .nav-link.active {{ color: var(--foam-2); background: rgba(0, 212, 255, 0.08); border-left-color: var(--foam-2); }}
        .back-link {{ display: flex; align-items: center; gap: 0.5rem; padding: 1rem 1.5rem; color: var(--text-muted); text-decoration: none; font-size: 0.85rem; border-top: 1px solid var(--border-subtle); position: fixed; bottom: 0; left: 0; width: 280px; background: var(--bg-surface); backdrop-filter: blur(20px); }}
        .back-link:hover {{ color: var(--text-secondary); }}
        .main-content {{ flex: 1; margin-left: 280px; padding: 3rem 4rem 4rem; max-width: 900px; }}
        h1 {{ font-size: 2.5rem; font-weight: 300; margin-bottom: 2rem; background: linear-gradient(135deg, var(--text-primary), var(--foam-2)); -webkit-background-clip: text; background-clip: text; color: transparent; }}
        h2 {{ font-size: 1.5rem; font-weight: 500; margin: 2.5rem 0 1rem; color: var(--text-primary); padding-bottom: 0.5rem; border-bottom: 1px solid var(--border-subtle); }}
        h3 {{ font-size: 1.15rem; font-weight: 600; margin: 1.5rem 0 0.75rem; color: var(--foam-1); }}
        p {{ margin-bottom: 1rem; color: var(--text-secondary); }}
        strong {{ color: var(--text-primary); }}
        em {{ color: var(--foam-2); font-style: italic; }}
        ul, ol {{ margin: 1rem 0; padding-left: 1.5rem; }}
        li {{ margin-bottom: 0.5rem; color: var(--text-secondary); }}
        pre {{ background: var(--bg-elevated); border: 1px solid var(--border-subtle); border-radius: 8px; padding: 1.25rem; overflow-x: auto; margin: 1.5rem 0; font-family: 'SF Mono', 'Fira Code', monospace; font-size: 0.85rem; line-height: 1.5; white-space: pre-wrap; word-wrap: break-word; }}
        code {{ font-family: 'SF Mono', 'Fira Code', monospace; font-size: 0.9em; color: var(--foam-2); }}
        pre code {{ color: var(--text-secondary); }}
        blockquote {{ border-left: 3px solid var(--foam-2); padding: 1rem 1.5rem; margin: 1.5rem 0; background: rgba(0, 212, 255, 0.05); border-radius: 0 8px 8px 0; }}
        blockquote p {{ margin: 0; color: var(--text-primary); font-size: 1.1rem; }}
        table {{ width: 100%; border-collapse: collapse; margin: 1.5rem 0; }}
        th, td {{ padding: 0.75rem 1rem; text-align: left; border-bottom: 1px solid var(--border-subtle); }}
        th {{ color: var(--foam-1); font-weight: 600; background: var(--bg-elevated); }}
        td {{ color: var(--text-secondary); }}
        hr {{ border: none; border-top: 1px solid var(--border-subtle); margin: 2rem 0; }}
        a {{ color: var(--foam-2); text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
        @media (max-width: 900px) {{
            .sidebar {{ width: 100%; height: auto; position: relative; padding-bottom: 1rem; }}
            .main-content {{ margin-left: 0; padding: 2rem 1.5rem; }}
            .back-link {{ position: relative; width: 100%; }}
        }}
    </style>
</head>
<body>
    <div class="void-bg"></div>
    <div class="wiki-container">
        <nav class="sidebar">
            <div class="sidebar-header">
                <a href="/wiki/" class="sidebar-logo">
                    <div class="sidebar-logo-icon">H</div>
                    <span class="sidebar-logo-text">HolonicEngine</span>
                </a>
                <div class="sidebar-tagline">Agents with Agency</div>
            </div>
            <div class="nav-section">Core Concepts</div>
            {core_links}
            <div class="nav-section">Systems</div>
            {system_links}
            <div class="nav-section">Vision</div>
            {vision_links}
        </nav>
        <a href="/" class="back-link"><span>&larr;</span> Back to Holonic.org</a>
        <main class="main-content">
            <h1>{title}</h1>
            {content}
        </main>
    </div>
</body>
</html>'''


def build_all():
    for md_file, (html_file, title) in PAGES.items():
        md_path = WIKI_SOURCE / md_file
        html_path = WIKI_DEST / html_file

        if not md_path.exists():
            print(f"Skipping {md_file} - not found")
            continue

        md_content = md_path.read_text(encoding='utf-8')
        html_content = md_to_html_content(md_content)
        full_page = make_page(title, html_content, html_file)

        html_path.write_text(full_page, encoding='utf-8')
        print(f"Built {html_file}")


if __name__ == "__main__":
    build_all()
    print("Done!")
