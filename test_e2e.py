from pythonSelfFramework.pageObject.Homepage import HomePage
from pythonSelfFramework.utility.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.test_logging()
        homepage= HomePage(self.driver)
        checkoutpage = homepage.shopitem()

        products = checkoutpage.getCard()
        for product in products:

            productName = product.find_element_by_xpath("div/h4/a").text

            if productName == "Nokia Edge":
                product.find_element_by_xpath("div/button").click()

        checkoutpage.getlink()
        checkoutpage.getSuccess()
        checkoutpage.getcountrykey()


        #timesleep
        self.verifyLink("India")

        checkoutpage.getcountry()
        checkoutpage.getcheckbox()

        assert "Success!" in self.driver.find_element_by_class_name("alert-success").text, "test_fail"








