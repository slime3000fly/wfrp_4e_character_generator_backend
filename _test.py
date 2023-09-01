import unittest
from fillpdf import fillpdfs
import os
from uzupelnienie_pdf import uzupelnianie_pdf

class TestUzupelnianiePdf(unittest.TestCase):

    def setUp(self):
        self.NAZWA_PDF = "WFRP_4ed_final_edytowalna.pdf"
        self.output_pdf = "test_output.pdf"
        self.pdf = fillpdfs.get_form_fields(self.NAZWA_PDF)
        self.keys = list(self.pdf.keys())
        self.data_dict = {}
        self.pdf_uzupelnianie = uzupelnianie_pdf(self.output_pdf)

    def test_tworzenie_pdf(self):
        self.pdf_uzupelnianie.tworzenie_pdf()
        # Sprawdź, czy plik PDF został utworzony
        self.assertTrue(os.path.exists(self.output_pdf))
        os.remove(self.output_pdf)

    def test_uzupelnienie_pola_tekstowego(self):
        key_name = 'Rasa'
        field_value = 'WartośćPolaTekstowego'
        self.pdf_uzupelnianie.uzupelnienie_pola_tekstowego(key_name=key_name,text=field_value)
        self.pdf_uzupelnianie.tworzenie_pdf()

        # pobieranie slownika pol z pdf
        d = fillpdfs.get_form_fields(self.output_pdf)

        # Sprawdź, czy pole tekstowe zostało wypełnione poprawną wartością
        self.assertEqual(d[key_name],field_value)
        os.remove(self.output_pdf)

