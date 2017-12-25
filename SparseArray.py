class SparseArray:
    def __init__(self):
        self.all_strings = dict()
        self.results = list()
        self.inputs()
        self.queries()
        self.print_results(self.results)

    def inputs(self):
        num_strings = int(input())

        for counter in range(num_strings):
            input_str = input()

            if input_str in self.all_strings:
                self.all_strings[input_str] += 1
            else:
                self.all_strings[input_str] = 1

    def search(self, element):
        if element in self.all_strings:
            return str(self.all_strings[element])
        else:
            return '0'

    def queries(self):
        total_queries = int(input())

        for query in range(total_queries):
            test = input()
            self.results.append(self.search(test))

    def print_results(self, results):
        for element in results:
            print(element)

sp = SparseArray()
