import pymupdf4llm

def read_pdf(filepath) -> list[str]:
    md_read = pymupdf4llm.LlamaMarkdownReader()
    data = md_read.load_data(filepath)
    return data