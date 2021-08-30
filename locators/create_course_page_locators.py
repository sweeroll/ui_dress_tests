from selenium.webdriver.common.by import By


class CoursePageLocators:
    FULL_COURSE_NAME = (By.ID, "id_fullname")
    SHORT_COURSE_NAME = (By.ID, "id_shortname")
    END_DAY = (By.ID, "id_enddate_day")
    END_MONTH = (By.ID, "id_enddate_month")
    END_YEAR = (By.ID, "id_enddate_year")
    END_HOUR = (By.ID, "id_enddate_hour")
    END_MINUTE = (By.ID, "id_enddate_minute")
    COURSE_DESCRIPTION = (By.ID, "id_summary_editoreditable")
    SECTION_NUMBER = (By.ID, "id_numsections")
    COURSE_LANGUAGE = (By.ID, "id_lang")
    MAX_FILE_SIZE = (By.ID, "id_maxbytes")
    MANAGER_NAME = (By.ID, "id_role_1")
    TEACHER_NAME = (By.ID, "id_role_3")
    STUDENT_NAME = (By.ID, "id_role_5")
    SAVE_AND_SHOW_BUTTON = (By.ID, "id_saveanddisplay")