

class Item():

    """ Keeps items info """
    def __init__(self, name, description, options, pick=False):
        self.name = name
        self.description = description
        self.options = options
        self.pick = pick

        if self.pick:
            self.options[f"Take {name}."] = {'default':f"You take {name}."}
            self.options[f"Drop {name}."] = {'default':f"You drop {name}."}
