
class VendorPage:

    def __init__(self, page):
        self.page = page

    def create_new_vendor(self, vendor_name, contact_name, contact_email, contact_phone, url):
        self.page.fill('input:right-of(:text("Vendor Name"))', vendor_name)
        self.page.fill('input:right-of(:text("Contact Name"))', contact_name)
        self.page.fill('input:right-of(:text("Contact Email*"))', contact_email)
        self.page.fill('input:right-of(:text("Contact Phone"))', contact_phone)
        self.page.fill('input:right-of(:text("URL"))', url)

