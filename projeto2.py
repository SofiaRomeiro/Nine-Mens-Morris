# Sofia Romeiro ist 98968


#-------------------------------------------------------------------------------------#
#                                       POSICAO                                       #
#-------------------------------------------------------------------------------------#

# - Construtores
def cria_posicao(c, l):
	'''
	Funcao : Recebe uma coluna ('a, 'b', 'c') - string - e uma linha ('1', '2', '3') - string - \
	e devolve a respetiva posicao. Valida os argumentos dados. 
	Recebe : 2 x string com a coluna e linha
	Devolve : posicao 
	Representacao da posicao : inteiros de 0 a 8 correspondentes a ordem de leitura do tabuleiro
	'''
	if c not in ('a', 'b', 'c') or type(c) != str or l not in ('1', '2', '3') or type(l) != str:
		raise ValueError('cria_posicao: argumentos invalidos')
	if c == 'a':
		if l == '1': return 0
		if l == '2': return 3 
		if l == '3': return 6 
	elif c == 'b':
		if l == '1': return 1 
		if l == '2': return 4 
		if l == '3': return 7 
	else:
		if l == '1': return 2 
		if l == '2': return 5 
		if l == '3': return 8 

def cria_copia_posicao(p):
	'''
	Funcao : Efetua uma copia da posicao pretentida
	Recebe : posicao (0 a 8)
	Devolve : posicao (0 a 8)
	'''
	return cria_posicao(obter_pos_c(p), obter_pos_l(p))

# - Seletores
def obter_pos_c(p):
	'''
	Funcao : Obtem a coluna correspondente a posicao
	Recebe : posicao (0 a 8)
	Devolve : string com a respetiva coluna ('a', 'b', 'c') da posicao dada
	'''
	if p in (0, 3, 6): return 'a'
	elif p in (1, 4, 7): return 'b'
	elif p in (2, 5, 8): return 'c'

def obter_pos_l(p):
	'''
	Funcao : Obtem a coluna correspondente a posicao
	Recebe : posicao (0 a 8)
	Devolve : string com a respetiva linha ('1', '2', '3') da posicao dada
	'''
	if p in (0, 1, 2): return '1'
	elif p in (3, 4, 5): return '2'
	elif p in (6, 7, 8): return '3'

# - Reconhecedor
def eh_posicao(arg):
	'''
	Funcao : Verifica se o argumento recebido e uma posicao
		-> Requisitos: numero inteiro entre 0 e 8
	Recebe : argumento de qualquer tipo
	Devolve : True se for uma posicao, False caso contrario
	'''
	return type(arg) == int and arg in range(0,9)

# - Teste
def posicoes_iguais(p1, p2):
	'''
	Funcao : Compara as posicoes dadas, vendo se sao iguais
	Recebe : 2 x posicao 
	Devolve : True se forem posicoes iguais, False caso contrario
	'''
	return eh_posicao(p1) and eh_posicao(p2) and p1 == p2

# - Transformador
def posicao_para_str(p):
	'''
	Funcao : Transforma a posicao dada numa string
		-> String : coluna - ('a', 'b', 'c') + linha - ('1', '2', '3')
	Recebe : posicao
	Devolve : string contendo a coluna e a linha a que pertence a posicao 
	'''
	return str((obter_pos_c(p)) + (obter_pos_l(p)))

#-------------------------------------------------------------------------------------#

