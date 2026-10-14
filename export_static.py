import os
import shutil
from pathlib import Path
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio.settings")
django.setup()

from django.test import Client

docs_dir = Path("docs")
docs_dir.mkdir(exist_ok=True)

output = docs_dir / "index.html"
backup = docs_dir / "index.backup.html"

response = Client(HTTP_HOST="localhost").get("/")

print("Django response status:", response.status_code)

if response.status_code == 200:
    if output.exists() and not backup.exists():
        backup.write_bytes(output.read_bytes())

    html = response.content.decode("utf-8")
    # Fix paths for static hosting (GitHub Pages)
    html = html.replace('/static/', './static/')
    html = html.replace('/media/', './media/')

    output.write_text(html, encoding="utf-8")
    print(f"SUCCESS: Exported to {output} ({len(html.encode('utf-8'))} bytes)")

    # Sync static and media into docs
    print("Syncing static files into docs/static...")
    shutil.copytree("static", "docs/static", dirs_exist_ok=True)

    print("Syncing media files into docs/media...")
    shutil.copytree("media", "docs/media", dirs_exist_ok=True)

    print("Export and asset sync completed successfully!")
else:
    print("Export stopped. Existing docs/index.html was not changed.")
    print(response.content[:1500].decode("utf-8", errors="replace"))
