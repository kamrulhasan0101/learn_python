import pyttsx3
import PyPDF4
book = open('dcl-report.pdf','rb')
pdfReader = PyPDF4.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
page = pdfReader.getPage(0)
speech = page.extractText()
# text = "sound works"
kamrul = pyttsx3.init()
kamrul.say(speech)
kamrul.runAndWait()