# - Funcoes AN
def obter_posicoes_adjacentes(p):
	'''
	Funcao : Indica quais as posicoes adjacentes a introduzida
	Recebe : posicao (0 a 8)
	Devolve : tuplo com as posicoes adjacentes (0 a 8)
	'''
	# primeira linha :
	if posicoes_iguais(p, cria_posicao('a', '1')): 
		return (cria_posicao('b', '1'), cria_posicao('a', '2'), cria_posicao('b', '2'))
	if posicoes_iguais(p, cria_posicao('b', '1')): 
		return (cria_posicao('a', '1'), cria_posicao('c', '1'), cria_posicao('b', '2'))
	if posicoes_iguais(p, cria_posicao('c', '1')): 
		return (cria_posicao('b', '1'), cria_posicao('b', '2'), cria_posicao('c', '2'))
	# segunda linha :
	if posicoes_iguais(p, cria_posicao('a', '2')): 
		return (cria_posicao('a', '1'), cria_posicao('b', '2'), cria_posicao('a', '3'))
	if posicoes_iguais(p, cria_posicao('b', '2')): 
		return (cria_posicao('a', '1'), cria_posicao('b', '1'), cria_posicao('c', '1'), \
			cria_posicao('a', '2'), cria_posicao('c', '2'), cria_posicao('a', '3'), \
			cria_posicao('b', '3'), cria_posicao('c', '3'))
	if posicoes_iguais(p, cria_posicao('c', '2')): 
		return (cria_posicao('c', '1'), cria_posicao('b', '2'), cria_posicao('c', '3'))
	# terceira linha :
	if posicoes_iguais(p, cria_posicao('a', '3')): 
		return (cria_posicao('a', '2'), cria_posicao('b', '2'), cria_posicao('b', '3'))
	if posicoes_iguais(p, cria_posicao('b', '3')): 
		return (cria_posicao('b', '2'), cria_posicao('a', '3'), cria_posicao('c', '3'))
	if posicoes_iguais(p, cria_posicao('c', '3')): 
		return (cria_posicao('b', '2'), cria_posicao('c', '2'), cria_posicao('b', '3'))

def pos_para_int(c, l):
	'''
	Funcao : converte uma posicao dada num inteiro 
	Recebe : posicao representada pela coluna e linha correspondentes
		-> coluna : ('a', 'b', 'c')
		-> linha : ('1', '2', '3')
	Devolve : inteiro entre 0 e 8
	'''
	if c == 'a':
		if l == '1': return 0
		if l == '2': return 3
		if l == '3': return 6
	if c == 'b':
		if l == '1': return 1
		if l == '2': return 4
		if l == '3': return 7
	if c == 'c':
		if l == '1': return 2
		if l == '2': return 5
		if l == '3': return 8 

#-------------------------------------------------------------------------------------#
#                                          PECA                                       #
#-------------------------------------------------------------------------------------#

# - Construtores
def cria_peca(s):
	'''
	Funcao : Transforma o identificador do jogador / peca livre e devolve a peca correspondente 
	Recebe : string que identifica o jogador - ('X', 'O') - \
	ou uma peca livre - (' ') 
	Devolve : peca
	Representacao da peca : 
		-> string : 'X', jogador X; 
		-> string : 'O', jogador O;
		-> string : ' ', peca vazia
	'''
	if s not in ('X', 'O', ' ') or type(s) != str:
		raise ValueError('cria_peca: argumento invalido')
	return s

def cria_copia_peca(j):
	'''
	Funcao : Efetua uma copia da peca pretendida
	Recebe : peca ('X', 'O', ' ')
	Devolve : peca ('X', 'O', ' ')
	'''
	return  cria_peca(j)

# - Reconhecedor
def eh_peca(arg):
	'''
	Funcao : Verifica se o argumento recebido e uma peca
		-> Requisitos : string contida em ('X', 'O', ' ')
	Recebe : argumento de qualquer tipo
	Devolve : True se for uma peca, False caso contrario
	'''
	return type(arg) == str and arg in ('X', 'O', ' ')

# - Teste
def pecas_iguais(j1, j2):
	'''
	Funcao : Compara as pecas entre si e verifica se correspondem a pecas
	Recebe : 2 x peca
	Devolve : True se forem pecas iguais, False caso contrario 
	'''
	return eh_peca(j1) and eh_peca(j2) and j1 == j2

# - Transformador
def peca_para_str(j):
	'''
	Funcao : Devolve a representacao da peca do jogador 
		-> Representacao : '[X]', '[O]', '[ ]'
	Recebe : peca
	Devolve : string contendo a representacao exterior da peca 
	'''
	return str('[' + j + ']')


#-------------------------------------------------------------------------------------#

# - Funcoes AN
def peca_para_inteiro(j):
	'''
	Funcao : Avalia a que jogador pertence a peca
	Recebe : peca ('X', 'O', ' ')
	Devolve : inteiro correspondente a peca
		-> 1 : jogador 'X'
		-> -1 : jogador 'O'
		-> 0 : peca livre
	'''
	if pecas_iguais(j, cria_peca('X')): return 1
	if pecas_iguais(j, cria_peca('O')): return -1
	if pecas_iguais(j, cria_peca(' ')): return 0

