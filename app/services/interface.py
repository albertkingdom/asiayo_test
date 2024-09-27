from abc import ABC, abstractmethod

# 驗證器interface
class ValidatorInterface(ABC):
    @abstractmethod
    def validate(self, order: dict) -> tuple[bool, str]:
        pass

# 轉換器interface
class TransformerInterface(ABC):
    @abstractmethod
    def convert_currency(self, price: str, currency: str) -> tuple[float, str]:
        pass