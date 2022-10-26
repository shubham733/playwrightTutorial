
class HomePage:

    def __init__(self, page):
        self.left_header = page.locator("#react-home-dashboard >> text=Items Need My Action")
        self.right_header = page.locator("#react-home-dashboard >> text=Most Frequently Viewed")
        self.quick_add_button = page.locator("[data-testid=\"quick_add\"] svg")