#-------------------------------------------------------------------------------------#
#                                       TABULEIRO                                     #
#-------------------------------------------------------------------------------------#

# - Construtores
def cria_tabuleiro():
	'''
	Funcao : Cria um tabuleiro de jogo livre
	Devolve : tabuleiro de jogo livre
	Nota : Esta funcao nao requer qualquer input
	Representacao do tabuleiro : lista com 9 elementos contendo pecas livres (' ')
	'''
	return 9 * [cria_peca(' ')]

def cria_copia_tabuleiro(t):
	'''
	Funcao : Cria uma copia do tabuleiro de jogo
	Recebe : tabuleiro de jogo (lista contendo 9 pecas)
	Devolve : copia nova do tabuleiro
	'''
	return (t + ['.'])[:-1]

# - Seletores
def obter_peca(t, p):
	'''
	Funcao : Devolve a peca que esta na posicao escolhida
	Recebe : tabuleiro de jogo e posicao
		-> Posicao : string contendo a coluna e linha
	Devolve : peca que ocupa a posicao escolhida
	'''
	pos_ind = pos_para_int(obter_pos_c(p), obter_pos_l(p))
	return t[pos_ind]

def obter_vetor(t, s):
	'''
	Funcao : Apresenta todas as pecas contidas na linha / coluna selecionadas
	Recebe : tabuleiro de jogo, coluna ou linha (string)
	Devolve : tuplo de pecas por ordem de leitura do tabuleiro
	'''
	if s == 'a': return (t[0], t[3], t[6])
	if s == 'b': return (t[1], t[4], t[7])
	if s == 'c': return (t[2], t[5], t[8])
	if s == '1': return (t[0], t[1], t[2])
	if s == '2': return (t[3], t[4], t[5])
	if s == '3': return (t[6], t[7], t[8])

# - Modificador
def coloca_peca(t, j, p):
	'''
	Funcao : Modifica o tabuleiro, colocando a peca do jogador dado na posicao escolhida
	Recebe : tabuleiro de jogo, peca correspondente ao jogador a marcar, \
	posicao a ser marcada
	Devolve : tabuleiro de jogo modificado 
	'''
	pos_ind = pos_para_int(obter_pos_c(p), obter_pos_l(p))
	t[pos_ind] = j
	return t

def remove_peca(t, p):
	'''
	Funcao : Modifica o tabuleiro, removendo a peca existente da posicao escolhida
	Recebe : tabuleiro de jogo, posicao cuja peca sera removida
	Devolve : tabuleiro de jogo modificado
	'''
	pos_ind = pos_para_int(obter_pos_c(p), obter_pos_l(p))
	t[pos_ind] = cria_peca(' ')
	return t

def move_peca(t, p1, p2):
	'''
	Funcao : Modifica o tabuleiro, movendo a peca da primeira posicao introduzida \
	para a segunda posicao introduzida
	Recebe : tabuleiro de jogo, posicao de origem, posicao de destino
	Devolve : tabuleiro de jogo modificado
	'''
	pos_inicio = pos_para_int(obter_pos_c(p1), obter_pos_l(p1))
	pos_fim = pos_para_int(obter_pos_c(p2), obter_pos_l(p2))
	peca = obter_peca(t, pos_inicio)
	t = remove_peca(t, pos_inicio)
	t = coloca_peca(t, peca, pos_fim)
	return t

# - Reconhecedor 
def eh_tabuleiro(arg):
	'''
	Funcao : Avalia se o argumento introduzido e um tabuleiro valido de acordo com \
	a representacao escolhida
	Recebe : argumento de qualquer tipo
	Devolve : True se corresponde a um tabuleiro de jogo, False caso contrario
	'''
	count_X, count_O, vitoria = 0, 0, 0

	if type(arg) == list and len(arg) == 9:
		for i in range(len(arg)):
			if eh_peca(arg[i]):
				if pecas_iguais(cria_peca(arg[i]), cria_peca('X')):
					count_X += 1
				elif pecas_iguais(cria_peca(arg[i]), cria_peca('O')):
					count_O += 1			

		for peca_str in ('X', 'O'):
			peca = cria_peca(peca_str)
			for index in ('a', 'b', 'c', '1', '2', '3'):
				vetor = obter_vetor(arg, index)
				if all(pecas_iguais(peca, p) for p in vetor):
					vitoria += 1
	
		return all(eh_peca(peca) for peca in arg) and count_X < 4 and count_O < 4 \
			and abs(count_X - count_O) < 2 and vitoria < 2

	return False

