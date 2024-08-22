from assets.conto_nosso_povo_cap_1_ptbr_ticuna import portugues
from assets.conto_nosso_povo_cap_1_ptbr_ticuna import ticuna

def traduz_conto_ticuna_pro_portugues(texto_portugues,texto_ticuna):
    conto_portugues = texto_portugues.split('\n')
    conto_ticuna = texto_ticuna.split('\n')

    traducao = ""
  
    for frase_ticuna in conto_ticuna:
        indice = frase_ticuna[:2]  
        texto_ticuna = frase_ticuna[3:]  
    
        for frase_portugues in conto_portugues:
            if frase_portugues.startswith(indice) and indice != '':
                texto_portugues = frase_portugues[3:]  
                traducao += f"{texto_portugues}\n{texto_ticuna}\n\n"
                break
    
    traducao.strip()

    print(traducao)

traduz_conto_ticuna_pro_portugues(portugues,ticuna)