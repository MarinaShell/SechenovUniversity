class DataParser:
    ############################################################################
    #Инициализация класса DataParser
    def __init__(self):
        pass

    ############################################################################
    #Находит числовое значение с единицей измерения в строке.
    #Возвращает найденное значение и оставшуюся строку.
    #input_string: Строка, в которой нужно искать значение.
    #return: Кортеж (найденное значение, оставшаяся строка) или (None, исходная строка) если не найдено.
    def parseStringValue(self, input_string):
        # Регулярное выражение для поиска чисел с единицами измерения
        pattern_with_number = r'(\d+[.,]?\d*)\s*(гр|г|кг|мг|мл|л|шт|уп|м/уп|упак|пор|порция|вин|порц|ml|l)'
        # Регулярное выражение для поиска только единиц измерения без числа
        pattern_without_number = r'\b(гр|г|кг|мг|мл|л|шт|уп|упак|м/уп|пор|порция|вин|порц|ml|l)\b'

        # 1. Приводим строку к нижнему регистру
        input_string = input_string.lower()

        # 2. Сначала ищем все вхождения с числом и единицей измерения
        matches = re.findall(pattern_with_number, input_string)
        
        if matches:
            found_value = ' '.join(matches[0])  # Берем первое вхождение (число + единица измерения)
            # Удаляем все вхождения с числом и единицей измерения, включая знаки препинания
            remaining_string = re.sub(rf'{pattern_with_number}[.,]*\s*', ' ', input_string).strip()
        else:
            # 3. Если нет числа с единицей измерения, ищем только единицы измерения
            match = re.search(pattern_without_number, input_string)
            
            if match:
                # Если нашли, то считаем, что число перед ними равно 1
                found_value = f"1 {match.group(0)}"
                # Удаляем единицу измерения из строки, включая знаки препинания
                remaining_string = re.sub(rf'{pattern_without_number}[.,]*\s*', ' ', input_string).strip()
            else:
                return None, input_string

        # 4. Убираем все дополнительные единицы измерения
        remaining_string = re.sub(rf'{pattern_without_number}[.,]*\s*', ' ', remaining_string).strip()
  
        return found_value, remaining_string    

    ############################################################################
    #очищаем строку
    #input_string: Строка, которую нужно очистить
    def cleanString(self, input_string):
        # Убираем лишние пробелы (заменяем несколько пробелов одним)
        cleaned_string = re.sub(r'\s+', ' ', input_string).strip()
        
        return cleaned_string

    ############################################################################
    #Убирает из строки вхождения, соответствующие заданному шаблону.      
    #input_string: Строка, из которой нужно убрать вхождения.
    #pattern: Регулярное выражение для поиска шаблона.
    #return: Строка без вхождений, подходящих под шаблон.
    def remove_pattern(self, input_string, pattern):
        # Убираем все вхождения, соответствующие шаблону
        cleaned_string = re.sub(pattern, ' ', input_string).strip()
        
        # Убираем лишние пробелы
        cleaned_string = re.sub(r'\s+', ' ', cleaned_string).strip()
        
        return cleaned_string     