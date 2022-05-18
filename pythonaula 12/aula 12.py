nome = str(input("qual seu nome: "))
if nome == "osmar":
    print("bom dia! osmar.")
elif nome == 'pedro':
    print('nome bonito')
elif nome == "gabi":
    print('nome da minha filha')
elif nome == 'joao' or nome=='jose' or nome== 'chico':
    print('sao nomes comuns do nordeste')
elif nome in 'helio zeus poseidon':
    print('nome de deus.')
else:
    print("nome comum")
print('tenha um bom dia! {}'.format(nome))