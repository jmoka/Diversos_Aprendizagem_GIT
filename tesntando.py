from pessoas import Pessoas

from chamando_classe_pessoas import pessoaFisica

pessoa_1 = Pessoas ("joão", 43, 1.8)
pessoa_2 = pessoaFisica (2334, 555555,"joão", 43, 1.8)
print(f'o cpf {pessoa_2.getCpf()} o titulo {pessoa_2.getTitulo()} o nome {pessoa_1.getNome()} a idade é {pessoa_1.getIdade()} e o peso {pessoa_1.getPeso()},')


