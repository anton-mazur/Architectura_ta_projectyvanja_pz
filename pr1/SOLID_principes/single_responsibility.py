"""SRP: кожен клас має одну причину для зміни."""
from dataclasses import dataclass

@dataclass
class Invoice:
    customer: str
    amount: float

class InvoiceCalculator:
    def total_with_tax(self, invoice: Invoice) -> float:
        return invoice.amount * 1.2

class InvoicePrinter:
    def print(self, invoice: Invoice, total: float) -> str:
        return f"Рахунок для {invoice.customer}: {total:.2f} грн"

class InvoiceRepository:
    def save(self, invoice: Invoice) -> str:
        return f"Рахунок {invoice.customer} збережено"

if __name__ == "__main__":
    invoice = Invoice("Олена", 500)
    total = InvoiceCalculator().total_with_tax(invoice)
    print(InvoicePrinter().print(invoice, total))
    print(InvoiceRepository().save(invoice))
