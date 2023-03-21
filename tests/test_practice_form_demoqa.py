
import os

from selene.support.conditions import be, have
from selene.support.shared import browser


def test_filling_out_registration_forms_for_the_demoqa():
    # GIVEN
    browser.open("/automation-practice-form")
    # WHEN
    browser.element("#firstName").should(be.blank).type("Ivan")
    browser.element("#lastName").should(be.blank).type("Ivanov")
    browser.element("#userEmail").should(be.blank).type("test_email@test.com")
    browser.element("[for=gender-radio-1]").click()
    browser.element("#userNumber").should(be.blank).type("9990000001")
    browser.element('#dateOfBirthInput').should(be.not_.blank).click()
    browser.element(".react-datepicker__year-select").type("1977")
    browser.element(".react-datepicker__month-select").type("Juli")
    browser.element("[aria-label*='July 7th, 1977']").click()

    browser.element("#subjectsInput").should(be.blank).click().\
        type("Physics").press_enter().\
        type("Computer Science").press_enter()
    browser.element("[for=hobbies-checkbox-3]").click()
    browser.element("#uploadPicture").send_keys(os.path.abspath(os.path.dirname(__file__) + r"\image\img.png"))
    browser.element("#currentAddress").should(be.blank).type("Spain")
    browser.element("#state").click().element("#react-select-3-option-2").click()
    browser.element("#city").click().element("#react-select-4-option-0").click()
    browser.element("#submit").press_enter()
    # THEN
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.all('.table-responsive td:nth-child(2)').should(have.texts(
        'Ivan Ivanov',
        'test_email@test.com',
        'Male',
        '9990000001',
        '07 July,1977',
        'Physics, Computer Science',
        'Music',
        'img.png',
        'Spain',
        'Haryana Karnal'
    )
    )

