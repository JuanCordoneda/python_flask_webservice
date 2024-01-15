class NumberController:
    def __init__(self):
        self.collection = {}

    def add_number(self, number):
        if number % 3 == 0 and number % 5 == 0:
            self.collection[number] = 'Type 3'
        elif number % 3 == 0:
            self.collection[number] = 'Type 1'
        elif number % 5 == 0:
            self.collection[number] = 'Type 2'
        else:
            self.collection[number] = number

    def get_number(self, number):
        if number in self.collection:
            return self.collection[number]
        else:
            return None

    def get_all_numbers(self):
        return self.collection

    def update_number(self, number, updated_number):
        if number in self.collection:
            if updated_number % 3 == 0 and updated_number % 5 == 0:
                self.collection[number] = 'Type 3'
            elif updated_number % 3 == 0:
                self.collection[number] = 'Type 1'
            elif updated_number % 5 == 0:
                self.collection[number] = 'Type 2'
            else:
                self.collection[number] = updated_number
            return True
        else:
            return False
