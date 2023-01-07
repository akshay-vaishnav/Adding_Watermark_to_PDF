import PyPDF2 #use pip install PyPDF2

template = PyPDF2.PdfReader(open('twopage.pdf','rb')) 
watermark = PyPDF2.PdfReader(open('wtr.pdf','rb')) 
output = PyPDF2.PdfWriter()

for i in range(len(template.pages)):
	page = template.pages[i]
	page.merge_page(watermark.pages[0])
	output.add_page(page)


with open('watermarked_page.pdf','wb') as file:
    output.write(file)

