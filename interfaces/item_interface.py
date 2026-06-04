from abc import ABC, abstractmethod

class ItemInterface(ABC):

    @abstractmethod
    def tampilkan_info(self):
        pass

    @abstractmethod
    def hitung_nilai_stok(self):
        
        pass

    @abstractmethod
    def to_dict(self):
        pass