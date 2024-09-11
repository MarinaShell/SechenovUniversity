class ExcelReader:
    ############################################################################
    #Инициализация класса ExcelReader с указанием пути к файлу.
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = {}

    ############################################################################
    #Загрузка всех листов из Excel файла.
    def loadAllSheets(self):
        try:
            self.data = pd.read_excel(self.file_path, sheet_name=None)  # Загружаем все листы
            print(f"Все листы из файла '{self.file_path}' успешно загружены.")
            return self.data
        except FileNotFoundError:
            print(f"Файл '{self.file_path}' не найден.")
        except Exception as e:
            print(f"Ошибка при загрузке файла: {e}")

    ############################################################################
    #Загрузка данных из Excel файла. Если не указан лист, загружается первый лист.
    def loadSheet(self, sheet_name=None):
        try:
            self.data = pd.read_excel(self.file_path, sheet_name=sheet_name)
            print(f"Лист{sheet_name} файла'{self.file_path}' успешно загружен.")
            return self.data
        except FileNotFoundError:
            print(f"Файл '{self.file_path}' не найден.")
        except Exception as e:
            print(f"Ошибка при загрузке файла: {e}")

    ############################################################################
    #Получение имен всех листов в Excel файле.
    def getSheetNames(self):
        if self.data:
            return list(self.data.keys())
        else:
            print("Данные не загружены. Пожалуйста, сначала загрузите все листы с помощью метода 'load_all_sheets'.")
            return []    

    ############################################################################
    #Вывод первых N строк данных с указанного листа (по умолчанию 5 строк). 
    def showDataFromSheet(self, sheet_name, rows=5):
        if sheet_name in self.data:
            print(self.data[sheet_name].head(rows))
        else:
            print(f"Лист '{sheet_name}' не найден в загруженных данных. Проверьте имя листа.")