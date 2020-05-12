"""Dessert classes."""


class Cupcake:
    """A cupcake."""

    def __repr__(self):
        """Human-readable printout for debugging."""

        return f'<Cupcake name="{self.name}" qty={self.qty}>'
    
    def __init__(self, name, flavor, price, qty=0):
            """Names a cupcake with flavor, price and qty attributes."""
            self.name = name
            self.flavor = flavor
            self.price = price
            self.qty = qty

    def add_stock(self, amount):
        """Adds existing stock amount to qty of cupcakes."""
        stock = amount + self.qty
        self.qty = stock 

    def sell(self, amount):
        """Sells a number of cupcakes."""
        if amount <= self.qty:
            stock = self.qty - amount
            self.qty = stock
        else:
            print("Sorry, these cupcakes are sold out")  

    @staticmethod
    def scale_recipe(ingredients, amount):
        """Scale the list of ingredients by the given amount of cupcakes."""  
        new_ingredients = []

        for ingredient in (ingredients):
            
            scaled_ingredient = ingredient[0]
            scaled_value = ingredient[1] * amount
            
            new = (scaled_ingredient, scaled_value)
            new_ingredients.append(new)
        
        return new_ingredients
            

           















if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')


    