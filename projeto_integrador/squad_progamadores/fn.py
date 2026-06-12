# ================================================================
# SISTEMA DE ANÁLISE FINANCEIRA INTEGRADO (PROJETO 5 ALUNOS)
# ================================================================

# --- ALUNO 1 HENRIQUE : ENTRADA E VALIDAÇÃO DOS DADOS ---
class InterfaceValidada:
    @staticmethod
    def entrada_dados():
        print("\n" + "-"*30)
        print("📥 INSERÇÃO DE DADOS")
        print("-"*30)
        try:
            d = {}
            d['ano'] = int(input("Ano"))
            d['ac'] = float(input("Ativo Circulante: "))
            d['ai'] = float(input("Ativo Não Circulante (Imobilizado): "))
            d['pc'] = float(input("Passivo Circulante: "))
            d['pnc'] = float(input("Passivo Não Circulante: "))
            d['pl'] = float(input("Patrimônio Líquido: "))
            d['rl'] = float(input("Receita Líquida: "))
            d['lb'] = float(input("Lucro Bruto: "))
            d['ll'] = float(input("Lucro Líquido: "))
            d['caixa'] = float(input("Disponibilidades (Caixa): "))
            d['estoques'] = float(input("Estoques: "))

            ativo = d['ac'] + d['ai']
            passivo_total = d['pc'] + d['pnc'] + d['pl']

            # Validação Crítica (Aluno 1 HENRIQUE)
            if abs(ativo - passivo_total) > 0.1:
                print(f"\n❌ ERRO: Balanço não fecha! Ativo({ativo}) != Passivo+PL({passivo_total})")
                return None
            return d
        except ValueError:
            print("\n❌ ERRO: Entrada inválida. Use apenas números.")
            return None

# --- ALUNO 2 CAMILA : MOTOR ANALÍTICO (FÓRMULAS) ---
class MotorAnalitico:
    @staticmethod
    def calcular_todos(df):
        # Liquidez
        df.indices['LC'] = df.ac / df.pc if df.pc > 0 else 0
        df.indices['LS'] = (df.ac - df.estoques) / df.pc if df.pc > 0 else 0
        df.indices['LI'] = df.caixa / df.pc if df.pc > 0 else 0
        # Endividamento
        df.indices['EG'] = (df.pc + df.pnc) / df.ativo_total if df.ativo_total > 0 else 0
        # Rentabilidade
        df.indices['ROE'] = df.ll / df.pl if df.pl != 0 else 0
        df.indices['ML'] = df.ll / df.rl if df.rl > 0 else 0

# --- ALUNO 3 GABRIEL: POO CONTÁBIL & GESTÃO DE HISTÓRICO ---
class DemonstracaoFinanceira:
    def __init__(self, dados):
        self.ano = dados['ano']
        self.ac = dados['ac']
        self.ai = dados['ai']
        self.pc = dados['pc']
        self.pnc = dados['pnc']
        self.pl = dados['pl']
        self.rl = dados['rl']
        self.lb = dados['lb']
        self.ll = dados['ll']
        self.caixa = dados['caixa']
        self.estoques = dados['estoques']
        self.ativo_total = self.ac + self.ai
        self.passivo_terceiros = self.pc + self.pnc
        self.indices = {}
        self.analise_v = {} # Para o (Aluno 5 REGIS )

class GerenciadorEmpresa:
    def __init__(self):
        self.historico = [] # Vetor de 5 anos (Aluno 3 GABRIEL)

    def adicionar_ano(self, df):
        if len(self.historico) >= 5:
            self.historico.pop(0)
        self.historico.append(df)
        self.historico.sort(key=lambda x: x.ano)

