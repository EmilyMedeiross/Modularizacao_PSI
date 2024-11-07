from database import get_connection

class Emprestimo:
    def __init__(self, titulo, data_emprestimo,user_id, book_id):
        self.titulo = titulo 
        self.data_emprestimo = data_emprestimo
        self.user_id = user_id
        self.book_id = book_id
      
        
    def save(self):
        conn = get_connection()
        conn.execute("INSERT INTO emprestimos(titulo, data_emprestimo, user_id, book_id ) values(?,?,?,?)", (self.titulo,self.data_emprestimo, self.user_id, self.book_id))
        conn.commit()
        conn.close()
        return True

    @classmethod
    def all(cls):
        conn = get_connection()
        emprestimos = conn.execute("SELECT * FROM emprestimos").fetchall()
        return emprestimos
    

