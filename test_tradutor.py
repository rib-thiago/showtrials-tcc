# test_tradutor.py
from translator import criar_tradutor_da_configuracao

def main():
    print("🔍 Testando conexão com Google Translate API...")
    
    tradutor = criar_tradutor_da_configuracao()
    
    if not tradutor:
        print("❌ Falha na configuração")
        return
    
    if tradutor.testar_conexao():
        print("\n📝 Testando tradução russo → inglês...")
        
        texto_teste = "Здравствуйте, это тестовое сообщение."
        resultado = tradutor.traduzir(texto_teste, destino='en')
        
        print(f"   Original: {resultado.texto_original}")
        print(f"   Tradução: {resultado.texto_traduzido}")
        print(f"   Idioma detectado: {resultado.idioma_origem}")
        print(f"   Custo estimado: ${resultado.custo_estimado:.6f}")
        
        print("\n✅ Teste concluído com sucesso!")
    else:
        print("❌ Falha no teste de conexão")

if __name__ == "__main__":
    main()