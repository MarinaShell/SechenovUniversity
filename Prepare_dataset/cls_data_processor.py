class DataProcessor:
    ############################################################################
    # ������������� ������ DataProcessor
    def __init__(self, data):
        self.data = data

    ############################################################################
    #�������� ���� ��������, � ������� ��� ��������.
    def removeEmptyColumns(self):
        if isinstance(self.data, dict):
            for sheet_name, df in self.data.items():
                # ��������� dropna() � ������� DataFrame (������� �����)
                self.data[sheet_name] = df.dropna(axis=1, how='all')
            print("������ ������� ������� �� ���� ������.")
        else:
            print("������ ������ ���� �������� ������.")
        return self

    ############################################################################
    #�������� ���� �����, ��� � ��������� ������� ���� �������� ��������.
    #���� ������� �� �������, ����������� ��� �������.
    def removeRowsWithValue(self, value, column=None):
        if isinstance(self.data, dict):
            for sheet_name, df in self.data.items():
                if column is not None:
                    # �������� �����, ��� � ��������� ������� ��������� ��������
                    if column in df.columns:
                        self.data[sheet_name] = df[df[column] != value]
                    else:
                        print(f"������� {column} �� ������ � ����� {sheet_name}. �������.")
                else:
                    # �������� �����, ��� �������� ��������� � ����� �������
                    self.data[sheet_name] = df[~df.isin([value]).any(axis=1)]
            print(f"������ � ��������� {value} ������� �� ���� ������.")
        else:
            print("������ ������ ���� �������� ������.")
        return self

    ############################################################################
    #�������� ������� �� ���������� ����� ��� �� ���� ������.
    #���� column � ��� ������, �� ������� ������� �� �������.
    #���� column � ��� �������� �������, ������� �� ��������.
    #column: ������ ��� �������� ������� ��� ��������.
    #sheet_name: �������� ����� ��� �������� �������. ���� None, ������� ������� �� ���� ������.
    def removeColumn(self, column, sheet_name=None):
        if isinstance(self.data, dict):
            # ���� ������ ���������� ����
            if sheet_name is not None:
                if sheet_name in self.data:
                    df = self.data[sheet_name]
                    self._removeColumnFromDf(df, column, sheet_name)
                else:
                    print(f"���� '{sheet_name}' �� ������.")
            else:
                # ���� ���� �� ������, ������������ ��� �����
                for sheet_name, df in self.data.items():
                    self._removeColumnFromDf(df, column, sheet_name)
        else:
            print("������ ������ ���� �������� ������.")
        
        return self

    ############################################################################
    #��������������� ������� ��� �������� ������� �� ����������� DataFrame.
    def _removeColumnFromDf(self, df, column, sheet_name):
        if isinstance(column, int):
            if 0 <= column < df.shape[1]:
                # �������� �� ������� �������
                self.data[sheet_name] = df.drop(df.columns[column], axis=1)
                print(f"������� � �������� {column} ������ �� ����� '{sheet_name}'.")
            else:
                print(f"������ {column} ��� ��������� �������� � ����� '{sheet_name}'. �������.")
        elif isinstance(column, str):
            if column in df.columns:
                # �������� �� �������� �������
                self.data[sheet_name] = df.drop(column, axis=1)
                print(f"������� '{column}' ������ �� ����� '{sheet_name}'.")
            else:
                print(f"������� '{column}' �� ������ � ����� '{sheet_name}'. �������.")
        else:
            print("������������ ��� �������. ����������� ������ ��� ��������.")

    ############################################################################
    #���������� ������������ ������.
    def getProcessedData(self):
        return self.data

    ############################################################################
    #������ ������������ ������ � Excel ����.
    #output_file_path: ����, �� �������� ����� �������� ����.
    def save2Excel(self, output_file_path):
        try:
            # ������� ������ ExcelWriter ��� ������ � ����
            with pd.ExcelWriter(output_file_path, engine='openpyxl') as writer:
                # ���������� ������ ���� (DataFrame) � ���� ���� Excel �����
                for sheet_name, df in self.data.items():
                    df.to_excel(writer, sheet_name=sheet_name, index=False)
            
            print(f"������ ������� ��������� � ����: {output_file_path}")
      
        except Exception as e:
            print(f"������ ��� ���������� ������ � Excel ����: {e}")

    ############################################################################
    #����� ������ N ����� ������ � ���������� ����� (�� ��������� 5 �����). 
    def showDataFromSheet(self, sheet_name, rows=5):
        if sheet_name in self.data:
            print(self.data[sheet_name].head(rows))
        else:
            print(f"���� '{sheet_name}' �� ������ � ����������� ������. ��������� ��� �����.")     