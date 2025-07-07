import fitz  
import re

def extract_links_from_pdf(pdf_path):
    doc=fitz.open(pdf_path)
    urls=[]

    for page_num in range(len(doc)):
        page=doc[page_num]
        text=page.get_text()
        links=re.findall(r'(https?://[^\s)]+)', text)
        urls.extend(links)

    seen=set()
    clean_urls=[]
    for url in urls:
        if url not in seen:
            seen.add(url)
            clean_urls.append(url)

    return clean_urls


pdf_path =r"UserID311.pdf"
urls=extract_links_from_pdf(pdf_path)

for i, url in enumerate(urls, 1):
    print(f"{i}. {url}")
