class Machine:
    def print(self,document):
        raise NotImplementedError
    def fax(self,document):
        raise NotImplementedError

    def scan(self,document):
        raise NotImplementedError


class MultiFunctionPrinter(Machine):
    def fax(self, document):
        return super().fax(document)

    def print(self, document):
        return super().fax(document)
    def scan(self, document):
        return super().fax(document)

class OldFashionPrinter(Machine):
    def fax(self, document):
        return super().fax(document)

    def print(self, document):
        return super().fax(document)
    def scan(self, document):
        raise NotImplementedError("Printer can't scan")
