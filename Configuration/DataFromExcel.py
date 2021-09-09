import openpyxl


def readData_fromExcel(sheetname, rownum, colnum):
    file = "C:\\Users\\SatishKumar\\PycharmProjects\\OrangeHRM\\DataFile\\TestData.xlsx"
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheetname]
    inputvalue = sheet.cell(row=rownum, column=colnum).value
    return inputvalue


class TestData:
    URL = readData_fromExcel("MyInfo", 1, 2)
    USERNAME = readData_fromExcel("MyInfo", 2,2)
    PASSWORD = readData_fromExcel("MyInfo", 3,2)

    """MyInfo page data"""
    FIRST_NAME = readData_fromExcel("MyInfo",8, 1)
    MIDDLE_NAME = readData_fromExcel("MyInfo",8, 2)
    LAST_NAME = readData_fromExcel("MyInfo",8, 3)
    EMPLOYEE_ID = readData_fromExcel("MyInfo", 8, 4)
    OTHERS_ID = readData_fromExcel("MyInfo", 8, 5)
    DRIVER_LICENSE_NUMBER = readData_fromExcel("MyInfo", 8, 6)
    SSN_NUMBER = readData_fromExcel("MyInfo", 8, 7)
    SIN_NUMBER = readData_fromExcel("MyInfo", 8, 7)
    GENDER = readData_fromExcel("MyInfo", 8, 8)
    MARTIAL_STATUS = readData_fromExcel("MyInfo", 8, 9)
    NATIONALITY = readData_fromExcel("MyInfo", 8, 10)
    MILITARY_SERVICE = readData_fromExcel("MyInfo", 8, 17)
    SMOKER = readData_fromExcel("MyInfo", 8, 18)

    """Buzz Data"""
    UPDATE_STATUS = readData_fromExcel("Buzz", 1, 2)
