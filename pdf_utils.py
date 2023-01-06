import PyPDF4 as pdf


class PDFUtils:

    def __init__(self, filename: str):
        self.filename = filename

    def decrypt(self, passwd: str, file_name_out: str = "out_PDFUtils.pdf"):
        file_encrypted = pdf.PdfFileReader(self.filename, strict=False)
        file_out_decrypted = pdf.PdfFileWriter()

        if file_encrypted.isEncrypted:
            file_encrypted.decrypt(passwd)
            
            for index in range(file_encrypted.numPages):
                page = file_encrypted.getPage(index)
                file_out_decrypted.addPage(page)
            
            print(f"Le mot de passe est {passwd}")
        with open(file_name_out, "wb") as f:
            file_out_decrypted.write(f)

    def encrypt(self, pdf_file: str, passwd: str):
        file = pdf.PdfFileReader(pdf_file, strict=False)
        out = pdf.PdfFileWriter()
        num_page = file.numPages
        
        for index in range(num_page):
            page = file.getPage(index)
            out.addPage(page)

        out.encrypt(passwd)
        with open(self.filename, "wb") as f:
            out.write(f)
