'''
Classes identificadas : Cliente, Conta

Observações:
    Não estou registrando operações mal-sucedidas no extrato (i.e. se não é possível sacar, a tentativa não fica registrada)
    Não estou verificando input - assumi usuário ideal

'''

class Cliente():
    
    def __init__(self, nome = "", telefone = 0) -> None:
        self.__nome = nome;
        self.__telefone = telefone;
        
    def getNome(self):
        return self.__nome;
        
    def getTelefone(self):
        return self.__telefone;
        
    def setNome(self, nome = ""):
        if (nome == ""):
            return False;
            
        self.__nome = nome;
        
    def setTelefone(self, telefone = 0):
        if (telefone == 0):
            return False;
        
        self.__telefone = telefone;
        
    def __str__(self) -> str:
        return f"{self.__nome}";
        
        
class Conta():
    
    # CONSTANTES
    
    RENDIMENTO = 0.05; 
    
    TIPOS = ("Corrente", "Poupança", "Especial");
    
    TIPO_CORRENTE = 0;
    TIPO_POUPANCA = 1;
    TIPO_ESPECIAL = 2;
    
    LIMITE_CONTA_ESPECIAL = -1000;
    
    OPS = ("Saque", "Depósito", "Rendimento");
    
    OP_SAQUE = 0;
    OP_DEPOSITO = 1;
    OP_RENDIMENTO = 2;
    
    # METODOS
    
    def __init__(self, saldo = 0, historico = list(), clientes = list(), tipo = TIPO_CORRENTE) -> None:
        self.__saldo = saldo;
        self.__historico = historico;
        self.__clientes = clientes;
        self.__tipo = tipo;
        
    def getSaldo(self):
        return self.__saldo;
        
    def getHistorico(self):
        return self.__historico;
        
    def getClientes(self):
        return self.__clientes;
        
    def getTipo(self):
        return self.__tipo;
    
    def setSaldo(self, saldo):
        self.__saldo = saldo;
        
    def setHistorico(self, historico = list()):
        if len(historico) == 0:
            return False;
        
        self.__historico = historico;
        
    def setClientes(self, clientes = list()):
        if len(clientes) == 0:
            return False;
        
        self.__clientes = clientes;
        
    def setTipo(self, tipo = TIPO_CORRENTE):
        if 0 <= tipo <= len(Conta.TIPOS):
            return False;
            
        self.__tipo = tipo;
        
    # Apenas montando uma string, transformei em método pois usei essa mesma lógica 3 vezes
    
    def strToExtrato(nome, op, valor):
        return nome + "-" + op + ": " + str(valor);
    
    # Logica especifica
    
    def monthTick(self):
        if self.__tipo == Conta.TIPO_POUPANCA:
            rendeu = self.__saldo * Conta.RENDIMENTO;
            self.__saldo = self.__saldo + rendeu;
            strHistorico = Conta.strToExtrato("(Poupança)", Conta.OPS[Conta.OP_RENDIMENTO], rendeu);
            self.__historico.append(strHistorico);
        else:
            print("Não é conta poupança.");
    
    def sacar(self, valor = 0, cliente = Cliente()):
        
        tempSaldo = self.__saldo;
        
        tempSaldo -= valor;
        
        if (cliente not in self.__clientes):
            print("Não é tutelar da conta.")
            return False;
        
        if (tempSaldo < Conta.LIMITE_CONTA_ESPECIAL):
            print("Ultrapassou limite de saldo negativo.");
            return False;
        
        else:
            if (tempSaldo < 0) and not (self.__tipo == Conta.TIPO_ESPECIAL):
                print("Saldo negativo em conta não-especial.");
                return False;
                
            else:
                self.__saldo = tempSaldo;
                strHistorico = Conta.strToExtrato(cliente.getNome(), Conta.OPS[Conta.OP_SAQUE], valor);
                self.__historico.append(strHistorico);
                
    def depositar(self, valor = 0, cliente = Cliente()):
        
        if (cliente not in self.__clientes):
            print("Não é titular.");
            return False;
            
        self.__saldo += valor;
        strHistorico = Conta.strToExtrato(cliente.getNome(), Conta.OPS[Conta.OP_DEPOSITO], valor);
        self.__historico.append(strHistorico);
        
    def __str__(self) -> str:
        gambiarra = "";
        for c in self.__clientes:
            gambiarra += c.getNome() + "; ";
        return f"Conta(Saldo: {self.__saldo}, Titulares: {gambiarra}, Tipo: {Conta.TIPOS[self.__tipo]})";
        

