#Pages 238 to 247

#Importing PyPDF2
import PyPDF2 as PDF

#Importing_Source_PDF_File
Input=open("Walter_Nicholson,_Christopher_M_Snyder_IntermedBookFi_org.pdf", "rb")

#PdfFileReader
Reader=PDF.PdfFileReader(Input)

#PDFFileWriter
Writer=PDF.PdfFileWriter()

#Getting_Pages 228-237_For_PDFExtract_File
Range=[271,272,273,274,275,276,277,278,279,280]
for Page_Range in Range:
    Pages = Reader.getPage(Page_Range)
    Writer.addPage(Pages)

#Specifying_PDF_Extract_File
Output=open("Robert_Owusu_pg.238-247).pdf",'wb')

#Writing_Pages 238-237_intoPDF_Extract_File
Writer.write(Output)

#Closing_Source_PDF_File
Input.close()

#Closing_PDF_Extract_File
Output.close()

