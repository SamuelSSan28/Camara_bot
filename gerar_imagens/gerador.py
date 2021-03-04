from PIL import Image, ImageDraw, ImageFont

def gerar_imagens(projetos, vereadores_dict):
    paths = []
    for projeto in projetos:
        #print(projeto)
        n = 40
        dados_aux = []
        dados_aux.append(projeto["titulo"][:n])
        projeto["titulo"] = projeto["titulo"][n:]
        while len(projeto["titulo"][n:]) > n:
            dados_aux.append(projeto["titulo"][:n])
            projeto["titulo"] = projeto["titulo"][n:]
        dados_aux.append(projeto["titulo"])

        img = Image.open('gerar_imagens/background.jpg')

        
        fnt1 = ImageFont.truetype("C:\Windows\Fonts\Candara.ttf", 25)
        fnt2 = ImageFont.truetype("C:\Windows\Fonts\Arial.ttf", 25)

        d = ImageDraw.Draw(img)

        color = 'rgb(0, 0, 0)'

        #linha1
        d.text((20,20), 'Autor(es) da Proposição: ' + str(vereadores_dict[projeto["vereador"]]["nome"]) ,  font=fnt1, fill=color)
        d.text((500,20), "Protocolo: Nº " + str(projeto["protocolo"]) , font=fnt1, fill=color)

        #linha2
        d.text((20,60), "Data: " + str(projeto["data"]) , font=fnt1, fill=color)
        d.text((500,60), "Setor: " + str(projeto["setor"]), font=fnt1, fill=color)

        #linha3
        d.text((20,100), "Fase: " + str(projeto["fase"]) , font=fnt1, fill=color)
        d.text((500,100), "Situação: " + str(projeto["situacao"]) , font=fnt1, fill=color)


        k = 300

        for dado in dados_aux:
            d.text((40,k), dado, align="left", font=fnt2, fill=color)
            k += 25
        
        img_path = 'images/img_proj_' + str(projeto["processo"][:3] + '.jpeg') 
        img.save('./gerar_imagens/'+ img_path)
    
        paths.append(img_path+",legenda @galerinhadomal" + "\n") #mandar as informações para a legende

    arquivo = open('./gerar_imagens/paths.txt', 'w')
    arquivo.writelines(paths)
    arquivo.close()