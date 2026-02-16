# src/interface/cli/presenters.py
"""
Presenters - Formatam DTOs para exibição no terminal.
"""

from typing import List, Dict
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich import box
from src.interface.console import console
from src.domain.value_objects.tipo_documento import TipoDocumento


class DocumentoPresenter:
    """Formata documentos para exibição."""
    
    @staticmethod
    def badge_tipo(tipo: str) -> str:
        """Retorna badge colorido para tipo."""
        try:
            tipo_enum = TipoDocumento(tipo)
            return f"[{tipo_enum.icone} {tipo_enum.descricao_pt}]"
        except:
            return "[dim]📄 Documento[/dim]"
    
    @staticmethod
    def badge_idioma(idioma: str) -> str:
        """Retorna badge de idioma."""
        badges = {
            'ru': '[bold white]🇷🇺 RU[/bold white]',
            'en': '[bold blue]🇺🇸 EN[/bold blue]',
            'pt': '[bold green]🇧🇷 PT[/bold green]',
        }
        return badges.get(idioma, f'[dim]{idioma}[/dim]')
    

    @classmethod
    def tabela_documentos(cls, resultados: Dict):
        """Cria tabela de documentos para listagem."""
        table = Table(
            title=f"[bold]📚 Documentos[/bold] (Página {resultados['pagina']}/{resultados['total_paginas']})",
            box=box.ROUNDED,
            header_style="bold cyan",
            border_style="bright_blue"
        )
        
        table.add_column("ID", width=4, justify="right")
        table.add_column("Tipo", width=20)
        table.add_column("Data", width=12)
        table.add_column("Pessoa", width=25)
        table.add_column("Título", width=35)
        table.add_column("🌐", width=8, justify="center")
        
        for item in resultados['items']:
            # Badge de tradução baseado no campo tem_traducao
            if item.tem_traducao:
                trad_badge = "[bold green]✓[/bold green]"
            else:
                trad_badge = "[dim]—[/dim]"
            
            table.add_row(
                str(item.id),
                cls.badge_tipo(item.tipo),
                item.data_original or "N/D",
                item.pessoa_principal_en or item.pessoa_principal or "",
                item.titulo[:35] + "…" if len(item.titulo) > 35 else item.titulo,
                trad_badge
            )
        
        console.print(table)
        console.print(f"[dim]Total: {resultados['total']} documentos[/dim]")

    @classmethod
    def documento_completo(cls, dto):
        """Exibe documento completo com metadados e traduções."""
        # Cabeçalho com título
        titulo_panel = Panel(
            f"[bold yellow]{dto.titulo}[/bold yellow]\n\n"
            f"{cls.badge_tipo(dto.tipo)}",
            border_style="bright_green",
            padding=(1, 2)
        )
        console.print(titulo_panel)
        console.print()
        
        # Metadados
        console.print("[bold cyan]📋 METADADOS[/bold cyan]")
        console.print(f"  🏛️  Centro: [yellow]{dto.centro}[/yellow]")
        console.print(f"  📅 Data original: {dto.data_original or 'Não informada'}")
        console.print(f"  🔗 URL: [blue]{dto.url}[/blue]")
        console.print(f"  📊 Tamanho: {dto.tamanho_caracteres} caracteres")
        console.print(f"  📝 Palavras: {dto.tamanho_palavras} palavras")
        
        if dto.pessoa_principal:
            nome = dto.pessoa_principal_en or dto.pessoa_principal
            console.print(f"  👤 Pessoa principal: {nome}")
        
        if dto.remetente:
            console.print(f"  ✉️  Remetente: {dto.remetente}")
        
        if dto.destinatario:
            console.print(f"  📨 Destinatário: {dto.destinatario}")
        
        if dto.envolvidos:
            console.print(f"  ⚖️  Envolvidos: {', '.join(dto.envolvidos)}")
        
        if dto.tem_anexos:
            console.print("  [green]📎 Possui anexos[/green]")
        
        # MOSTRAR TRADUÇÕES DISPONÍVEIS
        if hasattr(dto, 'traducoes') and dto.traducoes:
            console.print("\n[bold cyan]🌐 TRADUÇÕES DISPONÍVEIS:[/bold cyan]")
            for trad in dto.traducoes:
                # Formatar data (pegar só a parte da data)
                data_trad = trad['data_traducao'][:10] if trad['data_traducao'] else 'data desconhecida'
                console.print(f"  • {cls.badge_idioma(trad['idioma'])} - {data_trad}")
            
            # Instrução para ver tradução
            console.print("\n[dim]Digite 't' durante a visualização para alternar entre traduções[/dim]")
        
        console.print()
        
        # Conteúdo
        console.print("[bold white]📄 CONTEÚDO[/bold white]")
        console.print("─" * 80)
        
        texto = dto.texto
        if len(texto) > 2000:
            texto = texto[:2000] + "\n\n[dim]... (texto truncado, use exportar para completo)[/dim]"
        
        console.print(texto)
        console.print("─" * 80)
        

    @classmethod
    def estatisticas(cls, stats):
        """Exibe estatísticas completas."""
        console.print("[bold cyan]📊 ESTATÍSTICAS DO ACERVO[/bold cyan]")
        console.print()
        
        # Visão geral
        console.print(Panel.fit(
            f"[bold]📚 Documentos: {stats.total_documentos}[/bold]   "
            f"[bold]🌐 Traduções: {stats.total_traducoes}[/bold]",
            border_style="blue"
        ))
        console.print()
        
        # Por centro
        if stats.documentos_por_centro:
            console.print("[bold]🏛️  Por centro:[/bold]")
            for centro, total in stats.documentos_por_centro.items():
                nome = "Leningrad" if centro == "lencenter" else "Moscow"
                console.print(f"  • {nome}: {total}")
            console.print()
        
        # Por tipo
        if stats.documentos_por_tipo:
            console.print("[bold]📋 Por tipo:[/bold]")
            for tipo, total in stats.documentos_por_tipo.items():
                console.print(f"  • {cls.badge_tipo(tipo)}: {total}")
            console.print()
        
        # Pessoas frequentes
        if stats.pessoas_frequentes:
            console.print("[bold]👤 Pessoas mais frequentes:[/bold]")
            for nome_ru, total, nome_en in stats.pessoas_frequentes[:10]:
                console.print(f"  • {nome_en} [dim]({nome_ru})[/dim]: {total}")
            console.print()