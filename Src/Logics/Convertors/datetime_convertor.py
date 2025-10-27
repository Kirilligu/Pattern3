from Src.Core.abstract_convertor import abstract_convertor
from datetime import datetime

class datetime_convertor(abstract_convertor):
    """
    Конвертер для типа DateTime
    """
    def convert(self, obj) -> dict:
        result = {}
        if isinstance(obj, datetime):
            #преобразуем в строку в стандартном формате
            result['datetime'] = obj.isoformat()
            result['date'] = obj.date().isoformat()
            result['time'] = obj.time().isoformat()
        return result