class ExcelReader:
    ############################################################################
    #������������� ������ ExcelReader � ��������� ���� � �����.
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = {}

    ############################################################################
    #�������� ���� ������ �� Excel �����.
    def loadAllSheets(self):
        try:
            self.data = pd.read_excel(self.file_path, sheet_name=None)  # ��������� ��� �����
            print(f"��� ����� �� ����� '{self.file_path}' ������� ���������.")
            return self.data
        except FileNotFoundError:
            print(f"���� '{self.file_path}' �� ������.")
        except Exception as e:
            print(f"������ ��� �������� �����: {e}")

    ############################################################################
    #�������� ������ �� Excel �����. ���� �� ������ ����, ����������� ������ ����.
    def loadSheet(self, sheet_name=None):
        try:
            self.data = pd.read_excel(self.file_path, sheet_name=sheet_name)
            print(f"����{sheet_name} �����'{self.file_path}' ������� ��������.")
            return self.data
        except FileNotFoundError:
            print(f"���� '{self.file_path}' �� ������.")
        except Exception as e:
            print(f"������ ��� �������� �����: {e}")

    ############################################################################
    #��������� ���� ���� ������ � Excel �����.
    def getSheetNames(self):
        if self.data:
            return list(self.data.keys())
        else:
            print("������ �� ���������. ����������, ������� ��������� ��� ����� � ������� ������ 'load_all_sheets'.")
            return []    

    ############################################################################
    #����� ������ N ����� ������ � ���������� ����� (�� ��������� 5 �����). 
    def showDataFromSheet(self, sheet_name, rows=5):
        if sheet_name in self.data:
            print(self.data[sheet_name].head(rows))
        else:
            print(f"���� '{sheet_name}' �� ������ � ����������� ������. ��������� ��� �����.")