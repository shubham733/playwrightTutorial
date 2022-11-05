
class HomePage:

    def __init__(self, page):
        self.left_header = page.locator("#react-home-dashboard >> text=Items Need My Action")
        # self.left_header2 = page2.locator("#react-home-dashboard >> text=Items Need My Action")
        self.right_header = page.locator("#react-home-dashboard >> text=Most Frequently Viewed")
        # self.right_header2 = page2.locator("#react-home-dashboard >> text=Most Frequently Viewed")
        self.quick_add_button = page.locator("[data-testid=\"quick_add\"] svg")
        # self.quick_add_button2 = page2.locator("[data-testid=\"quick_add\"] svg")