from reportlab.pdfgen import canvas
from reportlab.pdfbase.pdfmetrics import getRegisteredFontNames,registerFont
from pypdf import PdfMerger, PdfReader, PdfWriter
from io import BytesIO
from reportlab.lib.units import inch
from reportlab.pdfbase.ttfonts import TTFont
 

def add_watermark(input_pdf_path, output_pdf_path, watermark_text):
    # 创建一个新的PDF文件来作为水印
    watermark_pdf = BytesIO()
    c = canvas.Canvas(watermark_pdf,pagesize=(1920,1080))
    c.rotate(-45) 
    c.setFont('微软雅黑',16)
    c.setFillColorRGB(0.5,0.5,0.5,alpha=0.3)
    for i in range(-5,10,2):
        for j in range(-5,20,1):
            c.drawString(i*inch ,j*inch, watermark_text)
     # 在PDF的指定位置添加水印文本
    c.save()
    
    watermark_pdf.seek(0)

    # 读取原始PDF文件和水印PDF文件
    input_pdf = PdfReader(input_pdf_path)
    watermark_pdf = PdfReader(watermark_pdf)

    # 创建一个新的PDF文件来合并原始PDF和水印PDF
    output_pdf = PdfWriter()

    # 遍历原始PDF的每一页，并添加水印
    for page_num in range(input_pdf.get_num_pages()):
        page = input_pdf.get_page(page_num)
        page.merge_page(watermark_pdf.get_page(0))  # 将水印PDF的第一页（即水印）合并到原始PDF的每一页上
        output_pdf.add_page(page)

    # 将合并后的PDF写入到输出文件
    with open(output_pdf_path, 'wb') as output_file:
        output_pdf.write(output_file)
if __name__ == "__main__":
    # 使用示例
    registerFont(TTFont('微软雅黑', './MSYH.TTC'))
    # print(getRegisteredFontNames())
    import sys
    path = sys.argv[1]
    target = path.replace(".pdf","_marked.pdf")
    add_watermark(path, target, '仅供办理业务使用')
