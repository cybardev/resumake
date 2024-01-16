from dataclasses import dataclass


@dataclass
class Address:
    street: str
    postal_code: str
    city: str = "Halifax"
    province: str = "NS"
    province_full: str = "Nova Scotia"
    country: str = "Canada"

    def __str__(self) -> str:
        return f"{self.city}, {self.province}, {self.postal_code}"

    def __repr__(self) -> str:
        return f"{self.street}, {self}"
