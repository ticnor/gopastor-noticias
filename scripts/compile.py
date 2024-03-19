#!/usr/bin/env python3
import json
from os.path import relpath
from pathlib import Path
import re
from urllib.parse import quote

from markdown import Markdown

BASE_URL = 'https://ticnor.github.io/gopastor-noticias/'

md = Markdown(extensions=['meta'])


def image_url(url: str, md_path: Path):
    if re.match(f'^https?://', url):
        return url
    return f"{BASE_URL}{quote(relpath(md_path.parent.joinpath(url)))}"


posts = []
for fn in Path('posts').rglob('*.md'):
    print("Compiling", fn)
    with open(fn) as f:
        html = md.convert(f.read())
    metadata = md.Meta
    posts.append({
        'filename': str(fn),
        'title': metadata['title'][0],
        'images': [image_url(i, fn) for i in metadata.get('image', [])],
        'date': metadata['date'][0],
        'content': html,
    })

posts.sort(reverse=True, key=lambda x: x['filename'])

output = Path('noticias.json')
with open(output, 'w') as f:
    json.dump(posts, f)

print(len(posts), "posts written")
