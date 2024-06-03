def menuInicial():
    print('DIGITE 1 PARA CADASTRAR UM PRODUTO.')
    print('DIGITE 2 PARA ALTERAR UM PRODUTO.')
    print('DIGITE 3 PARA EXCLUIR UM PRODUTO.')
    print('DIGITE 4 PARA LISTAR OS PRODUTOS.')
    print('DIGITE OUTRO NÚMERO PARA SAIR.')
    menu = int(input('DIGITE O NÚMERO: '))
    return menu

def criptografiaDescriptografia(palavra, x):
    # Lista com as lestras de 'A' a 'Z'
    T = ['Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']
    #Lista com os numeros das letras da palavra digitada
    I = [T.index(c) for c in palavra if c in T]
    #Caso a palavra seja impar, adiciona um 0 extra
    if len(I) % 2 != 0:
        I.append(0)
    #Cria os vetores na matriz inicial
    num_cols = 2
    P = [I[i:i+num_cols] for i in range(0, len(I), num_cols)]
    if x == 1:
        A = ([[11, 13], [2, 3]])
    else:
        A = ([[45, -195], [-30, 165]])
    #Mutiplicação da Matriz da palavra e da de criptografia
    vetor = []
    matriz = []
    for d in range(len(P)):
        for k in range(len(A)):
            for c in range(len(P[d])):
                B = A[k][c]*P[d][c]
                vetor.append(B)
                if len(vetor) > 1:
                    matriz.append(sum(vetor))
                    vetor = []
    for i in range(len(matriz)):
        if matriz[i] > 26:
            matriz[i] = matriz[i] % 26
        elif matriz[i] < 0:
            while matriz[i] < 0:
                matriz[i] = matriz[i] + 26
    #Cria vetores na matriz resultante
    num_cols = 2
    vetores = [matriz[i:i+num_cols] for i in range(0, len(matriz), num_cols)]
    #Transforma os numeros em letras novamente
    TC = []
    for col in vetores:
            for c in col:
                TC.append(T[c])
    if len(palavra) % 2 != 0:
        ul = len(TC)-1
        del(TC[ul])
    texto = ''.join(TC)
    return texto

import getpass
import oracledb

pw = getpass.getpass("Digite a senha: ")

try:
    conexao = oracledb.connect(
    user="Priscila2",
    password = pw,
    dsn="localhost/xepdb1")
except Exception as erro:
    print("Erro em conexao", erro)
else:
    print("Conectado", conexao.version)

cursor = conexao.cursor()
tabela = []
resultado = []

