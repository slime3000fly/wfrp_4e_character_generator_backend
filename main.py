from fillpdf import fillpdfs


class uzpelnianie_pdf():
    def __init__(self,output_pdf="New_PDF"):
        self.NAZWA_PDF = "WFRP_4ed_final_edytowalna.pdf"
        self.pdf = fillpdfs.get_form_fields(self.NAZWA_PDF)
        self.output_pdf = output_pdf
        self.keys = list(self.pdf.keys())
        self.data_dict = {}

    def tworzenie_pdf(self):
        fillpdfs.write_fillable_pdf(self.NAZWA_PDF, self.output_pdf, self.data_dict)
        
    def uzupelnienie_pola_tekstowego (self,key_number = None, key_name = None, text = "placeHolder"):
        if key_number != None:
            tmp_key = self.keys[key_number]
        if key_name != None:
            tmp_key = key_name
        
        self.data_dict={
        tmp_key:text
        }

# d = uzpelnianie_pdf("nic.pdf")
# d.uzupelnienie_pola_tekstowego(1)
# d.tworzenie_pdf()