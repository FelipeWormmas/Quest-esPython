
class Nota:

    def __init__(self, nota:str):
        self.nota = nota

    def get_nota(self):
        return self.nota
    
    def set_nota(self,nota):
        self.nota = nota  

    def __repr__(self):
        return self.nota

class Aluno:

    def __init__(self,qtd_notas:int):
        self.qtd_notas = qtd_notas
        self.list_nota = []
    

    def inserir_notas(self):

        for i in range(self.qtd_notas):
            nota = int(input('> Informe a nota: '))
            nota = Nota(nota)
            self.list_nota.append(nota)
        
    def get_media(self):
        return sum([nota.get_nota() for nota in self.list_nota]) / self.qtd_notas

    
    def __repr__(self) -> str:
        list_nota = ""
        for nota in self.list_nota:
            list_nota += " \n " + str(nota.get_nota())
        return f"As notas lidas são {list_nota} e a média é {str(self.get_media())} "


aluno = Aluno(4)
aluno.inserir_notas()
print(aluno)