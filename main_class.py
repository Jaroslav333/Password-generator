import random

class BrainPassGenerator:

    def __init__(self, data_list):
        self.data = data_list

        self.type_letter = ""
        self.type_number = ""
        self.type_special_char = ""
        self.final_list = ""
        self.final_string = ""

    def counter_type(self, num_let, num_num, num_char):
        self.type_letter = random.sample(self.data[0], num_let)
        self.type_number = random.sample(self.data[1], num_num)
        self.type_special_char = random.sample(self.data[2], num_char)
        self.final_list = self.type_letter + self.type_number + self.type_special_char
        random.shuffle(self.final_list)

        for one_symbol in self.final_list:
            self.final_string += one_symbol
        return self.final_string
