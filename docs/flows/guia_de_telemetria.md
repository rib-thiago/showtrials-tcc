# Guia de Telemetria do Projeto

## Objetivo

Este guia descreve o padrao tecnico predominante de instrumentacao e testes de telemetria observado no projeto.

Seu objetivo e:

- preservar consistencia entre modulos que usam telemetria
- manter baixo acoplamento e fallback seguro quando a instrumentacao nao estiver configurada
- apoiar implementacao, revisao e teste de mudancas que toquem observabilidade

## Contexto de Uso

A telemetria tem lastro real no codigo e nos testes do projeto.

Ela aparece em modulos de dominio, casos de uso, factories e repositorios, e costuma seguir um padrao baseado em:

- variavel `_telemetry`
- configuracao explicita
- chamadas condicionais a `increment(...)`
- testes especificos `test_*_telemetry.py`

Este guia deve ser lido como referencia tecnica especifica, complementar ao protocolo de qualidade, ao guia de auto-revisao e ao guia de debug.

## Principios da Instrumentacao

- telemetria deve ser opcional
- o codigo nao deve quebrar quando ela estiver desabilitada
- a instrumentacao deve ser testavel
- nomes de contadores devem permanecer consistentes
- a implementacao nao deve aumentar acoplamento desnecessario

Exemplo do padrao predominante:

```python
if _telemetry:
    _telemetry.increment("modulo.operacao.status")
```

## Padrao Tecnico de Implementacao

O padrao predominante no projeto inclui:

- variavel `_telemetry = None`
- funcao `configure_telemetry(...)`
- chamadas protegidas por `if _telemetry:`
- uso de `increment(...)` para registrar eventos e contadores

Exemplo-base:

```python
_telemetry = None

def configure_telemetry(telemetry_instance=None):
    global _telemetry
    _telemetry = telemetry_instance
```

Na maior parte dos casos observados, esse bloco aparece proximo ao topo do modulo. Alguns arquivos podem combinar telemetria com mecanismos auxiliares adicionais, como decoradores ou monitoramento complementar, sem invalidar o padrao principal.

## Padrao de Nomenclatura dos Contadores

Estrutura base:

```
modulo.submodulo.operacao.estado
```

| Parte | Descrição | Exemplo |
|-------|-----------|---------|
| **modulo** | Domínio principal | `exportar_documento` |
| **submodulo** | (opcional) Subdivisão | `buscar_documento` |
| **operacao** | Ação sendo executada | `executar` |
| **estado** | Resultado/status | `iniciado`, `concluido`, `erro.tipo` |

Exemplos observados no projeto:

```python
_telemetry.increment("exportar_documento.executar.iniciado")
_telemetry.increment("exportar_documento.executar.formato.txt")
_telemetry.increment("exportar_documento.executar.sucesso_txt")
_telemetry.increment("exportar_documento.erro.formato_invalido")

_telemetry.increment("gerar_relatorio.coletar_dados.iniciado")
_telemetry.increment("gerar_relatorio.documentos_processados", value=len(documentos))
_telemetry.increment("gerar_relatorio.salvar.sucesso_txt")
```

## Testes de Telemetria

O padrao predominante de testes inclui:

- arquivo `test_*_telemetry.py`
- import do modulo como `uc_module` ou equivalente
- `setup_method` zerando `_telemetry`
- uso de mock para validar chamadas a `increment(...)`
- caso em que telemetria esta desabilitada e nada quebra

Exemplo-base:

```python
class TestMeuModuloTelemetry:
    def setup_method(self):
        uc_module._telemetry = None

    def test_telemetria_sucesso(self):
        mock_telemetry = MagicMock()
        uc_module.configure_telemetry(telemetry_instance=mock_telemetry)
        mock_telemetry.increment.assert_any_call("modulo.metodo.iniciado")
```

Os testes reais do projeto mostram que esse padrao esta efetivamente em uso.

## Erros Comuns e Cuidados

| Erro | Causa | Solução |
|------|-------|---------|
| `AttributeError: 'NoneType' object has no attribute 'increment'` | Esqueceu de verificar `if _telemetry:` | Adicionar `if _telemetry:` antes de usar |
| Testes de telemetria falham com chamadas não encontradas | Mock não configurado ou caminho diferente | Use `assert_any_call` em vez de `assert_called_with` |
| `_telemetry` persistindo entre testes | Não zerou no `setup_method` | Adicionar `uc_module._telemetry = None` |
| Contadores com nomes inconsistentes | Não seguiu o padrão | Use `modulo.operacao.estado` |

## Pendencias e Validacoes Necessarias

- alguns modulos combinam telemetria com mecanismos auxiliares adicionais, como decoradores ou variaveis complementares, entao o guia nao deve ser lido como se toda base seguisse uma unica assinatura exata sem variacao
- os exemplos historicos ligados a fases antigas ajudam a rastrear origem do padrao, mas nao devem ser tratados como unica forma valida de instrumentacao
- em etapa posterior, vale revisar se ha padroes divergentes de `configure_telemetry(...)` que precisem de consolidacao mais formal

## Documentos Relacionados

- [Protocolo de Qualidade do Projeto](protocolo_de_qualidade.md)
- [Guia de Auto-Revisao antes de PR e Merge](guia_de_auto_revisao.md)
- [Guia de Debug do Projeto](guia_de_debug.md)
- [Automacao Operacional com Taskipy](automacao_operacional_com_taskipy.md)