def eh_posicao_livre(t, p):
	'''
	Funcao : Verifica se a posicao escolhida esta ou nao livre
	Recebe : tabuleiro de jogo, posicao
	Devolve : True se esta livre, False caso contrario
	'''
	indice = pos_para_int(obter_pos_c(p), obter_pos_l(p))
	return pecas_iguais(t[indice], cria_peca(' '))


# - Teste
def tabuleiros_iguais(t1,t2):
	'''
	Funcao : Compara dois tabuleiros, verificando se sao iguais  
	Recebe : 2 x tabuleiro de jogo
	Devolve : True se sao iguais, False caso contrario
	'''
	return eh_tabuleiro(t1) and eh_tabuleiro(t2) and all(pecas_iguais(peca1, peca2) \
		for peca1, peca2 in zip(t1,t2))

# - Transformador
def tabuleiro_para_str(t):
	'''
	Funcao : Transforma a representacao interna (TAD tabuleiro) do tabuleiro de jogo \
	na sua representacao em string
		-> Representacao interna : lista com 9 pecas
	Recebe : tabuleiro de jogo
	Devolve : string da representacao do tabuleiro
	'''
	return '   a   b   c\n1 '+peca_para_str(t[0])+'-'+peca_para_str(t[1])+'-'+peca_para_str(t[2])+'\n   | \\ | / |\n2 '+peca_para_str(t[3])+'-'+peca_para_str(t[4])+'-'+peca_para_str(t[5])+'\n   | / | \\ |\n3 '+peca_para_str(t[6])+'-'+peca_para_str(t[7])+'-'+peca_para_str(t[8])+''

def tuplo_para_tabuleiro(t):
	'''
	Funcao : Transforma um tuplo de 3 tuplos, contendo pecas, na representacao\
	interna de tabuleiro
	Recebe : tuplo de 3 tuplos contendo inteiros (1, -1, 0) que representam pecas
	Devolve : tabuleiro de jogo de acordo com a representacao interna 
	'''
	# transformar na representacao do tab :
	lista_tab = list(t[0]) + list(t[1]) + list(t[2])
	# converter 0, 1 e -1 em pecas 
	for i in range(len(lista_tab)):
		if lista_tab[i] == 1:
			lista_tab[i] = cria_peca('X')
		elif lista_tab[i] == -1:
			lista_tab[i] = cria_peca('O')
		else:
			lista_tab[i] = cria_peca(' ')
	return lista_tab

#-------------------------------------------------------------------------------------#

# - Funcoes AN
def obter_ganhador(t):
	'''
	Funcao : Verifica se ha um vencedor
	Recebe : tabuleiro de jogo
	Devolve : peca correspondente ao jogador que ganhou (caso tenha ocorrido uma vitoria)\
	ou uma peca livre (em caso de nao haver vitoria ate ao momento)
	'''
	for peca_str in ('X', 'O'):
		peca = cria_peca(peca_str)
		for index in ('a', 'b', 'c', '1', '2', '3'):
			vetor = obter_vetor(t, index)
			if all(pecas_iguais(peca, p) for p in vetor):
				return peca
	return cria_peca(' ')

def obter_posicoes_livres(t):
	'''
	Funcao : Indica as posicoes livres do tabuleiro
	Recebe : tabuleiro de jogo
	Devolve : tuplo contendo as posicoes livres do tabuleiro
	'''
	poslivres = ()
	for linha in ('1', '2', '3'):
		for coluna in ('a', 'b', 'c'):
			pos = cria_posicao(coluna, linha)
			if eh_posicao_livre(t, pos):
				poslivres += (pos,)
	return poslivres

def obter_posicoes_jogador(t, j):
	'''
	Funcao : Identifica as posicoes que estao ocupadas pelo \
	jogador introduzido 
	Recebe : tabuleiro de jogo, peca do jogador 
	Devolve : tuplo de posicoes ocupadas pelo jogador
	'''
	posjog = ()
	for linha in ('1', '2', '3'):
		for coluna in ('a', 'b', 'c'):		
			pos = cria_posicao(coluna, linha)
			peca = obter_peca(t, pos)
			if pecas_iguais(peca, j):
				posjog += (pos,)
	return posjog

