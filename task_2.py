class UserData:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f"User: {self.name}, Age: {self.age}")


def process_data(data_list):
    result = []
    for data in data_list:
        if data.age > 18:
            result.append(data.name.upper())
    return result