"""
Hydra project application

Using Beeware, this app produces a simple Gui that allows users to enter in a series of search terms for the NHS Hydra pfam
portal and returns a set of transcripts for each one that are saved to an excel spreadsheet. 
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import hydra_fetch


class hydra(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

        term_label = toga.Label(
            'Enter search term(s): ',
            style=Pack(padding=(0, 5))
        )
        self.term_input = toga.TextInput(style=Pack(flex=1))

        term_box = toga.Box(style=Pack(direction=ROW, padding=5))
        term_box.add(term_label)
        term_box.add(self.term_input)

        button = toga.Button(
            'Done',
            on_press=self.hydra_fetch,
            style=Pack(padding=5)
        )

        main_box.add(term_box)
        main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    terms =[]
    def hydra_fetch(self, widget):
        term = self.term_input.value
        if (' ' not in term and len(term) != 0):
            terms.append(term)
        else:
            self.main_window.info_dialog(
            'Please enter a term or press \'Done\' to finish adding terms.'
            )

        self.main_window.info_dialog(
            'Finished adding terms',
            "Term(s): {}".format(term)
        )

        return terms 


def main():
    return HelloWorld()