#-------------------------------------------------------------------------------------#
#                                    FUNCOES ADICIONAIS                               #
#-------------------------------------------------------------------------------------#

def eh_fase_de_colocacao(t):
	'''
	Funcao : Avalia se a fase de jogo atual corresponde ou nao a fase de colocacao
	Recebe : tabuleiro de jogo
	Devolve : True se a fase atual e a fase de colocacao, False se e fase de movimento
	'''
	count_X, count_O = 0, 0
	for coluna in ('a', 'b', 'c'):
		for linha in ('1', '2', '3'):
			pos = cria_posicao(coluna, linha)
			peca = obter_peca(t, pos)
			if pecas_iguais(peca, cria_peca('X')):
				count_X += 1
			if pecas_iguais(peca, cria_peca('O')):
				count_O += 1
			
	return count_O < 3 or count_X < 3 


def obter_movimento_manual(t, Hpeca):
	'''
	Funcao : Representa a jogada do humano no tabuleiro
	Recebe : tabuleiro de jogo, peca que representa o jogador humano
	Devolve : tuplo de posicoes com 1 ou 2 elementos;
		-> Fase de colocacao : tuplo com 1 elemento correspondente a posicao de colocacao
		-> Fase de moviemnto : tuplo com 2 elementos, em que o primeiro e a \
	posicao de origem e o segundo a posicao de destino
	'''
	if eh_fase_de_colocacao(t):
		p = tuple(input('Turno do jogador. Escolha uma posicao: '))
		if len(p) != 2 or p[0] not in ('a', 'b', 'c') or p[1] not in ('1', '2', '3'):
			raise ValueError('obter_movimento_manual: escolha invalida')
		pos = cria_posicao(p[0], p[1])
		if not eh_posicao(pos) or not eh_posicao_livre(t, pos) :
			raise ValueError('obter_movimento_manual: escolha invalida')
		return (pos,)
	else:
		p = tuple(input('Turno do jogador. Escolha um movimento: '))
		if len(p) != 4 or p[0] not in ('a', 'b', 'c') or p[2] not in ('a', 'b', 'c') \
		or p[1] not in ('1', '2', '3') or p[3] not in ('1', '2', '3'):
			raise ValueError('obter_movimento_manual: escolha invalida')
		p_in = cria_posicao(p[0], p[1])
		p_fin = cria_posicao(p[2], p[3])
		adj = ()
		for posi in obter_posicoes_jogador(t, Hpeca):
			adj += obter_posicoes_adjacentes(posi)
		pecas = []
		conta_free = 0
		for pos in adj:
			if pecas_iguais(obter_peca(t, pos), cria_peca(' ')):
				conta_free += 1
		#movimento para a mesma casa 
		if posicoes_iguais(p_in, p_fin) and pecas_iguais(Hpeca, obter_peca(t, p_in)):
			if not eh_posicao(p_in) or not eh_posicao(p_fin) \
			or p_fin not in (obter_posicoes_adjacentes(p_in) + (p_in,)) \
			or conta_free != 0:
				raise ValueError('obter_movimento_manual: escolha invalida')
		#movimento para casa diferente da origem 
		else:
			if not eh_posicao(p_in) or not eh_posicao(p_fin) \
				or not eh_posicao_livre(t, p_fin) \
				or p_fin not in obter_posicoes_adjacentes(p_in) \
				or not pecas_iguais(Hpeca, obter_peca(t, p_in)):
				raise ValueError('obter_movimento_manual: escolha invalida')
		return (p_in, p_fin)

def vitoria(t, AIpeca):
	'''
	Funcao : analisa se ha alguma posicao em que, colocando a peca na mesma, \
	seja possivel obter uma vitoria 
	Recebe : tabuleiro de jogo, peca que representa o computador 
	Devolve : posicao de jogo na qual o computador deve jogar de modo a \
	obter vitoria 
	'''
	#colunas 
	for c in ('a', 'b', 'c'):
		count = 0 
		pos = 0 
		col = obter_vetor(t, c)
		for i in range(len(col)):
			if pecas_iguais(col[i], AIpeca):
				count += 1
			elif pecas_iguais(col[i], cria_peca(' ')):
				pos = cria_posicao(c, str(i + 1))
		if count == 2 and eh_posicao_livre(t, pos): return pos 
	#linhas
	for l in ('1', '2', '3'):
		count = 0 
		pos = 0
		line = obter_vetor(t, l)
		for i in range(len(line)):
			if pecas_iguais(line[i], AIpeca):
				count += 1
			elif pecas_iguais(col[i], cria_peca(' ')):
				pos = cria_posicao(chr(97 + i), l)
		if count == 2 and eh_posicao_livre(t, pos): return pos 

