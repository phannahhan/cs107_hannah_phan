class Animal:

    # a class attribute of the valid species in our universe
    valid_species = {
        'cat',
        'dog',
        'duck',
        'elf',
        'goblin',
        'horse',
        'human',
        'mermaid',
        'nightingale',
        'pig',
        'swan',
        'wolf'
    }

    def __init__(self, name, species):
        self.name = name
        self._species = species

    def __repr__(self):
        return f'{self.name} ({self._species})'
    
    @property
    def species(self):
        return self._species
    
    @species.setter
    def species(self, into):
        try:
            assert into in Animal.valid_species, f'invalid species: {into}'
        except Exception as e:
            print(e)           
        self._species = into
#         assert into in Animal.valid_species, Exception(f'invalid species: {into}')
#         self.species = into
        

dog = Animal('Fido', 'dog')
print(dog.species)

dog.species = 'cat'
print(dog.species)

dog.species = 'The Thing'

