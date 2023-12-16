# Variável para armazenar a quantidade de experiência (XP) do herói
xp = 7500  # Exemplo de XP

# Estrutura de decisão para determinar o nível com base na XP
if xp < 1000:
    nivel = "Ferro"
elif 1001 <= xp <= 2000:
    nivel = "Bronze"
elif 2001 <= xp <= 5000:
    nivel = "Prata"
elif 5001 <= xp <= 6000:
    nivel = "Ouro"
elif 6001 <= xp <= 7000:
    nivel = "Platina Diamante"
elif 7001 <= xp <= 8000:
    nivel = "Ascendente"
elif 8001 <= xp <= 10000:
    nivel = "Imortal"
else:
    nivel = "Radiante"

# Saída com a mensagem final exibindo o nome do herói e o nível
nome = "Zeus"
print(f"O Herói de nome {nome} está no nível de {nivel}.")