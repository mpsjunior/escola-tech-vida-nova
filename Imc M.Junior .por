programa {
	funcao inicio() {
		real imc
		caracter sexo
		inteiro qtd_jov = 0, qtd_adu = 0, qtd_exp = 0, qtd_hom = 0, qtd_mul = 0, total = 0, continua
		real peso, somas_peso[5] = {0.0, 0.0, 0.0, 0.0, 0.0}
		real altura, somas_altura[5] = {0.0, 0.0, 0.0, 0.0, 0.0}
		inteiro idade, somas_idade[5] = {0, 0, 0, 0, 0}
		real soma_peso_jov, soma_peso_adu, soma_peso_exp, soma_peso_hom, soma_peso_mul
 		real soma_altura_jov, soma_altura_adu, soma_altura_exp, soma_altura_hom, soma_altura_mul
 		inteiro soma_idade_jov, soma_idade_adu, soma_idade_exp, soma_idade_hom, soma_idade_mul
	   
        
        faca {
            escreva("Qual a sua idade?\n")
            leia(idade)
            se (idade < 18){ 
		  escreva("Você precisa ter mais de 18 para a pesquisa!\n")	
		  }
            
            escreva("Qual a sua altura?\n")
            leia(altura)
            
            escreva("Qual o seu peso?\n")
            leia(peso)
            
            escreva("Qual o seu sexo?\nDigite [F] para feminino e [M] para masculino\n")
            leia(sexo)
            
            imc = peso/(altura * altura)
            
            se(imc >= 18.5 e imc <= 24.9){
            	escreva("Você está dentro do peso!\n\n")
            } senao se (imc >= 25.0) {
            	escreva("Você está acima do peso!\n\n")
            } senao {
            	escreva("Você está abaixo do peso!\n\n")
            }
            
            escreva("Você deseja entrevistar mais uma pessoa?\nDigite 1 se sim e 0 se não.\n")
            leia(continua)
            
            total++
            
            escolha(sexo){
                caso 'f':
                    qtd_mul++
                    somas_peso[4]+=peso
                    somas_altura[4]+=altura
                    somas_idade[4]+=idade
                    pare
                
                caso 'm':
                    qtd_hom++
                    somas_peso[3]+=peso
                    somas_altura[3]+=altura
                    somas_idade[3]+=idade
                    pare
                
                caso contrario:
                    escreva("Você digitou o sexo errado\n")
            }
            
            se (idade >= 18 e idade <= 32){
                qtd_jov++
                somas_peso[0]+=peso
                somas_altura[0]+=altura
                somas_idade[0]+=idade
                
            } senao se (idade >= 33 e idade <= 61){
                qtd_adu++
                somas_peso[1]+=peso
                somas_altura[1]+=altura
                somas_idade[1]+=idade
                
            } senao se (idade > 61) {
                qtd_exp++
                somas_peso[2]+=peso
                somas_altura[2]+=altura
                somas_idade[2]+=idade
            } senao {
                escreva("Pessoas menores de 18 anos não podem participar da pesquisa :(\n")
            }
        } enquanto (continua == 1)
        
        escreva("----------------------------------------------\n")
        escreva("----------  MÉDIAS DOS ENTREVISTADOS  --------\n")
        escreva("----------------------------------------------\n")
        escreva("---------- *** GRUPO DE MULHERES *** ---------\n")
        escreva("------------ MÉDIA DE IDADE: ", somas_idade[4]/qtd_mul ,"---------------\n")
        escreva("------------ MÉDIA DE PESO: ", somas_peso[4]/qtd_mul ,"----------------\n")
        escreva("------------ MÉDIA DE ALTURA: ", somas_altura[4]/qtd_mul ,"--------------\n")
        escreva("----------------------------------------------\n")
        escreva("---------- *** GRUPO DE HOMENS *** -----------\n")
        escreva("------------ MÉDIA DE IDADE: ", somas_idade[3]/qtd_hom ,"---------------\n")
        escreva("------------ MÉDIA DE PESO: ", somas_peso[3]/qtd_hom ,"----------------\n")
        escreva("------------ MÉDIA DE ALTURA: ", somas_altura[3]/qtd_hom ,"--------------\n")
        escreva("----------------------------------------------\n")
        escreva("----------------------------------------------\n")
        escreva("---------- *** GRUPO DE JOVENS *** -----------\n")
        escreva("------------ MÉDIA DE IDADE: ", somas_idade[0]/qtd_jov ,"---------------\n")
        escreva("------------ MÉDIA DE PESO: ", somas_peso[0]/qtd_jov ,"----------------\n")
        escreva("------------ MÉDIA DE ALTURA: ", somas_altura[0]/qtd_jov ,"--------------\n")
        escreva("--------------------------------------------\n")
        escreva("---------- *** GRUPO DE ADULTOS *** -----------\n")
        escreva("------------ MÉDIA DE IDADE: ", somas_idade[1]/qtd_adu ,"---------------\n")
        escreva("------------ MÉDIA DE PESO: ", somas_peso[1]/qtd_adu ,"----------------\n")
        escreva("------------ MÉDIA DE ALTURA: ", somas_altura[1]/qtd_adu ,"--------------\n")
        escreva("--------------------------------------------\n")
        escreva("-------- *** GRUPO DE EXPERTS *** ---------\n")
        escreva("------------ MÉDIA DE IDADE: ", somas_idade[2]/qtd_exp ,"---------------\n")
        escreva("------------ MÉDIA DE PESO: ", somas_peso[2]/qtd_exp ,"----------------\n")
        escreva("------------ MÉDIA DE ALTURA: ", somas_altura[2]/qtd_exp ,"--------------\n")
        escreva("--------------------------------------------\n")
	}
}

/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 5195; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */