class Animal:

    warm_blooded = "unknown"

    average_lifetime_in_years = 5


    def __init__(self, name):
        self.name = name

    def get_number_remaining_years(self, years_so_far):
        return self.average_lifetime_in_years - years_so_far


class Mammal(Animal):

    warm_blooded = "most_definitely"
    average_lifetime_in_years = 20



def main():
    print "begin amimals "

    fido = Animal("weird fido")
    print fido.name
    print fido.warm_blooded
    print fido.get_number_remaining_years(2)

    print

    fido = Mammal("regular fido")
    print fido.name
    print fido.warm_blooded
    print fido.get_number_remaining_years(2)

if __name__ == '__main__':
  main()