# Chatbot de eSports

## Objetivo

Este projeto tem como objetivo desenvolver um chatbot capaz de responder perguntas relacionadas ao universo dos eSports. O sistema foi projetado para interpretar perguntas em linguagem natural e gerar respostas sobre jogos competitivos, times, jogadores, campeonatos, regras, cenários competitivos e outros temas ligados ao ecossistema de esportes eletrônicos.

A aplicação utiliza **Python 3.11.9** como linguagem principal e a **API Google Gemini 2.5 Flash** como motor de geração de respostas. O foco do projeto é oferecer respostas rápidas, diretas e escaláveis, com uma base técnica simples de manter e expandir.

## Tecnologias Utilizadas

- **Linguagem:** Python 3.11.9
- **Modelo de IA:** Google Gemini 2.5 Flash
- **Gerenciador de dependências:** pip
- **Ambiente virtual:** venv
- **Interface de execução:** terminal, podendo ser expandida para web futuramente

## Funcionalidades

- Receber perguntas em linguagem natural;
- Processar perguntas relacionadas a eSports;
- Gerar respostas com apoio de modelo de linguagem;
- Permitir expansão para novas categorias e fontes de dados;
- Servir como base para futuras integrações com APIs externas e interfaces gráficas.

## Estrutura do Projeto

Exemplo de organização:

```bash
esports-chatbot/
├── src/
│   ├── main.py
│   ├── chatbot.py
│   ├── config.py
│   └── prompts.py
├── .env
├── requirements.txt
└── README.md