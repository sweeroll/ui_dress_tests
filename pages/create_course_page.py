from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from locators.create_course_page_locators import CoursePageLocators


class CreateCoursePage(BasePage):
    def general_data(self) -> WebElement:
        return self.find_element(CoursePageLocators.GENERAL_DATA)

    def full_course_name_input(self) -> WebElement:
        return self.find_element(CoursePageLocators.FULL_COURSE_NAME)

    def short_course_name_input(self) -> WebElement:
        return self.find_element(CoursePageLocators.SHORT_COURSE_NAME)

    def end_day_select(self) -> WebElement:
        return self.find_select_element(CoursePageLocators.END_DAY)

    def end_month_select(self) -> WebElement:
        return self.find_select_element(CoursePageLocators.END_MONTH)

    def end_year_select(self) -> WebElement:
        return self.find_select_element(CoursePageLocators.END_YEAR)

    def end_hour_select(self) -> WebElement:
        return self.find_select_element(CoursePageLocators.END_HOUR)

    def end_minute_select(self) -> WebElement:
        return self.find_select_element(CoursePageLocators.END_MINUTE)

    def course_description_input(self) -> WebElement:
        return self.find_element(CoursePageLocators.COURSE_DESCRIPTION)

    def section_number_select(self) -> WebElement:
        return self.find_select_element(CoursePageLocators.SECTION_NUMBER)

    def course_language_select(self) -> WebElement:
        return self.find_select_element(CoursePageLocators.COURSE_LANGUAGE)

    def max_file_size_select(self) -> WebElement:
        return self.find_select_element(CoursePageLocators.MAX_FILE_SIZE)

    def manager_name_input(self) -> WebElement:
        return self.find_element(CoursePageLocators.MANAGER_NAME)

    def teacher_name_input(self) -> WebElement:
        return self.find_element(CoursePageLocators.TEACHER_NAME)

    def student_name_input(self) -> WebElement:
        return self.find_element(CoursePageLocators.STUDENT_NAME)

    def save_and_show_button(self):
        return self.find_element(CoursePageLocators.SAVE_AND_SHOW_BUTTON)

    def input_full_course_name(self, name):
        self.fill_element(self.full_course_name_input(), name)

    def input_short_course_name(self, name):
        self.fill_element(self.short_course_name_input(), name)

    def select_end_day(self, value):
        self.select_value(self.end_day_select(), value)

    def select_end_month(self, value):
        self.select_value(self.end_month_select(), value)

    def select_end_year(self, value):
        self.select_value(self.end_year_select(), value)

    def select_end_hour(self, value):
        self.select_value(self.end_hour_select(), value)

    def select_end_minute(self, value):
        self.select_value(self.end_minute_select(), value)

    def input_course_description(self, text):
        self.fill_element(self.course_description_input(), text)

    def select_section_number(self, value):
        self.select_value(self.section_number_select(), value)

    def select_course_language(self, value):
        self.select_value(self.course_language_select(), value)

    def select_max_file_size(self, value):
        self.select_value(self.max_file_size_select(), value)

    def input_manager_name(self, name):
        self.fill_element(self.manager_name_input(), name)

    def input_teacher_name(self, name):
        self.fill_element(self.teacher_name_input(), name)

    def input_student_name(self, name):
        self.fill_element(self.student_name_input(), name)

    def submit_changes(self):
        self.click_element(self.save_and_show_button())

    def create_course(self, data):
        self.full_course_name = data.full_course_name
        self.short_course_name = data.short_course_name
        self.end_month = data.end_month
        self.end_year = data.end_year
        self.end_day = data.end_day
        self.end_hour = data.end_hour
        self.end_minute = data.end_minute
        self.course_description = data.course_description
        self.section_number = data.section_number
        self.course_language = data.course_language
        self.max_file_size = data.max_file_size
        self.manager_name = data.manager_name
        self.teacher_name = data.teacher_name
        self.student_name = data.student_name
