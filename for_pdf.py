from fpdf import FPDF

pdf = FPDF(unit='in')
pdf.add_page()

pdf.set_font('Arial', size= 12)

def make_table(data):
    
    epw = pdf.w - 2*pdf.l_margin

    col_widths = epw/4

    th = pdf.font_size
    for row in data:
        for datum in row:
            pdf.cell(col_widths, th, str(datum), border=1)
        
        pdf.ln(th)


data = [['Abv', 45, 23, 52.00],
        ['Dfc', 55, 21, 99.23],
        ['Ina', 15, 26, 87.89],
        ['FGa', 75, 86, 8.9],
        ['Kjut', 95, 416, 12.9]
        ]

make_table(data=data)

pdf.output('simple_inv.pdf','F')


