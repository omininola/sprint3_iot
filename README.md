# Sprint 03 | IoT

## Integrantes

| Nome |  RM  |
| ---- | :--: |
| Otavio Miklos Nogueira | 554513 |
| Luciayla Yumi Kawakami | 557987 |
| João Pedro Amorim Brito | 559213 |

## Links
Youtube: 

## Rodando

### Requisitos

- Docker & Docker Compose
- Postman | Insomnia
- WebCam

### Comandos

```bash
# Clone o projeto
git clone https://github.com/omininola/sprint3_iot

# Mude o diretório
cd sprint3_iot/project

# Rode o Docker Compose
docker compose up -d --build
```

Na primeira vez subindo os containers, pode ser que demore um pouco, pois é necessário que as imagens do MySQL e MongoDB sejam instaladas. E que os serviços do Server (Java API), Client (React) e Tag Recognition (Python) sejam buildados.

### Problemas

#### Acesso da câmera

O Docker Compose precisa que a WebCam seja passada para dentro do container, no linux isso é feito facilmente com a seguinte opção no Docker Compose

```yml
devices:
  - /dev:/dev
```

Porém se o seu sistema for Windows ou Mac, essa tarefa pode não ser tão simples assim. Pois o Windows utiliza uma VM para rodar os containers do Docker, então a VM teria que ter acesso a WebCam também.  

#### Portas

Pode ser que dê algum problema na hora de rodar os containers, caso isso ocorra, cheque se já existe algum recurso rodando em alguma das portas:
- 8080
- 5000
- 3000

Se houver, você pode alterar o Docker Compose para mapear para outras portas

### Testes

Para iniciar os testes, teremos que criar alguns recursos

#### Filial

#### Pátio

#### Tags

#### Motos

## Limpar a Máquina

```bash
# Remover as Imagens do MySQL, MongoDB, Java, Python e Node

# Remover as Networks criadas

# Remover os Volumes
```