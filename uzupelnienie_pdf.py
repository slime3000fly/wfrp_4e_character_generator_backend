from fillpdf import fillpdfs

class Uzupelnianie_pdf():
    def __init__(self, output_pdf="New_PDF.pdf"):
        """
        Inicjalizuje obiekt klasy uzupelnianie_pdf.

        :param output_pdf: Nazwa pliku PDF, do którego będą wprowadzane zmiany.
                           Domyślnie jest to "New_PDF".
        """
        self.NAZWA_PDF = "WFRP_4ed_final_edytowalna.pdf"
        self.pdf = fillpdfs.get_form_fields(self.NAZWA_PDF)
        self.output_pdf = output_pdf
        self.keys = list(self.pdf.keys())
        self.data_dict = {}

    def tworzenie_pdf(self):
        """
        Tworzy plik PDF na podstawie danych zdefiniowanych w obiekcie.

        Metoda tworzy plik PDF, w którym pola są wypełnione danymi z obiektu uzupelnianie_pdf.
        """
        fillpdfs.write_fillable_pdf(self.NAZWA_PDF, self.output_pdf, self.data_dict)

    def uzupelnienie_pola_tekstowego(self, key_number=None, key_name=None, text="placeHolder"):
        """
        Uzupełnia pole tekstowe w pliku PDF.

        :param key_number: Numer pola tekstowego do uzupełnienia. Jeśli jest podany, to key_name jest ignorowany.
        :param key_name: Nazwa pola tekstowego do uzupełnienia.
        :param text: Tekst, który ma być wstawiony do pola tekstowego. Domyślnie "placeHolder".
        """
        if key_number is not None and 0 <= key_number < len(self.keys):
            tmp_key = self.keys[key_number]
        elif key_name in self.keys:
            tmp_key = key_name
        else:
            raise ValueError("Nieprawidłowy numer pola tekstowego lub nazwa pola.")

        if key_number is not None:
            tmp_key = self.keys[key_number]
        if key_name is not None:
            tmp_key = key_name
        
        self.data_dict = {
            tmp_key: text
        }
