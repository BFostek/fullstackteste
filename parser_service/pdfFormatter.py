import fitz
import re


def pdf_to_array(file):
    with fitz.open(file) as doc:
        pages = []
        for page in doc:
            text = page.get_text()
            cleaned_text = [word.strip() for line in text.splitlines() for word in
                            re.sub(r'\s{2,}', '\n', line).split('\n') if word.strip()]
            pages.append(cleaned_text)
        return pages
