from fpdf import FPDF
import json

pdf = FPDF()
pdf.add_page()
epw = pdf.w - 2*pdf.l_margin

pdf.set_font('Arial', size= 12)
ratio=1262./297
global_dict = {}

def make_table(data,x,y):

    col_widths = epw/4

    th = pdf.font_size
    
    #Coordiante values
    x_cord = pdf.set_x(x)
    y_cord = pdf.set_y(y)
    
    global_dict['table'] = []
    for row in data:
        for item in row:
                global_dict['table'].append({
                        'x': ratio*pdf.get_x(),
                        'y': ratio*pdf.get_y(),
                        'w': pdf.w,
                        'h': pdf.h,
                        'text': item
                })
                with open('data.json', 'w') as outfile:

                        json.dump(global_dict, outfile, indent=4)
            
                pdf.cell(col_widths, th, str(item), border=1)
        
        pdf.ln(th)

data = [['Abv', 45, 23, 52.00],
        ['Dfc', 55, 21, 99.23],
        ['Ina', 15, 26, 87.89],
        ['FGa', 75, 86, 8.9],
        ['Kjut', 95, 416, 12.9]
        ]

make_table(data=data, x=1 ,y=140 )

def make_address(address, x,y):

        #Coordiante values
        x_cord = pdf.set_x(x)
        y_cord = pdf.set_y(y)

        global_dict['address'] = []
        global_dict['address'].append({
                        'x': ratio*pdf.get_x(),
                        'y': ratio*pdf.get_y(),
                        'w': pdf.w,
                        'h': pdf.h,
                        'text': address
                })
        with open('data.json', 'w') as outfile:
                json.dump(global_dict, outfile, indent=4)
 
        pdf.multi_cell(epw/4, 5, address, border=1)
        pdf.ln(0.5)

address= """Address"""

make_address(address=address, x= 50, y=50)

def make_paragraph(paragraph, x, y):

        #Coordiante values
        x_cord = pdf.set_x(x)
        y_cord = pdf.set_y(y)

        global_dict['paragraph'] = []
        global_dict['paragraph'].append({
                        'x': ratio*pdf.get_x(),
                        'y': ratio*pdf.get_y(),
                        'w': pdf.w,
                        'h': pdf.h,
                        'text': text
                })
        with open('data.json', 'w') as outfile:
                json.dump(global_dict, outfile, indent=4)
 
        pdf.multi_cell(epw, 5, paragraph, border=1)
        pdf.ln(0.5)

text= """Lorem ipsum dolor sit amet, vel ne quando dissentias. Ne his opo\
rteat expetendis. Ei tantas explicari quo, sea vidit minimum menandri ea. His ca\
se errem dicam ex, mel eruditi tibique delicatissimi ut. At mea wisi dolorum con\
tentiones, in malis vitae viderer mel.
Vis at dolores ocurreret splendide. Noster dolorum repudiare vis ei, te augue su\
mmo vis. An vim quas torquatos, electram posidonium eam ea, eros blandit ea vel.\
Reque summo assueverit an sit. Sed nibh conceptam cu, pro in graeci ancillae co\
nstituto, eam eu oratio soleat instructior. No deleniti quaerendum vim, assum sa\
epe munere ea vis, te tale tempor sit. An sed debet ocurreret adversarium, ne en\
im docendi mandamus sea.
"""

make_paragraph(paragraph= text, x=1 ,y=190 )

pdf.output('simple_inv.pdf','F')