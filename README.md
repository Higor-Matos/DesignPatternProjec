# DesignPatternProject

## :page_with_curl: Sobre o Projeto
Este projeto utiliza o padrão Singleton para gerenciar conexões com a API da Wikipedia e o padrão Factory Method para a criação específica de buscadores. Ele integra esses padrões com o Flask, oferecendo uma interface web eficiente e modular para buscas na Wikipedia.

## :computer: Tecnologias Utilizadas
- **Singleton e Factory Method**: Para eficiência e modularidade no design.
- **Flask**: Como framework web.
- **Docker**: Para dockerização do projeto.
- **GitHub Actions & AWS ECR**: Para CI/CD.

<img align="center" alt="Python logo" src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen">
<img align="center" alt="Docker logo" src="https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white">
<img align="center" alt="AWS" src="https://img.shields.io/badge/amazonaws-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white"> 
<img align="center" alt="githubactions" src="https://img.shields.io/badge/githubactions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white"> 

## :whale: Executando o Projeto com Docker
Para executar o projeto, use os seguintes comandos Docker:

```bash
docker build -t designpatternproject .
docker run -p 5000:5000 designpatternproject
```
Acesse a aplicação em `http://localhost:5000`.

## :framed_picture: Demonstração e Estrutura do Projeto
### **Demonstração Mobile**
<p align="center">
  <img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExeWRtdmc3ZHgzcmh5bXo5emEzanFsZXZtZ3B0MGN3aGg4am55cnJ4aSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/zg2HCjKV9Hrff6LOwa/giphy.gif">
</p>

### **Estrutura do Projeto**
<p align="center">
  <img src="https://i.imgur.com/3Blit0q.png">
</p>

### **CI/CD**
<p align="center">
  <img src="https://i.imgur.com/1Zr422Q.png">
</p>

## :heavy_check_mark: Benefícios dos Padrões Utilizados
- **Singleton**: Reduz o overhead de conexões múltiplas e garante consistência.
- **Factory Method**: Flexibilidade na criação de buscadores e facilita a expansão.

