############
# Part 1   #
############

class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""

        self.pairings = []

        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType("musk", 1998, "green", True, True, "Muskmelon")
    musk.add_pairing("mint")
    all_melon_types.append(musk)

    casaba = MelonType("cas", 2003, "orange", False, False, "Casaba")
    casaba.add_pairing("strawberries")
    casaba.add_pairing("mint")
    all_melon_types.append(casaba)

    cren = MelonType("cren", 1996, "green", False, False, "Crenshaw")
    cren.add_pairing("prosciutto")
    all_melon_types.append(cren)
    
    yel_wat = MelonType("yw", 2013, "yellow", False, True, "Yellow Watermelon")
    yel_wat.add_pairing("ice cream")
    all_melon_types.append(yel_wat)


    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f"{melon.name} pairs with: ")
        for pairing in melon.pairings:
            print(f"- {pairing}")
    
# print_pairing_info(all_melon_types)


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_dict = {}

    for melon in melon_types:
        melon_dict[melon.code] = melon

    return melon_dict


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

    def __init__(self, melon_type, shape_rating, color_rating, field, harvester):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvester = harvester

    def is_sellable(self):
        if self.shape_rating > 5 and self.color_rating > 5 and self.field != 3:
            return True
        else:
            return False

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    all_melon_types = []

    melons_by_id = make_melon_type_lookup(melon_types)

    melon_1 = Melon(melons_by_id["yw"], 8, 7, 2, "Sheila")
    all_melon_types.append(melon_1)

    melon_2 = Melon(melons_by_id["yw"], 3, 4, 2, "Sheila")
    all_melon_types.append(melon_2)

    melon_3 = Melon(melons_by_id["yw"], 9, 8, 3, "Sheila")
    all_melon_types.append(melon_3)

    melon_4 = Melon(melons_by_id["cas"], 10, 6, 35, "Sheila")
    all_melon_types.append(melon_4)

    melon_5 = Melon(melons_by_id["cren"], 8, 9, 35, "Michael")
    all_melon_types.append(melon_5)

    melon_6 = Melon(melons_by_id["cren"], 8, 2, 35, "Michael")
    all_melon_types.append(melon_6)

    melon_7 = Melon(melons_by_id["cren"], 2, 3, 4, "Michael")
    all_melon_types.append(melon_7)

    melon_8 = Melon(melons_by_id["musk"], 6, 7, 4, "Michael")
    all_melon_types.append(melon_8)

    melon_9 = Melon(melons_by_id["yw"], 7, 10, 3, "Sheila")
    all_melon_types.append(melon_9)

    return all_melon_types


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        sell_status = melon.is_sellable()
        harvested = melon.harvester
        field_num = melon.field
        if sell_status == True:
            print(f"{melon.melon_type.name} harvested by {harvested} in field #{field_num} is able to be sold.")
        else:
            print(f"{melon.melon_type.name} harvested by {harvested} in field #{field_num} is not sellable.")

def get_melon_data(filename):
    
    the_file = open(filename)

    all_melon_data = []

    for line in the_file:
        melon_data = line.strip().split(" ")
        all_melon_data.append(melon_data)
    
    return all_melon_data

def make_melons_from_file(melon_data):

    all_melons = []


    melons_by_id = make_melon_type_lookup(make_melon_types())

    for sublst in melon_data:
        #"shape" at 1, "color" at 3, "type" at 5, "harvester" at 8, "field" at 11
        melon = Melon(melon_type = melons_by_id[sublst[5]], shape_rating = int(sublst[1]), color_rating = int(sublst[3]), field = sublst[11], harvester = sublst[8])
        all_melons.append(melon)

    return all_melons