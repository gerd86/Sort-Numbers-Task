class Sort:
    def __init__(self, number_list):
        self.number_list = number_list

    def str_to_list(self):
        lst = self.number_list.split()
        return lst

    # Sort ascending

    def sort_number_ascending(self):
        return sorted(self.str_to_list(), key=lambda k: int(k))

    # Sort descending

    def sort_number_descending(self):
        return sorted(self.str_to_list(), key=lambda k: int(k), reverse=True)


