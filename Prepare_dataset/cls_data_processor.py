class DataProcessor:
    ############################################################################
    # Инициализация класса DataProcessor
    def __init__(self, data):
        self.data = data

    ############################################################################
    #Удаление всех столбцов, в которых нет значений.
    def removeEmptyColumns(self):
        if isinstance(self.data, dict):
            for sheet_name, df in self.data.items():
                # Применяем dropna() к каждому DataFrame (каждому листу)
                self.data[sheet_name] = df.dropna(axis=1, how='all')
            print("Пустые столбцы удалены во всех листах.")
        else:
            print("Данные должны быть словарем листов.")
        return self

    ############################################################################
    #Удаление всех строк, где в указанной колонке есть заданное значение.
    #Если колонка не указана, проверяются все колонки.
    def removeRowsWithValue(self, value, column=None):
        if isinstance(self.data, dict):
            for sheet_name, df in self.data.items():
                if column is not None:
                    # Удаление строк, где в указанной колонке находится значение
                    if column in df.columns:
                        self.data[sheet_name] = df[df[column] != value]
                    else:
                        print(f"Столбец {column} не найден в листе {sheet_name}. Пропуск.")
                else:
                    # Удаление строк, где значение находится в любой колонке
                    self.data[sheet_name] = df[~df.isin([value]).any(axis=1)]
            print(f"Строки с значением {value} удалены во всех листах.")
        else:
            print("Данные должны быть словарем листов.")
        return self

    ############################################################################
    #Удаление столбца из указанного листа или из всех листов.
    #Если column — это индекс, то удаляем столбец по индексу.
    #Если column — это название столбца, удаляем по названию.
    #column: Индекс или название столбца для удаления.
    #sheet_name: Название листа для удаления столбца. Если None, удаляет столбец во всех листах.
    def removeColumn(self, column, sheet_name=None):
        if isinstance(self.data, dict):
            # Если указан конкретный лист
            if sheet_name is not None:
                if sheet_name in self.data:
                    df = self.data[sheet_name]
                    self._removeColumnFromDf(df, column, sheet_name)
                else:
                    print(f"Лист '{sheet_name}' не найден.")
            else:
                # Если лист не указан, обрабатываем все листы
                for sheet_name, df in self.data.items():
                    self._removeColumnFromDf(df, column, sheet_name)
        else:
            print("Данные должны быть словарем листов.")
        
        return self

    ############################################################################
    #Вспомогательная функция для удаления столбца из конкретного DataFrame.
    def _removeColumnFromDf(self, df, column, sheet_name):
        if isinstance(column, int):
            if 0 <= column < df.shape[1]:
                # Удаление по индексу столбца
                self.data[sheet_name] = df.drop(df.columns[column], axis=1)
                print(f"Столбец с индексом {column} удален из листа '{sheet_name}'.")
            else:
                print(f"Индекс {column} вне диапазона столбцов в листе '{sheet_name}'. Пропуск.")
        elif isinstance(column, str):
            if column in df.columns:
                # Удаление по названию столбца
                self.data[sheet_name] = df.drop(column, axis=1)
                print(f"Столбец '{column}' удален из листа '{sheet_name}'.")
            else:
                print(f"Столбец '{column}' не найден в листе '{sheet_name}'. Пропуск.")
        else:
            print("Некорректный тип столбца. Используйте индекс или название.")

    ############################################################################
    #Возвращает обработанные данные.
    def getProcessedData(self):
        return self.data

    ############################################################################
    #Запись обработанных данных в Excel файл.
    #output_file_path: Путь, по которому будет сохранен файл.
    def save2Excel(self, output_file_path):
        try:
            # Создаем объект ExcelWriter для записи в файл
            with pd.ExcelWriter(output_file_path, engine='openpyxl') as writer:
                # Записываем каждый лист (DataFrame) в свой лист Excel файла
                for sheet_name, df in self.data.items():
                    df.to_excel(writer, sheet_name=sheet_name, index=False)
            
            print(f"Данные успешно сохранены в файл: {output_file_path}")
      
        except Exception as e:
            print(f"Ошибка при сохранении данных в Excel файл: {e}")

    ############################################################################
    #Вывод первых N строк данных с указанного листа (по умолчанию 5 строк). 
    def showDataFromSheet(self, sheet_name, rows=5):
        if sheet_name in self.data:
            print(self.data[sheet_name].head(rows))
        else:
            print(f"Лист '{sheet_name}' не найден в загруженных данных. Проверьте имя листа.")     