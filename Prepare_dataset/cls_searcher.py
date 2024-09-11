class Searcher:
    ############################################################################
    #������������� ������ Searcher � �������
    def __init__(self, data):
        self.data = data

    # ����� ������ � �������, ��� value1 � value2 ��������� � �������� � ��������� column_index1 � column_index2 �
    # ���� ������ �������, �� ��������� ������� �������� � ��������� ������� �� ����� multiplier.
    # value1: ������ �������� ��� ������.
    # value2: ������ �������� ��� ������.
    # column_index1: ������ ������� ������� ��� ������ ������� ��������.
    # column_index2: ������ ������� ������� ��� ������ ������� ��������.
    # multiplier: ����� ��� ��������� ��������� ��������.
    # return: ��������� ������ � ����������� ���������� ��� None.
    def getResultBy2Values(self, value1, value2, column_index1, column_index2, multiplier):
        results = {}

        # �������� �� ������� ����� � ������
        for sheet_name, sheet_data in self.data.items():
            # ��������, ��� ������� �������� ��������� � �������� DataFrame
            if column_index1 < 0 or column_index1 >= sheet_data.shape[1] or column_index2 < 0 or column_index2 >= sheet_data.shape[1]:
                print(f"������� �������� ������� �������� ��� ����� {sheet_name}. �������.")
                continue

            # ���������� �� ��������� � ��������� ��������
            filtered_data = sheet_data[(sheet_data.iloc[:, column_index1] == value1) & (sheet_data.iloc[:, column_index2] == value2)]

            # ���� ������� ������, �������� �������� �� multiplier
            if not filtered_data.empty:
                # �������� ��� �������� � ������� �� multiplier
                filtered_data_multiplied = filtered_data.applymap(lambda x: x * multiplier if pd.api.types.is_numeric_dtype(type(x)) else x)
                 # ��������� �������� ������������� �������� �������� (MultiIndex)
                if isinstance(filtered_data.columns, pd.MultiIndex):
                    new_columns = filtered_data.columns
                else:
                    new_columns = pd.MultiIndex.from_tuples([(col, '') for col in filtered_data.columns])

                # ��������� �������� ������������� ��������� ��������
                filtered_data_multiplied.columns = new_columns

                results[sheet_name] = filtered_data_multiplied
        if results:
            return results
        else:
            print("������������ �� ������� �� � ����� �����.")
            return None

    # ����� ������ � �������, ��� value1 � value2 ��������� � �������� � ��������� column_index1 � column_index2.
    # value1: ������ �������� ��� ������.
    # value2: ������ �������� ��� ������.
    # column_index1: ������ ������� ������� ��� ������ ������� ��������.
    # column_index2: ������ ������� ������� ��� ������ ������� ��������.
    # return: ��������� ������ (true/false)
    def findRowBy2Values(self, value1, value2, column_index1, column_index2):
        # �������� �� ������� ����� � ������
        for sheet_name, sheet_data in self.data.items():
            # ��������, ��� ������� �������� ��������� � �������� DataFrame
            if column_index1 < 0 or column_index1 >= sheet_data.shape[1] or column_index2 < 0 or column_index2 >= sheet_data.shape[1]:
                print(f"������� �������� ������� �������� ��� ����� {sheet_name}. �������.")
                continue

            # ���������� �� ��������� � ��������� ��������
            filtered_data = sheet_data[(sheet_data.iloc[:, column_index1] == value1) & (sheet_data.iloc[:, column_index2] == value2)]

            # ���� ������� ������, ���������� True
            if not filtered_data.empty:
                print("������������ �������!")
                return True

        # ���� �� ���� ������ �� �������, ���������� False
        print("������������ �� ������� �� � ����� �����.")
        return False         