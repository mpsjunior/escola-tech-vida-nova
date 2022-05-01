programa
{
	funcao inicio()
	{
		
		inteiro candidato_a = 0, candidato_b = 0
		inteiro brancos = 0, nulos = 0, total_votos = 0
		inteiro porcentagem_candidato_a, porcentagem_candidato_b
		inteiro porcentagem_brancos, porcentagem_nulos
		inteiro voto
		
		faca
		{
			limpa()
			escreva("Escolha seu candidato ou tecle zero para encerrar\n\n")
			escreva("  1 -> Candidato A\n")
			escreva("  2 -> Candidato B\n")
			escreva("  3 -> Branco\n")
			escreva("\nQualquer número diferente de 0, 1, 2 e 3 anulará o seu voto\n")
			escreva("Digite seu voto: ")
			leia(voto)
			limpa()

			escolha (voto)
			{
				caso 0: 
					escreva ("Votação encerrada!\n")
				pare
				
				caso 1: 
			 		candidato_a = candidato_a + 1 
			 	pare
			 	
			 	caso 2: 
			 		candidato_b = candidato_b + 1 
			 	pare
			 	
			 	caso 3: 
			 		brancos = brancos + 1 
			 	pare
			 	
			 	caso contrario:
			 		nulos = nulos + 1 
				}			 
				}
				enquanto(voto != 0)
				total_votos = candidato_a + candidato_b + brancos + nulos		
				se (total_votos > 0)
				{
					porcentagem_candidato_a = (candidato_a * 100.0) / total_votos  
					porcentagem_candidato_b = (candidato_b * 100.0) / total_votos
					porcentagem_brancos = (brancos * 100.0) / total_votos
					porcentagem_nulos = (nulos * 100.0) / total_votos
					
					
					escreva("\nporcentagem candidato_a: ",porcentagem_candidato_a,"%")			
					escreva("\nporcentagem candidato_b: ",porcentagem_candidato_b,"%")
					escreva("\nporcentagem brancos:",porcentagem_brancos,"%")
					escreva("\nporcentagem nulos:",porcentagem_nulos,"%")

					se (candidato_a > candidato_b)
					escreva("\n------*** Candidato A Ganhou a Eleição ***------")
									
					se (candidato_b > candidato_a)
					escreva("\n------*** Candidato B Ganhou a Eleição ***------")
					
					se (candidato_a == candidato_b)
					escreva("\n------------*** Ninguem Ganhou ***--------------")
					
					
		}
				}
		}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 1903; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */