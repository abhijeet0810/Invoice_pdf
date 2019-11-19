from fpdf import FPDF
import json
import yaml

pdf = FPDF()
pdf.add_page()

pdf.set_font('Arial', size= 12)
ratio=1262./297
epw = pdf.w - 2*pdf.l_margin

global col_width ##

def make_column():
    col_width = 0
    with open('myyml_3.yaml') as f:
    
                docs = yaml.load_all(f, Loader=yaml.FullLoader)

                for doc in docs:
                    # change the value of range() according to yaml file
                    for i in range(2):
                        # pdf.set_x(doc['data'][0]['data'][0]['x'])
                        # pdf.set_y(doc['data'][0]['data'][0]['y'])
                        if doc['data'][i]['type']== "column":                            
                            col_width = col_width +1
                    print (col_width) # =2 (myyml_3.yaml)
                
make_column()

def make_paragraph():

        with open('myyml_3.yaml') as f:
    
                docs = yaml.load_all(f, Loader=yaml.FullLoader)
                
                for doc in docs:
                    for i in range(2):
                        if doc['data'][i]['type']== "column" and doc['data'][i]['data'][i]['type']== "paragraph":
                            text = doc['data'][i]['data'][i]['text']
                            pdf.multi_cell(epw/2, 5, text, border=1) # epw/col_width
                            pdf.ln(0.5)

make_paragraph()

pdf.output('full_invoice.pdf','F')