menu = menuInicial()
while menu > 0 and menu < 5:
    if menu == 1:
        print(' '*7,'='*40)
        print(' '*7,'|   PROGRAMA PARA CADASTRAR PRODUTOS   |')
        print(' '*7,'='*40)

        cod_do_produto = int(input('\nDigite o código do produto: '))
        nome_do_produto = str(input('\nDigite o nome do produto: '))
        desc_do_produto = str(input('\nDigite a descrição do produto: '))
        custo_do_produto = float(input('\nDigite o custo de aquisição (Fornecedor): '))
        custo_fixo = float(input('\nDigite o custo fixo do produto/administrativo em %: '))
        comissao_de_venda = float(input('\nDigite a comissão de venda em %: '))
        imposto_sobre_venda = float(input('\nDigite o imposto sobre venda em %: '))
        margem_de_lucro = float(input('\nDigite a margem de lucro em %: '))
        nome_do_produtoCripto = criptografiaDescriptografia(nome_do_produto.upper(), 1)
        desc_do_produtoCripto = criptografiaDescriptografia(desc_do_produto.upper(), 1)

        cursor.execute(f"INSERT INTO PRODUTOS VALUES ({cod_do_produto},'{nome_do_produtoCripto}', '{desc_do_produtoCripto}',{custo_do_produto},{custo_fixo},{comissao_de_venda},{imposto_sobre_venda},{margem_de_lucro})")
        cursor.execute("commit")

        # Cálculo do preço de venda
        preco_de_venda = (((custo_fixo)/100) + ((comissao_de_venda)/100) + ((imposto_sobre_venda)/100) + ((margem_de_lucro)/100)/(100/100))
        if preco_de_venda >= 1:
            print('\nOps...A soma das porcentagens não pode ultrapassar ou ser igual a 100%. Tente novamente com outros valores.')
            print('')
            continue
                
        preco_de_venda_final = custo_do_produto / (1 - preco_de_venda)


        # calculo da receita bruta pv - cp
        receita_bruta = preco_de_venda_final - custo_do_produto

        # regra de 3 custo do produto para %
        CP = 100 * custo_do_produto / preco_de_venda_final

        # calculo da receita bruta para %
        RB = 100 - CP

        # regra de 3 do custo fixo
        CF = preco_de_venda_final * custo_fixo / 100

        # regra de 3 da comissão de venda
        CV = preco_de_venda_final * comissao_de_venda / 100

        # regra de 3 do imposto sobre a venda
        IV = preco_de_venda_final * imposto_sobre_venda / 100

        # calculo dos outros custos
        outros_custos = CF + CV + IV

        # outros custos em %
        OC = custo_fixo + comissao_de_venda + imposto_sobre_venda

        # calculo da rentabilidade 
        R = receita_bruta - outros_custos

        # calculo da rentabilidade em %
        RP = RB - OC

        print('')
        print('-'*60)
        print(f'{"TABELA DE VALORES":^60}')
        print('-'*60)
        print(f'{'Descrição':<40}{'Valor':^10}{'%':>10}')
        print(f'{'Preço de Venda:':<40}{preco_de_venda_final:^10.2f}{CP+RB:>10.2f}%')
        print(f'{'Custo de aquisição (Fornecedor):':<40}{custo_do_produto:^10.2f}{CP:>10.2f}%')
        print(f'{'Receita Bruta:':<40}{receita_bruta:^10.2f}{RB:>10.2f}%')
        print(f'{'Custo Fixo/Administrativo:':<40}{CF:^10.2f}{custo_fixo:>10.2f}%')
        print(f'{'Comissão de Vendas:':<40}{CV:^10.2f}{comissao_de_venda:>10.2f}%')
        print(f'{'Impostos:':<40}{IV:^10.2f}{imposto_sobre_venda:>10.2f}%')
        print(f'{'Outros custos:':<40}{outros_custos:^10.2f}{OC:>10.2f}%')
        print(f'{'Rentabilidade:':<40}{R:^10.2f}{RP:>10.2f}%')
        print('-'*60)

            
        if margem_de_lucro > 20:
            print(f'LUCRO ALTO: {margem_de_lucro}% de lucro')
        elif margem_de_lucro > 10 :
            print(f'LUCRO MÉDIO: {margem_de_lucro}% de lucro')
        elif margem_de_lucro > 0:
            print(f'LUCRO BAIXO: {margem_de_lucro}% de lucro')
        elif margem_de_lucro == 0:
            print(f'EQUILÍBRIO: {margem_de_lucro}% de lucro')
        elif margem_de_lucro < 0:
            print(f'PREJUÍZO: {margem_de_lucro}% de lucro')
        print('-'*60)
        cont = int(input('Digite 1 para adicionar outro produto, ou digite qualquer outro numero para ir para o menu: '))
        if cont == 1:
            menu = 1
        else:
            menu = menuInicial()
    elif menu == 2:
        cod = int(input('Digite o codigo do produto que deseja alterar: '))
        coluna = input('Digite a coluna que deseja alterar: ')
        if coluna == 'nome' or coluna == 'descricao':
            valorNovo = input('Digite o novo valor: ')
            valorNovoCripto = criptografiaDescriptografia(valorNovo.upper(),1)
            cursor.execute(f"UPDATE PRODUTOS set {coluna} = '{valorNovoCripto}' WHERE cod_prod = {cod}")
            cursor.execute("commit")
        elif coluna == 'cod_prod' or coluna == 'custo_prod' or coluna == 'custo_fixo' or coluna == 'comissao_de_venda' or coluna == 'impostos' or coluna == 'rentabilidade':
            valorNovo = input('Digite o novo valor: ')
            cursor.execute(f"UPDATE PRODUTOS set {coluna} = {valorNovo} WHERE cod_prod = {cod}")
            cursor.execute("commit")
        print('PRONTO!')
        cont = int(input('Digite 1 para alterar outro produto, ou digite qualquer outro numero para ir para o menu: '))
        if cont == 1:
            menu = 2
        else:
            menu = menuInicial()
    elif menu == 3:
        cod = int(input('Digite o codigo do produto que deseja excluir: '))
        cursor.execute(f"DELETE FROM PRODUTOS WHERE COD_PROD = {cod}")
        cursor.execute("commit")
        print('PRONTO')
        cont = int(input('Digite 1 para excluir outro produto, ou digite qualquer outro numero para ir para o menu: '))
        if cont == 1:
            menu = 3
        else:
            menu = menuInicial()
    elif menu == 4:
        # Salvar dados da tabela do Oracle no Python
        tabela = []
        resultado = []
        print(' '*7,'='*60)
        cursor.execute("select * from PRODUTOS order by cod_prod")
        for k in range(len(cursor.fetchall())):
            cursor.execute("select * from PRODUTOS order by cod_prod")
            for c in range(len(cursor.fetchall()[k])):
                cursor.execute("select * from PRODUTOS order by cod_prod")
                if c == 1 or c == 2:
                    nomeDescripto = criptografiaDescriptografia((cursor.fetchall()[k][c]).upper(),2)
                    resultado.append(nomeDescripto)
                else:
                    resultado.append(cursor.fetchall()[k][c])
            tabela.append(resultado)
            resultado = []

        # Printar dados na tela

        for p in range(len(tabela)):
            print(F'PRODUTO {p + 1}')
            nome = tabela[p][1]
            desc = tabela[p][2]
            print(nome.upper())
            print(desc.upper())
            for r in range(8):
                if r == 0:
                    pv = (((tabela[p][4])/100) + (((tabela[p][5]))/100) + (((tabela[p][6]))/100) + (((tabela[p][7]))/100)/(100/100))
                    pvf = (tabela[p][3]) / (1 - pv)
                    print(f'Preço de venda: R${pvf:.2f}     100%')
                elif r == 1:
                    print(f'Custo de Aquisição: R${tabela[p][3]:.2f}{(tabela[p][3]/pvf)*100:.2f}%')
                elif r == 2:
                    rb = pvf - tabela[p][3]
                    print(f'Receita Bruta: R${rb:<15.2f}{(rb/pvf)*100:.2f}%')
                elif r == 3:
                    print(f'Custo Fixo:  R${(tabela[p][4]/100)*pvf:.2f}    {tabela[p][4]}%')
                elif r == 4:
                    print(f'Comissão de vendas: R${(tabela[p][5]/100)*pvf:.2f}     {tabela[p][5]}%')
                elif r == 5:
                    print(f'Impostos: R${(tabela[p][6]/100)*pvf:.2f}     {tabela[p][6]}%')
                elif r == 6:
                    og = tabela[p][4] + tabela[p][5] + tabela[p][6]
                    print(f'Outros Custos: R${og/100*pvf:.2f}     {og}%')
                else:
                    print(f'Rentabilidade: R${tabela[p][7]/100*pvf:.2f}     {tabela[p][7]}%')

            # Calculo do lucro dos produtos

            if tabela[p][7] > 20:
                print(f'LUCRO ALTO: {tabela[p][7]}% de lucro')
            elif tabela[p][7] > 10 :
                    print(f'LUCRO MÉDIO: {tabela[p][7]}% de lucro')
            elif tabela[p][7] > 0:
                print(f'LUCRO BAIXO: {tabela[p][7]}% de lucro')
            elif tabela[p][7] == 0:
                print(f'EQUILÍBRIO: {tabela[p][7]}% de lucro')
            elif tabela[p][7] < 0:
                print(f'PREJUÍZO: {tabela[p][7]}% de lucro')
            print(' '*7,'='*60)
        cont = int(input('Digite qualquer numero para ir para o menu: '))
        menu = menuInicial()
cursor.close()
conexao.close()