def easyDebug():
    
    cliente1 = Cliente("Primus", 11111111);
    cliente2 = Cliente("Secundus", 22222222);
    cliente3 = Cliente("Tertius", 33333333);
    cliente4 = Cliente("Quartus", 44444444);
    
    contaCorrente = Conta(200, [], [cliente1, cliente2], Conta.TIPO_CORRENTE);
    contaPoupanca = Conta(1000, [], [cliente3, cliente4], Conta.TIPO_POUPANCA);
    contaEspecial = Conta(300, [], [cliente4], Conta.TIPO_ESPECIAL);
    
    contaCorrente.sacar(100, cliente1);
    print(contaCorrente.getHistorico());
    
    contaCorrente.sacar(100, cliente2);
    print(contaCorrente.getHistorico());
    
    contaCorrente.sacar(100, cliente3);
    
    contaPoupanca.monthTick();
    contaCorrente.monthTick();
    
    contaPoupanca.depositar(300, cliente3);
    print(contaPoupanca.getHistorico());
    
    contaEspecial.sacar(1000, cliente2);
    contaEspecial.sacar(1400, cliente4);
    contaEspecial.sacar(1300, cliente4);
    
    print(contaEspecial.getHistorico());
    print(contaEspecial.getSaldo());
    
    print(cliente1);
    
def main():
    
    # Listas principais
    listaContas = list();
    listaClientes = list();
    
    # Debug
    listaClientes.append(Cliente("Primus", 11111111));
    listaClientes.append(Cliente("Secundus", 22222222));
    
    listaContas.append(Conta(1000, [], [listaClientes[0], listaClientes[1]], Conta.TIPO_CORRENTE));
    # Coisas do menu
    menu = True;
    
    def printMenu():
        
        print("-"*16);
        print("Escolha: ");
        print("[0] Adcionar cliente");
        print("[1] Adcionar conta");
        print("[2] Informações");
        print("[3] Sacar");
        print("[4] Depositar");
        print("[5] Passar o mês");
        print("[6] Sair");
        
        return input();
    
    while menu:
        
        opcao = int(printMenu());
        
        temClientes = len(listaClientes) > 0; # calculando aqui pois uso mais de uma vez
        
        if (opcao == 0): # Add cliente
            
            print("Nome(str) e telefone(int), separados por ;");
            nome, telefone = input().split(";");
            listaClientes.append(Cliente(nome, telefone));
            
        elif (opcao == 1 and temClientes): # Add conta
            
            print("Clientes disponiveis: ");
            for i, c in enumerate(listaClientes):
                print(f"[{i}] {c.getNome()}");
            
            print("Tipos de contas: ");
            for j, t in enumerate(Conta.TIPOS):
                print(f"[{j}] {Conta.TIPOS[j]}");
                
            print("Digite os clientes e o tipo de conta, separados por ;");
            print("Ex: 1 2 3;2");
            titularesStr, tipo = input().split(";");
            
            tipo = int(tipo);
            titulares = list();
            for n in titularesStr.split():
                titulares.append(listaClientes[int(n)]);
            
            listaContas.append(Conta(0, [], titulares, tipo));
            
        elif (opcao == 1): # Add conta
            
            print("Não há clientes para serem titulares de uma conta.");
        
        elif (opcao == 2 and temClientes and len(listaContas) > 0): # Infos
            
            print("Se identifique:");
            for i, c in enumerate(listaClientes):
                print(f"[{i}] {c.getNome()}");
                    
            clienteId = listaClientes[int(input())];
            
            print("Sobre qual conta quer info?");
            for i, co in enumerate(listaContas):
                if (clienteId in co.getClientes()):
                    clStr = "";
                    for cl in co.getClientes():
                        clStr += cl.getNome() + "; ";
                    print(f"[{i}] {Conta.TIPOS[co.getTipo()]} ( {clStr})");
            
            contaId = int(input());
            
            print(listaContas[contaId]);
            print("Extrato: ");
            print(listaContas[contaId].getHistorico());
            
        
        elif (opcao == 2): # Infos
            
            print("Nao há contas ou nao há clientes");
        
        elif (opcao == 3): # Sacar
            
            print("Escolha a conta:");
            for i, co in enumerate(listaContas):
                print(f"[{i}] {co}");
            contaId = int(input());
            
            print("Digite o valor: ");
            valor = float(input());
            
            print("Qual cliente realizou o saque?");
            for j, cl in enumerate(listaClientes):
                if (cl in listaContas[contaId].getClientes()):
                    print(f"{j} {cl.getNome()}");
            clienteId = int(input());
            
            listaContas[contaId].sacar(valor, listaClientes[clienteId]);
            
            
        elif (opcao == 4): # Depositar
        
            print("Escolha a conta:");
            for i, co in enumerate(listaContas):
                print(f"[{i}] {co}");
            contaId = int(input());
            
            print("Digite o valor: ");
            valor = float(input());
            
            print("Qual cliente realizou o deposito?");
            for j, cl in enumerate(listaClientes):
                if (cl in listaContas[contaId].getClientes()):
                    print(f"[{j}] {cl.getNome()}");
            clienteId = int(input());
            
            listaContas[contaId].depositar(valor, listaClientes[clienteId]);
        
        elif (opcao == 5):
            
            i = 0;
            for co in listaContas:
                if (co.getTipo() == Conta.TIPO_POUPANCA):
                    co.monthTick();
                    i += 1;
            
            print(f"{i} contas renderam.");
            
        elif (opcao == 6): # Sair
            
            menu = False;
    
       
#easyDebug(); 
main();



