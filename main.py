"""Inspired by the README of the author of rich.

See:
    https://github.com/willmcgugan/willmcgugan

Create README.md by running: 
    (pip install rich)
    python main.py
"""

from rich import box
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree

console = Console(record=True, width=150)

tree = Tree("🤠 [link=https://www.paulbroek.com]Paul Broek", guide_style="bold cyan")
packages_tree = tree.add("🐍 Packages")
packages_tree.add("[link=https://github.com/paulbroek/youtube-recommender]YouTube recommender")
packages_tree.add("[link=https://github.com/paulbroek/imslp-recommender]IMSLP recommender")
packages_tree.add("[link=https://github.com/paulbroek/gcloud-utils]Google Cloud utility tools")
packages_tree.add("[link=https://github.com/paulbroek/github-notifier-js]Github notifier")
# articles_tree = tree.add("📘 Popular Articles")
# articles_tree.add("[link=https://towardsdatascience.com/...")

about = """\
Originally an econometrist, now mostly a data scientist who loves building tools to boost productivity. My interest lie in NLP, music, sustainability and environmental protection. 

Feel free to ask me anything!"""

panel = Panel.fit(
    about, box=box.DOUBLE, border_style="blue", title="[b]Hi 👋 I'm Paul", width=60
)

console.print(Columns([panel, tree]))

CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""

console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)