def bloqueio(t, AIpeca, Hpeca):
	'''
	Funcao : analisa se ha alguma posicao em que, colocando a peca na mesma, \
	seja possivel bloquear a vitoria do adversario
	Recebe : tabuleiro de jogo, peca que representa o computador, peca que \
	representa o humano
	Devolve : posicao de jogo na qual o computador deve jogar de modo a \
	impedir a vitoria do humano
	'''
	#colunas 
	for c in ('a', 'b', 'c'):
		count = 0
		pos = 0 
		col = obter_vetor(t, c)
		for i in range(len(col)):
			if pecas_iguais(col[i], Hpeca):
				count += 1
			elif pecas_iguais(col[i], cria_peca(' ')):
				pos = cria_posicao(c, str(i + 1))
		if count == 2 and eh_posicao_livre(t, pos): return pos 
	#linhas
	for l in ('1', '2', '3'):
		count = 0 
		pos = 0
		line = obter_vetor(t, l)
		for i in range(len(line)):
			if pecas_iguais(line[i], Hpeca):
				count += 1
			elif pecas_iguais(col[i], cria_peca(' ')):
				pos = cria_posicao(chr(97 + i), l)
		if count == 2 and eh_posicao_livre(t, pos): return pos

def centro(t):
	'''
	Funcao : verifica se e possivel o computador jogar na posicao central
	Recebe : tabuleiro de jogo
	Devolve : posicao central, caso seja possivel jogar na mesma	
	'''
	centro = obter_vetor(t, 'b')
	if pecas_iguais(centro[1], cria_peca(' ')):
		return cria_posicao('b', '2')

def canto_vazio(t):
	'''
	Funcao : verifica se e possivel o computador jogar em algum dos cantos
	Recebe : tabuleiro de jogo
	Devolve : posicao correspondente a um canto, \
	caso seja possivel jogar na mesma
	'''
	cantos_cima = obter_vetor(t, '1')
	cantos_baixo = obter_vetor(t, '3')
	if pecas_iguais(cantos_cima[0], cria_peca(' ')): return cria_posicao('a', '1')
	if pecas_iguais(cantos_cima[2], cria_peca(' ')): return cria_posicao('c', '1')
	if pecas_iguais(cantos_baixo[0], cria_peca(' ')): return cria_posicao('a', '3')
	if pecas_iguais(cantos_baixo[2], cria_peca(' ')): return cria_posicao('c', '3')			

def lateral_vazio(t):
	'''
	Funcao : verifica se e possivel o computador jogar numa posicao lateral
	Recebe : tabuleiro de jogo
	Devolve : posicao correspondente a uma lateral, \
	caso seja possivel jogar na mesma
	'''
	lateral_vert = obter_vetor(t, 'b')
	lateral_horiz = obter_vetor(t, '2') 
	if pecas_iguais(lateral_vert[0], cria_peca(' ')): return cria_posicao('b', '1')
	if pecas_iguais(lateral_horiz[0], cria_peca(' ')): return cria_posicao('a', '2')	
	if pecas_iguais(lateral_vert[2], cria_peca(' ')): return cria_posicao('b', '3')	
	if pecas_iguais(lateral_horiz[2], cria_peca(' ')): return cria_posicao('c', '2')

