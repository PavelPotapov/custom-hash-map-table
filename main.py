import copy

class HasTable:
    def __init__(self, size=1000) -> None:
        self.data = [HashData(None, None, False, True) for i in range(1)] #стартовая размерность
        self.size = size
    def append(self, key, value):
        index = self.my_hash(key)
        try:
            if self.data[index].key == key: #перезапись данных по ключу
                self.data[index].data = value
                self.data[index].key = key
                self.data[index].is_empty = False
            else: #если такой ключ встречается впервые
                while self.data[index].is_empty == False or self.data[index].is_deleted == True: #генерируем хеш новой ячейки
                    index = self.my_hash(str(index)) 
                self.data[index].data = value
                self.data[index].key = key
                self.data[index].is_empty = False
                self.data[index].is_deleted = False
        except IndexError:
            #увеличиваем размерность массива если ее недостаточно
            #делаем глубокую копию массива
            data_new = [HashData(None, None, False, True) for i in range(index+1)]
            k = 0
            for i in self.data:
                data_new[k] = i
                k += 1
            self.data = copy.deepcopy(data_new)
            data_new.clear()
            self.append(key, value)

    def my_hash(self, text):
        index = 0
        #for symbol in text:
        #    index += ord(symbol)
        index = abs(hash(text))
        index %= self.size
        #index %= len(self.data)
        return index
       
    def print_info(self):
        k = 0
        for i in self.data:
            if i.data != None:
                print('-' * 5 + str(k)  + '-' * 5)
                print('Данные:', i.data)
                print('Ключ:', i.key)
                print('is_del:', i.is_deleted)
                print('is_empty', i.is_empty)
                print('-'*10, '\n')
            k += 1

    def get_data(self, key):
        index = self.my_hash(key) #получаем индекс
        try:
            if self.data[index].is_empty == True:
                return key + ' - ' + ' Такого ключа не существует'
        except IndexError:
            try:
                while self.data[index].key != key:
                    index = self.my_hash(str(index))
                return self.data[index].data
            except IndexError:
                return key + ' - ' + ' Такого ключа не существует'     
    
    def del_data(self, key):
        index = self.my_hash(key)
        try:
            while self.data[index].key != key:
                index = self.my_hash(str(index))
            self.data[index].data = None
            self.data[index].is_deleted = True
            return 'Данные успешно удалены из таблицы'
        except IndexError:
            return key + ' - ' + ' Такого ключа не существует'
        
class HashData:
    def __init__(self, data, key, is_deleted, is_empty):
        self.data = data
        self.is_deleted = is_deleted
        self.is_empty = is_empty
        self.key = key
        
h = HasTable()


for i in range(100):
    h.append(str(i), 'aefgaegae')


h.print_info()
print(h.get_data('0'))


        
        