# --- ALUNO 4 LORENA: ANÁLISE DE TENDÊNCIAS (HORIZONTAL) ---
class AnalisadorTendencias:
    @staticmethod
    def comparar_evolucao(historico):
        if len(historico) < 2:
            return
        print("\n" + "=" * 60)
        print("📈 ANÁLISE HORIZONTAL (EVOLUÇÃO)".center(60))
        print("=" * 60)
        atual, anterior = historico[-1], historico[-2]
        
        contas = [("Receita", atual.rl, anterior.rl), ("Lucro", atual.ll, anterior.ll), 
                  ("Ativo", atual.ativo_total, anterior.ativo_total)]

        for nome, at, ant in contas:
            var = ((at - ant) / abs(ant)) * 100 if ant != 0 else 0
            status = "🟢 [SUBIU]" if var > 0 else "🔴 [CAIU]" if var < 0 else "⚪ [ESTÁVEL]"
            print(f"{nome:<15} | {var:>10.2f}% | {status}")

# --- ALUNO 5 REGIS: ANÁLISE VERTICAL & SCORE DE SAÚDE ---
class DiagnosticoAvancado:
    @staticmethod
    def calcular_vertical(df):
        # Proporção de ativos e margens (Aluno 5 REGIS)
        df.analise_v['Margem_Bruta'] = (df.lb / df.rl) if df.rl > 0 else 0
        df.analise_v['Peso_Estoque'] = (df.estoques / df.ativo_total) if df.ativo_total > 0 else 0

    @staticmethod
    def score_saude(df):
        score = 0
        if df.indices['LC'] >= 1.5: score += 2
        if df.indices['ROE'] >= 0.10: score += 2
        if df.indices['EG'] <= 0.5: score += 2
        
        print(f"\n⭐ SCORE DE SAÚDE FINANCEIRA: {score}/6")
        if score >= 5: print("Status: EXCELENTE")
        elif score >= 3: print("Status: SATISFATÓRIO")
        else: print("Status: ALERTA CRÍTICO")

# --- DASHBOARD FINAL (INTEGRAÇÃO) TODOS PODEM FALAR SOBRE O DASBHORD INTELIGENTE ---
class Dashboard:
    @staticmethod
    def exibir(historico):
        print("\n" + "█" * 100)
        print("📊 RELATÓRIO CONSOLIDADO".center(100))
        print("█" * 100)
        
        headers = ["ANO", "L. CORRENTE", "L. SECA", "ENDIVID.", "ROE%", "MARGEM%"]
        print(" | ".join(h.center(15) for h in headers))
        print("-" * 100)

        for d in historico:
            row = [str(d.ano), f"{d.indices['LC']:.2f}", f"{d.indices['LS']:.2f}", 
                   f"{d.indices['EG']:.2f}", f"{d.indices['ROE']*100:.1f}%", 
                   f"{d.indices['ML']*100:.1f}%"]
            print(" | ".join(v.center(15) for v in row))

# --- MAIN ---
def main():
    empresa = GerenciadorEmpresa()
    while True:
        print("\n1. Inserir Dados")
        print("2. Gerar Dashboard e Análises")
        print("3. Sair")
        op = input("Escolha: ")

        if op == "1":
            dados = InterfaceValidada.entrada_dados()
            if dados:
                df = DemonstracaoFinanceira(dados)
                MotorAnalitico.calcular_todos(df)     # Aluno 2 CAMILA
                DiagnosticoAvancado.calcular_vertical(df) # Aluno 5 REGIS
                empresa.adicionar_ano(df)            # Aluno 3 GABRIEL 
                print("\n✔ Dados Processados e Salvos!")

        elif op == "2":
            if not empresa.historico:
                print("Sem dados cadastrados.")
                continue
            
            Dashboard.exibir(empresa.historico)
            AnalisadorTendencias.comparar_evolucao(empresa.historico) # Aluno 4 LORENA
            DiagnosticoAvancado.score_saude(empresa.historico[-1])    # Aluno 5 REGIS
            
        elif op == "3":
            print("Encerrando sistema...")
            break

if __name__ == "__main__":
    main()
