class Puppy:
    n_puppies = 0
    MAX_PUPPIES = 10

    def __new__(cls):
        if cls.n_puppies < cls.MAX_PUPPIES:
            cls.n_puppies += 1
            return object.__new__(cls)
        return None
