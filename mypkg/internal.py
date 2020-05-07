
from pandas import DataFrame
from pandas import read_csv
from numpy import nan


class Content(object):
    """Object represent lesson content. Lesson content can consist of
    words, phrases, as well as their translations,
    organized in a way to help practice particular language skill.
    """
    def __init__(self, name, path):
        """Initializes self an populates its content
        """
        assert type(name) == str
        assert type(path) == str
        
        self.name = name
        self.path = path

        # vars to held self option
        self.fromLang = ''
        self.toLang = ''
        self.example = ''
        self.num_ques = 0

        self.data_stru = []           # DataFrame col_names
        self.data = DataFrame()

        # setting Content
        self.load()

    def load(self):
        """Loads self with content, i.e. structure and data
        """      
        # Set content data
        self.set_stru()

        # Load data (content)
        data = read_csv(self.get_full_path(),
                         names     = self.get_stru(),
                         delimiter = "|",
                         header    = None,
                         encoding  = "utf-8")

        # Replace NaN with empty strings, which are easy to handle
        self.data = data.replace(nan, '', regex=True)

        # Populate option
        self.set_option()
        
        # Populate basics for stats
        self.set_num_ques(len(self.data.index))

    def set_num_ques(self, num):
        self.num_ques = num    

    def get_stru(self):
        """Self data getter. Returns list used as pandas DataFtame col_names
        """
        return self.data_stru

    def get_name(self):
        """Self name getter"""
        return self.name

    def set_stru(self):
        """Content structure setter. Sets a list used as pandas DataFrame col_names
        """
        self.data_stru = [self.get_name(), "polnisch", "englisch", "komment"]

    def set_option(self):
        """Method which allows user to choose particular content option. 
        In case only one option is available, values populated without 
        asking user for an action
        """
        
        self.example = self.get_stru()[3]       # word or phrase example
        self.toLang  = self.get_stru()[0]       # word in german

        multioption = True

        if self.get_stru()[1] == '':
            self.fromLang = self.get_stru()[2] # englisch
            multioption = False
            print("lesson option is set to: en -> de")

        elif self.get_stru()[2] == '':
            multioption   = False
            self.fromLang = self.get_stru()[1] # polnisch
            print("lesson option is set to: pl -> de")

        while multioption:

            try:
                option = int(input("Choose lesson option: (1) pl -> de; (2) en -> de: "))

            except ValueError:
                print('Sorry, must be an integer ')

            else:
                if option == 1:
                    self.fromLang = self.get_stru()[1] # polnisch
                    break
                elif option == 2:
                    self.fromLang = self.get_stru()[2] # englisch
                    break
                else:
                    print('Must be: 1 (pl) or 2 (en)')
                    continue

    #def get_struPath(self):
    #    """Getter of self structure path"""
    #    return self.path + self.name + "_sche_py.txt"

    def get_wd(self):
        """Getter of self working dir"""
        return self.path

    def get_full_path(self):
        """Getter of a self path"""
        return str(self.path) + str(self.name) + "_prep_py.txt"

    def get_inst(self, orig=0):
        """Getter of a self. Returns pandas DataFrame"""
        if orig:
            return self.data
        else:
            return self.data.sample(frac=1)

    def get_option(self):
        """Getter of a content option. Returns option as a tuple:
        (1) pl, de; (2) en, de"""
        return (self.fromLang, self.toLang, self.example)

    def get_translation(self):
        """Method to get transalation for words (phrases) from content
        implemented using pons.de API"""
        pass

    def import_cont_from_gglsheet(self):
        """Imports content of predefined structure (get_cont_struct()) from google sheet"""
        pass

    def __str__(self):
        """Returns a string representation of self"""
        return "This is content located at <" + self.get_full_path() + ">"
