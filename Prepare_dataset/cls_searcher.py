class Searcher:
    ############################################################################
    #Инициализация класса Searcher с данными
    def __init__(self, data):
        self.data = data

    # Поиск строки в таблице, где value1 и value2 находятся в столбцах с индексами column_index1 и column_index2 и
    # если строка найдена, то умножение каждого значения в найденных строках на число multiplier.
    # value1: Первое значение для поиска.
    # value2: Второе значение для поиска.
    # column_index1: Индекс первого столбца для поиска первого значения.
    # column_index2: Индекс второго столбца для поиска второго значения.
    # multiplier: Число для умножения найденных значений.
    # return: Найденные строки с умноженными значениями или None.
    def getResultBy2Values(self, value1, value2, column_index1, column_index2, multiplier):
        results = {}

        # Проходим по каждому листу в данных
        for sheet_name, sheet_data in self.data.items():
            # Проверка, что индексы столбцов находятся в пределах DataFrame
            if column_index1 < 0 or column_index1 >= sheet_data.shape[1] or column_index2 < 0 or column_index2 >= sheet_data.shape[1]:
                print(f"Указаны неверные индексы столбцов для листа {sheet_name}. Пропуск.")
                continue

            # Фильтрация по значениям в указанных столбцах
            filtered_data = sheet_data[(sheet_data.iloc[:, column_index1] == value1) & (sheet_data.iloc[:, column_index2] == value2)]

            # Если найдены строки, умножаем значения на multiplier
            if not filtered_data.empty:
                # Умножаем все значения в строках на multiplier
                filtered_data_multiplied = filtered_data.applymap(lambda x: x * multiplier if pd.api.types.is_numeric_dtype(type(x)) else x)
                 # Сохраняем исходные двухуровневые названия столбцов (MultiIndex)
                if isinstance(filtered_data.columns, pd.MultiIndex):
                    new_columns = filtered_data.columns
                else:
                    new_columns = pd.MultiIndex.from_tuples([(col, '') for col in filtered_data.columns])

                # Применяем исходные двухуровневые заголовки столбцов
                filtered_data_multiplied.columns = new_columns

                results[sheet_name] = filtered_data_multiplied
        if results:
            return results
        else:
            print("Соответствие не найдено ни в одном листе.")
            return None

    # Поиск строки в таблице, где value1 и value2 находятся в столбцах с индексами column_index1 и column_index2.
    # value1: Первое значение для поиска.
    # value2: Второе значение для поиска.
    # column_index1: Индекс первого столбца для поиска первого значения.
    # column_index2: Индекс второго столбца для поиска второго значения.
    # return: результат поиска (true/false)
    def findRowBy2Values(self, value1, value2, column_index1, column_index2):
        # Проходим по каждому листу в данных
        for sheet_name, sheet_data in self.data.items():
            # Проверка, что индексы столбцов находятся в пределах DataFrame
            if column_index1 < 0 or column_index1 >= sheet_data.shape[1] or column_index2 < 0 or column_index2 >= sheet_data.shape[1]:
                print(f"Указаны неверные индексы столбцов для листа {sheet_name}. Пропуск.")
                continue

            # Фильтрация по значениям в указанных столбцах
            filtered_data = sheet_data[(sheet_data.iloc[:, column_index1] == value1) & (sheet_data.iloc[:, column_index2] == value2)]

            # Если найдены строки, возвращаем True
            if not filtered_data.empty:
                print("Соответствие найдено!")
                return True

        # Если ни одна строка не найдена, возвращаем False
        print("Соответствие не найдено ни в одном листе.")
        return False         