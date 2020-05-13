from random import shuffle

class Content(object):
    """This object represents typical Lesson objects content. A Content object 
    itself consists of the words, phrases as well as their translations
    organized as nested lists and designed to help practicing particular language skill.
    """
    def __init__(self, name, path):
        """Initializes self an populates its content
        """
        assert type(name) == str
        assert type(path) == str
        
        self.name = name
        self.path = path

        # vars to held self option
        self.from_lang = ''
        self.to_lang = ''
        self.example = ''
        self.num_ques = 0

        self.data_stru = []
        self.data = []

        # setting content default structure
        self.set_defstru()

        # loading content
        self.set_data(self.get_fpath())

    def set_data(self, fpath, enc="utf-8", fsep="|"):
        """Sets (loads) data as of predefined structure into self
        """     
        with open(fpath, encoding=enc) as cfile:
            for line in cfile:
                self.data.append(line.rstrip("\n").split(fsep))
        
        # Set structure of a current instance
        self.set_curstru()
        
        # Populate basis for statistic
        self.set_num_ques(len(self.data))

    def set_curstru(self):
        """Method which allows user to choose particular content option. 
        In case only one option is available, values populated without 
        asking user for an action
        """
        
        self.example = self.get_stru()[3]               # word or phrase example
        self.to_lang = self.get_stru()[0]               # word in german

        multioption = True

        if self.get_stru()[1] == '':
            self.from_lang = self.get_stru()[2]         # englisch
            print("lesson option is set to: en -> de")            
            multioption = False

        elif self.get_stru()[2] == '':
            self.from_lang = self.get_stru()[1]         # polnisch
            print("lesson option is set to: pl -> de")
            multioption = False

        while multioption:

            try:
                option = int(input("Choose lesson option: (1) pl -> de; (2) en -> de: "))

            except ValueError:
                print('Sorry, must be an integer ')
            
            # not multioption case
            else:
                if option == 1:
                    self.from_lang = self.get_stru()[1]     # polnisch
                    break
                elif option == 2:
                    self.from_lang = self.get_stru()[2]     # englisch
                    break
                else:
                    print('Must be: 1 (pl) or 2 (en)')
                    continue

    def set_defstru(self):
        """Content structure setter. Sets a list used as pandas DataFrame col_names
        """
        # self.data_stru = [self.get_name(), "polnisch", "englisch", "komment"]
        self.data_stru = [0, 1, 2, 3] # "german", "polnisch", "englisch", "komment"

    def get_stru(self):
        """Self data getter. Returns list used as pandas DataFtame col_names
        """
        return self.data_stru

    def get_name(self):
        """Self name getter"""
        return self.name

    def set_num_ques(self, num):
        self.num_ques = num    

    def get_wd(self):
        """Getter of self working dir"""
        return self.path

    def get_fpath(self):
        """Getter of a self path"""
        return str(self.path) + str(self.name) + "_prep_py.txt"

    def get_inst(self, sffl=1):
        """Return self as-is or shuffled
        
        Returns
        -------
        list
        """
        if sffl:
            shuffle(self.data)
        
        return self.data

    def get_option(self):
        """Getter of a self option. One of the defined translation 
        directions used in current lesson. For example: (1) pl, de; (2) en, de. 
        
        Returns
        -------
        tuple
        """
        return (self.from_lang, self.to_lang, self.example)

    def get_translation(self):
        """A placeholder for words/phrases transalations get method.
        Implementation using pons.de API"""
        pass

    def import_cont_from_gglsheet(self):
        """A placeholder to imports content from google sheets"""
        pass

    def __str__(self):
        """Returns a string representation of self"""
        return "This is content located at <" + self.get_fpath() + ">"
