class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        return self.count

    def __next__(self):
        item = next(self.iterator)  # Raises StopIteration naturally when exhausted
        self.count += 1
        return item

    def __iter__(self):
        return self


# Testing
data = [10, 20, 30, 40, 50]
ci = CountedIterator(data)

# Manual calls to __next__
print(next(ci))           # 10
print(next(ci))           # 20
print(f"Count so far: {ci.get_count()}")  # Count so far: 2

# Loop through the rest
for item in ci:
    print(item)           # 30, 40, 50

print(f"Total fetched: {ci.get_count()}")  # Total fetched: 5
