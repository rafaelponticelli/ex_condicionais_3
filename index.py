loop = 0

while (loop < 1):
#entradas de dados
  
    nome = (input("Digite Seu Nome :"))

    matematica = float(input("Digite a Sua Nota em MATEMATICA :"))

    portugues = float(input("Digite a Sua Nota em PORTUGUES :"))

    historia = float(input("Digite SuaNota em HISTÓRIA :"))

    
 #frmula de soma de media 
    media = (matematica + portugues) + historia
 #apresentação do resutado

    print(nome,"Suas Notas Foram")
    print("\nMatematica    :",matematica ,
          "\nPortugues     :",portugues ,
          "\nHistoria      :",historia,
          "\nSua Media Foi :",media)
    
    
    