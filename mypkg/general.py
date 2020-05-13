from mypkg import internal

class Lesson(object):
    """Represents a Lesson object and methods associated with it
    
       Returns
       -------
       Lesson object
    """
    def __init__(self, name, path):
        """Creates self of a given name and loads it's content assosiated
        """
        assert type(name) == str
        assert type(path) == str

        self.name = name
        self.path = path

        self.num_ques = 0        
        self.attempts = 2
        self.repeat_list = []
        
        # Populate lesson content based on lesson name 
        self.cont = internal.Content(self.get_name(), self.get_path())

    def start(self):
        """
        """
        print("Welcome to", self.get_name(), "lesson!")
        print("You will have 2 attempt for each word. To stop at any time type 'stop()'. Good luck!")
        print("")

        return (self.get_cont(), self.get_cont_option())
        
    def get_cont(self):
        """Returns content of self instance. 
        
        Returns
        -----
        list
        """
        return self.cont.get_inst()
    
    def get_cont_option(self):
        """Return self content option. 
        
        Returns
        -----
        tuple
        """
        return self.cont.get_option()

    def get_name(self):
        """Getter method for lesson name attribute
        """
        return self.name

    def get_path(self):
        """Self path getter
        """
        return self.path

    def get_attempts(self):
        """Getter method for number of attempts available
        """
        return self.attempts

    def get_num_ques(self):
        """Getten for number of questions in lesson
        """
        return self.cont.num_ques

    def get_repeat_list(self):
        """Getter for repeat list
        """
        return self.repeat_list

    def add_2_repeat_list(self, item):
        """Method to add word or phrase to repeat list
        """
        if item not in self.repeat_list:
            self.repeat_list.append(item)

    def end(self, interrupt=0):
        """Method to finish the lesson properly
        """
        if not interrupt:
            print("Good job!")
        else:
            print("Hope to see you soon!")

    def stats(self):
        """Method to display stats collected during lesson practice
        """
        print("Stats:")
        print("Number of questions:", self.get_num_ques())
        print("Words to repeat:", self.get_repeat_list())

    def __str__(self):
        """Returns a string representation of self
        """
        return "This is the "+ self.get_name() + " lesson!"
