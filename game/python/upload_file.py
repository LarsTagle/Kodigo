import tkinter as tk
import os
import sys
import json
from docx import Document
from pdfminer.high_level import extract_text
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer
from collections import Counter

from preprocess import clean_text

from tkinter.filedialog import askopenfilename
tk.Tk().withdraw() # part of the import if you are not using other tkinter functions

fn = askopenfilename()

if os.path.splitext(fn)[1] == ".txt":
    # Open the file in read mode
    with open(fn, "r", encoding='utf-8') as file:
        # Read the contents of the file
        text = file.read()
elif os.path.splitext(fn)[1] == ".docx":
    doc = Document(fn)

    text = []

    for paragraph in doc.paragraphs:
        text.append(paragraph.text)
    
    text = '\n'.join(text)
elif os.path.splitext(fn)[1] == ".pdf":
    #text = extract_text(fn)
    pages = []
    headers = []
    footers = []
    for page_layout in extract_pages(fn):
        page = []
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                page.append(element.get_text())
        
        if page:
            headers.append(page[0])
            footers.append(page[-1])
        pages.append(page)

    header_counter = Counter(headers)
    footer_counter = Counter(footers)

    if len(header_counter) == 1:
        common_header = header_counter.most_common(1)[0][0]

        for page in pages:
            if page[0] == common_header:
                page.pop(0)

    if len(footer_counter) == 1:
        common_footer = footer_counter.most_common(1)[0][0]
        print(common_footer)
    
        for page in pages:
            if page and page[-1] == common_footer:
                page.pop(-1)
    
    text = []
    for page in pages:
        page = ''.join(page)
        text.append(page)

    text = ' '.join(text)

text = clean_text(text)

fn= sys.argv[1]

base_path = os.getcwd()
relative_path = f"kodigo\\game\\python\\temp\\{fn}.json"
fp =  os.path.join(base_path, relative_path)#f"D:\\renpy-8.1.3-sdk\\kodigo\\game\\python\\docs\\{filename}.json"

#read the json file
with open(fp, 'r') as file:
    quiz = json.load(file)

quiz["notes"] = text

#save the updated data back to json
with open(fp, 'w') as file:
    json.dump(quiz, file)