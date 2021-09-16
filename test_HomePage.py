import pytest

from pythonSelfFramework.pageObject.Homepage import HomePage
from pythonSelfFramework.utility.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_form(self,getData):
        homepage = HomePage(self.driver)
        homepage.getName().send_keys(getData[0])
        homepage.getEmail().send_keys(getData[1])
        homepage.getCheckBox().click()
        self.OptionSelectLinkText(homepage.getGender(),getData[2])
        homepage.getSelectGender().click()
        homepage.getDate().send_keys("20-12-2012")
        homepage.getSubmit().click()
        massage = homepage.getSuccess().text
        print(homepage.getSuccess().text)
        assert "Success!" in massage
        self.driver.refresh()

    @pytest.fixture(params = [("shivaraja","gangalli","Male"),("Ashwini","Gangalli","Female")])
    def getData(self,request):
        return request.param



