def minimax(t, jog_atual, profundidade, seq_movimentos):
	'''
	Funcao : analisa recursivamente todas as possibilidades de jogo \
	(num limite ate n jogadas apos a atual), decidindo qual a melhor posicao \
	na qual jogar num determinado momento, com o objetivo de ganhar o jogo
	Recebe :
		-> tabuleiro de jogo
		-> peca do jogador a que pertence a vez de jogar
		-> alcance maximo de analise do jogo a efetuar pelo computador
		-> tuplo vazio a preencher com uma sequencia de movimentos (posicoes)
	Devolve : 
		-> representacao do tabuleiro contendo a melhor jogada
		-> tuplo contendo a melhor sequencia de movimentos a efetuar consoante \
	o alcance introduzido e tendo em conta a jogada do humano
	'''		
	if not pecas_iguais(obter_ganhador(t), cria_peca(' ')) or profundidade == 0:
		return peca_para_inteiro(obter_ganhador(t)), seq_movimentos
	# definir peca do jogador atual e do adversario 
	if pecas_iguais(jog_atual, cria_peca('X')):
		jog_outro = cria_peca('O')
	else:
		jog_outro = cria_peca('X')	
	melhor_seq_movs = None
	melhor_resultado = peca_para_inteiro(jog_outro)
	# analise da melhor sequencia de movimentos a efetuar :
	for p_jog in obter_posicoes_jogador(t, jog_atual):
		for p_adj in obter_posicoes_adjacentes(p_jog):
			if eh_posicao_livre(t, p_adj):
				novo_t = cria_copia_tabuleiro(t)				
				novo_t = move_peca(novo_t, p_jog, p_adj)
				novo_resultado, nova_seq_movs = minimax(novo_t, jog_outro, profundidade - 1, seq_movimentos + ((p_jog, p_adj),))
				if melhor_seq_movs == None or ((pecas_iguais(jog_atual, cria_peca('X')) 	
					and melhor_resultado < novo_resultado)) \
					or ((pecas_iguais(jog_atual, cria_peca('O')) \
					and melhor_resultado > novo_resultado)):
					melhor_resultado, melhor_seq_movs = novo_resultado, nova_seq_movs
	return melhor_resultado, melhor_seq_movs

def fase_de_colocacao(t, AIpeca, Hpeca):
	'''
	Funcao : escolher a posicao onde o computador deve colocar a peca \
	durante a fase de colocacao
	Recebe : tabuleiro de jogo, peca que representa o computador, peca que \
	representa o humano
	Devolve : posicao de jogo na qual o computador deve jogar consoante a \
	situacao de jogo atual
	'''
	pos = vitoria(t, AIpeca)	
	if eh_posicao(pos) and eh_posicao_livre(t, pos): return (pos,)	
	pos = bloqueio(t, AIpeca, Hpeca)
	if eh_posicao(pos) and eh_posicao_livre(t, pos): return (pos,)
	pos = centro(t)
	if eh_posicao(pos) and eh_posicao_livre(t, pos): return (pos,)
	pos = canto_vazio(t)
	if eh_posicao(pos) and eh_posicao_livre(t, pos): return (pos,)
	pos = lateral_vazio(t)
	if eh_posicao(pos) and eh_posicao_livre(t, pos): return (pos,)

def facil(t, AIpeca, Hpeca):
	'''
	Funcao : permite efetuar as jogadas do computador no nivel de dificuldade \
	facil, tanto na fase de colocacao como na fase de movimento
	Recebe : tabuleiro de jogo, peca que representa o computador, peca que \
	representa o humano
	Devolve : posicao de jogo na qual o computador deve jogar ou movimento \
	que deve efetuar consoante a situacao de jogo atual
	'''
	if eh_fase_de_colocacao(t): 
		return fase_de_colocacao(t, AIpeca, Hpeca)
	else:
		mov_pos = 0 
		for l in ('1', '2', '3'):
			for c in ('a', 'b', 'c'):
				pos = cria_posicao(c, l)
				peca = obter_peca(t, pos)
				if pecas_iguais(peca, AIpeca):
					for mov_pos in obter_posicoes_adjacentes(pos):
						if mov_pos in obter_posicoes_adjacentes(pos) \
							and eh_posicao_livre(t, mov_pos):
							return (pos, mov_pos)
		return (pos, pos)

def normal(t, AIpeca, Hpeca):
	'''
	Funcao : permite efetuar as jogadas do computador no nivel de dificuldade \
	normal, tanto na fase de colocacao como na fase de movimento
	Recebe : tabuleiro de jogo, peca que representa o computador, peca que \
	representa o humano
	Devolve : posicao de jogo na qual o computador deve jogar ou movimento \
	que deve efetuar consoante a situacao de jogo atual
	'''
	if eh_fase_de_colocacao(t):
		return fase_de_colocacao(t, AIpeca, Hpeca)			
	else:
		novo_tabuleiro, melhor_seq_movs = minimax(t, AIpeca, 1, ())
		return melhor_seq_movs[0]

