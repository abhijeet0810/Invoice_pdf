from fpdf import FPDF
import json

pdf = FPDF()
pdf.add_page()

pdf.set_font('Arial', size= 12)
ratio=1262./297

def make_table(data):
    
    epw = pdf.w - 2*pdf.l_margin

    col_widths = epw/4

    th = pdf.font_size
    
#     list_of_values = ['ratio*pdf.get_x()', 'ratio*pdf.get_y()', 'pdf.w', 'pdf.h', 'item']
    table_dict = {}
    for row in data:
        for item in row:
                table_dict['table'] = []
                table_dict['table'].append({
                        'x': ratio*pdf.get_x(),
                        'y': ratio*pdf.get_y(),
                        'w': pdf.w,
                        'h': pdf.h,
                        'text': item
                })

                with open('data.json', 'w') as outfile:
                        json.dump(table_dict, outfile, indent=4)
            
                pdf.cell(col_widths, th, str(item), border=1)
        
        pdf.ln(th)
        


data = [['Abv', 45, 23, 52.00],
        ['Dfc', 55, 21, 99.23],
        ['Ina', 15, 26, 87.89],
        ['FGa', 75, 86, 8.9],
        ['Kjut', 95, 416, 12.9]
        ]

make_table(data=data)

def make_paragraph(paragraph):

        epw = pdf.w - 2*pdf.l_margin

        pdf.multi_cell(epw, 0.15, paragraph, border=1)
        pdf.ln(0.5)

dummy_text= """Lorem ipsum dolor sit amet, vel ne quando dissentias. Ne his opo\
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

# make_paragraph(paragraph= dummy_text)

pdf.output('simple_inv.pdf','F')


