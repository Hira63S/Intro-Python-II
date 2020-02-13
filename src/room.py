# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    """ Holds room information """
    def __init__(self, title, description, multi_items=[]):#n_to, s_to, e_to, w_to, visible_items=[]):

        self.title = title
        self.description = description
        self.n_to = None # n_to
        self.s_to = None # s_to
        self.e_to = None #e_to
        self.w_to = None # w_to
        self.multi_items = multi_items #
    def __str__(self):
        """ This is a string method """
        return f"{self.title}\n\n{self.description}"