def dificil(t, AIpeca, Hpeca):
	'''
	Funcao : permite efetuar as jogadas do computador no nivel de dificuldade \
	dificil, tanto na fase de colocacao como na fase de movimento
	Recebe : tabuleiro de jogo, peca que representa o computador, peca que \
	representa o humano
	Devolve : posicao de jogo na qual o computador deve jogar ou movimento \
	que deve efetuar consoante a situacao de jogo atual
	'''	
	if eh_fase_de_colocacao(t):
		return fase_de_colocacao(t, AIpeca, Hpeca)
	else:
		novo_tabuleiro, melhor_seq_movs = minimax(t, AIpeca, 5, ())
		return melhor_seq_movs[0]

def obter_movimento_auto(t, AIpeca, dificuldade):
	'''
	Funcao : Representa a jogada do computador no tabuleiro
	Recebe : tabuleiro, peca que representa o computador, string contendo \
	uma das seguintes dificuldades;
		-> 'facil'
		-> 'normal'
		-> 'dificil'
	Devolve : tuplo de posicoes nas quais o computador deve jogar
	'''
	humano = - (peca_para_inteiro(AIpeca))
	# atribuicao da peca :
	if humano == 1: 
		Hpeca = cria_peca('X')
	else:
		Hpeca = cria_peca('O')
	if dificuldade == 'facil':
		return facil(t, AIpeca, Hpeca) #retorna uma posicao
	if dificuldade == 'normal':
		return normal(t, AIpeca, Hpeca)
	if dificuldade == 'dificil':
		return dificil(t, AIpeca, Hpeca)


#-------------------------------------------------------------------------------------#
#                                     FUNCAO PRINCIPAL                                #
#-------------------------------------------------------------------------------------#

def moinho(jogadorH, dificuldade):
	'''
	Funcao : Permite jogar um jogo completo do moinho contra o computador 
	Recebe : string que representa a peca que o jogador humano deseja utilizar, \
	string contendo a dificuldade com que o humano deseja que o computador jogue;
		-> 'facil'
		-> 'normal'
		-> 'dificil'
	Devolve - string contendo a representacao da peca do jogador vencedor
	'''
	t = cria_tabuleiro()
	print('Bem-vindo ao JOGO DO MOINHO. Nivel de dificuldade ' + dificuldade + '.')
	print(tabuleiro_para_str(t))

	if jogadorH not in ('[X]', '[O]') \
		or dificuldade not in ('facil', 'normal', 'dificil'):
		raise ValueError('moinho: argumentos invalidos')
	# AIpeca - peca correspondente ao computador , Hpeca - peca correspondente ao humano
	if jogadorH == '[X]':
		pecaAI = cria_peca('O')
		pecaH = cria_peca('X')
		turnoAI = False
	else:
		pecaAI = cria_peca('X')
		pecaH = cria_peca('O')
		turnoAI = True	
	t_pos = 0 
	while pecas_iguais(obter_ganhador(t), cria_peca(' ')):		
		if turnoAI:
			#turno do computador
			print('Turno do computador ('+ dificuldade + '):')			
			t_pos = obter_movimento_auto(t, pecaAI, dificuldade)		
			if eh_fase_de_colocacao(t):
				t = coloca_peca(t, pecaAI, t_pos[0])
			else:
				t = move_peca(t, t_pos[0], t_pos[1])
			print(tabuleiro_para_str(t))
			if pecas_iguais(obter_ganhador(t), pecaAI):
				return peca_para_str(pecaAI)
		else:
			#turno do jogador			
			if eh_fase_de_colocacao(t):
				t_pos = obter_movimento_manual(t, pecaH)
				t = coloca_peca(t, pecaH, t_pos[0])
			else:
				t_pos = obter_movimento_manual(t, pecaH)
				t = move_peca(t, t_pos[0], t_pos[1])
			print(tabuleiro_para_str(t))
			if pecas_iguais(obter_ganhador(t), pecaH):
				return peca_para_str(pecaH)
		#mudanca de turno
		turnoAI = not turnoAI
