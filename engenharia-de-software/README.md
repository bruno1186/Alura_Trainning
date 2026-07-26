# Engenharia de Software

Princípios, práticas e processos que sustentam a construção de software de qualidade em times de qualquer tamanho.

## Princípios de design: SOLID

- **S — Single Responsibility:** cada módulo deve ter um único motivo para mudar.
- **O — Open/Closed:** aberto para extensão, fechado para modificação — novas funcionalidades via extensão, não alterando código existente e testado.
- **L — Liskov Substitution:** subtipos devem poder substituir seus tipos base sem quebrar o comportamento esperado.
- **I — Interface Segregation:** interfaces pequenas e específicas são melhores que uma interface genérica e grande.
- **D — Dependency Inversion:** dependa de abstrações, não de implementações concretas.

## Clean Code

Código limpo é escrito para ser lido por humanos, não apenas executado por máquinas. Nomes que revelam intenção, funções pequenas e com um único propósito, ausência de efeitos colaterais escondidos, e comentários que explicam o "porquê" (não o "o quê") são a base de um código de fácil manutenção.

## Ciclo de vida de desenvolvimento

1. Levantamento e refinamento de requisitos.
2. Design técnico (quando a complexidade justifica).
3. Implementação com testes automatizados.
4. Revisão de código (code review).
5. Integração contínua e entrega contínua (CI/CD).
6. Observação em produção (monitoramento, logs, métricas).

## Versionamento e colaboração

Git é o padrão de mercado para controle de versão. Boas práticas incluem: commits pequenos e atômicos, mensagens de commit descritivas, uso de branches de curta duração, e Pull Requests como unidade de revisão e conhecimento compartilhado. Trunk-based development e Git Flow são duas estratégias de branching com trade-offs diferentes entre velocidade de integração e isolamento de mudanças.

## Integração e entrega contínuas (CI/CD)

CI garante que cada mudança seja validada automaticamente (build, testes, lint) antes de ser integrada. CD estende esse conceito até a entrega (ou implantação) em produção de forma automatizada e confiável, reduzindo o risco de cada release através de frequência alta e mudanças pequenas.

## Exemplo prático

Um exemplo real de API construída com esses princípios (camadas separadas, testes automatizados, CI configurado) está disponível no repositório [backend-api](https://github.com/bruno1186/backend-api), com NestJS, TypeScript e Swagger/OpenAPI.

## Boas práticas

- Escrever testes antes ou junto com o código de produção, nunca só depois "se sobrar tempo".
- Automatizar tudo que for repetitivo: build, testes, lint, deploy.
- Priorizar código simples e legível sobre soluções "espertas" e difíceis de manter.
