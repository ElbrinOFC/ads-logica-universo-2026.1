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