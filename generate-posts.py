#! /usr/bin/env python3

import os
import time
from pathlib import Path
from string import Template

frontmatter = Template("""---
layout: post
title: "$title"
preview: images/$file_name
---

![$title](/images/$file_name)
""")

images_dir = "./images"
posts_dir = "./_posts"

images = os.listdir(images_dir)

for image in images:
  name = Path(image).stem
  date = time.strftime("%Y-%m-%d", time.localtime(os.path.getctime(os.path.join(images_dir, image))))
  post_file_name = date + "-" + name + ".markdown"
  title = name.replace('-', ' ').title()
  contents = frontmatter.safe_substitute(title=title, file_name=image)
  print("writing", post_file_name)
  with open(os.path.join(posts_dir, post_file_name), 'w') as f:
    f.write(contents)
