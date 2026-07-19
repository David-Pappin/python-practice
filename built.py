import pymupdf4llm
md = pymupdf4llm.to_markdown("atbs.pdf")
open("atbs.md", "w").write(md)