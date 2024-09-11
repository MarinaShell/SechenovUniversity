class DataParser:
    ############################################################################
    #������������� ������ DataParser
    def __init__(self):
        pass

    ############################################################################
    #������� �������� �������� � �������� ��������� � ������.
    #���������� ��������� �������� � ���������� ������.
    #input_string: ������, � ������� ����� ������ ��������.
    #return: ������ (��������� ��������, ���������� ������) ��� (None, �������� ������) ���� �� �������.
    def parseStringValue(self, input_string):
        # ���������� ��������� ��� ������ ����� � ��������� ���������
        pattern_with_number = r'(\d+[.,]?\d*)\s*(��|�|��|��|��|�|��|��|�/��|����|���|������|���|����|ml|l)'
        # ���������� ��������� ��� ������ ������ ������ ��������� ��� �����
        pattern_without_number = r'\b(��|�|��|��|��|�|��|��|����|�/��|���|������|���|����|ml|l)\b'

        # 1. �������� ������ � ������� ��������
        input_string = input_string.lower()

        # 2. ������� ���� ��� ��������� � ������ � �������� ���������
        matches = re.findall(pattern_with_number, input_string)
        
        if matches:
            found_value = ' '.join(matches[0])  # ����� ������ ��������� (����� + ������� ���������)
            # ������� ��� ��������� � ������ � �������� ���������, ������� ����� ����������
            remaining_string = re.sub(rf'{pattern_with_number}[.,]*\s*', ' ', input_string).strip()
        else:
            # 3. ���� ��� ����� � �������� ���������, ���� ������ ������� ���������
            match = re.search(pattern_without_number, input_string)
            
            if match:
                # ���� �����, �� �������, ��� ����� ����� ���� ����� 1
                found_value = f"1 {match.group(0)}"
                # ������� ������� ��������� �� ������, ������� ����� ����������
                remaining_string = re.sub(rf'{pattern_without_number}[.,]*\s*', ' ', input_string).strip()
            else:
                return None, input_string

        # 4. ������� ��� �������������� ������� ���������
        remaining_string = re.sub(rf'{pattern_without_number}[.,]*\s*', ' ', remaining_string).strip()
  
        return found_value, remaining_string    

    ############################################################################
    #������� ������
    #input_string: ������, ������� ����� ��������
    def cleanString(self, input_string):
        # ������� ������ ������� (�������� ��������� �������� �����)
        cleaned_string = re.sub(r'\s+', ' ', input_string).strip()
        
        return cleaned_string

    ############################################################################
    #������� �� ������ ���������, ��������������� ��������� �������.      
    #input_string: ������, �� ������� ����� ������ ���������.
    #pattern: ���������� ��������� ��� ������ �������.
    #return: ������ ��� ���������, ���������� ��� ������.
    def remove_pattern(self, input_string, pattern):
        # ������� ��� ���������, ��������������� �������
        cleaned_string = re.sub(pattern, ' ', input_string).strip()
        
        # ������� ������ �������
        cleaned_string = re.sub(r'\s+', ' ', cleaned_string).strip()
        
        return cleaned_string     