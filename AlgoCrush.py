#!/bin/python3

class AlgoCrush:
    def __init__(self):
        self.results = dict()
        self.collect_inputs()

    def collect_inputs(self):
        n, m = input().strip().split(' ')
        n, m = [int(n), int(m)]

        for a0 in range(m):
            a, b, k = input().strip().split(' ')
            a, b, k = [int(a), int(b), int(k)]
            self.perform_ops(a, b, k)

    def perform_ops(self, start_index, end_index, element):
        # Keep only the non-zero indexes as key and values
        for current_index in range(start_index, end_index):
            value = self.results.get(current_index, default = 0)
            self.results[current_index] += value + element

    @property
    def report_max(self):
        return max(self.results.values())

test = AlgoCrush()
print(test.report_max)
