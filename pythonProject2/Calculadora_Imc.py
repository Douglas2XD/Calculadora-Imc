import customtkinter as ctk
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

#VERIFICA O IMC E RETORNA O VALOR.
def verificar_imc(imc,medida_valor):
    if imc < 16.9:
        return medida_valor.configure(janela, text=f"SEU IMC: {imc} MUITO ABAIXO DO PESO", text_color='#ff1100')
    elif imc > 16.9 and imc < 18.4:
        return medida_valor.configure(janela, text=f"SEU IMC: {imc} ABAIXO DO PESO", text_color='#ff7063')
    elif imc > 18.4 and imc < 25.9:
        return medida_valor.configure(janela, text=f"SEU IMC: {imc} PESO NORMAL", text_color='#147a00')
    elif imc > 25 and imc < 29.9:
        return medida_valor.configure(janela, text=f"SEU IMC: {imc} ACIMA DO PESO", text_color='#ff7063')
    else:
        return medida_valor.configure(janela, text=f"SEU IMC: {imc} OBESO", text_color='#ff1100')

#CALCULO DO IMC
def calc_imc(peso,altura):
    return  peso / (altura * 2)

#AQUI CHAMA AS FUNÇÕES E EXIBE O CONTEÚDO
def calcular(peso_entry,altura_entry,medida_valor):
    peso = peso_entry.get()
    altura = altura_entry.get()

    #VERIFICA SE SÃO NULOS
    if not peso or not altura:
        medida_valor.configure(text="VAZIO, POR FAVOR INSIRA UM DADO", text_color="red")
        return

    if not "," in altura or not"," in altura:
        altura = altura[0] + "." + altura[1::]
        

    peso = peso.replace(",", ".")
    altura = altura.replace(",", ".")

    try:
        peso_formatado = float(peso)
        altura_formatado = float(altura)
    except ValueError:
        medida_valor.configure(text="VALORES INVÁLIDOS", text_color="red")
        return

    imcc = calc_imc(peso_formatado, altura_formatado)
    imc = round(imcc, 2)

    verificar_imc(imc, medida_valor)

#JANELA PRINCIPAL ONDE OCORRE TUDO.
def janela():
    janela = ctk.CTk()
    janela.geometry('500x300')
    janela.title('Calculadora de IMC')


    ctk.CTkLabel(janela, text='PESO (kg): ').pack()
    peso = ctk.CTkEntry(janela, width=120,height=30)
    peso.pack()

    ctk.CTkLabel(janela, text='ALTURA (m ou cm): ').pack()
    altura = ctk.CTkEntry(janela, width=120,height=30)
    altura.pack()

    medida = ctk.CTkLabel(janela, text="SUA MEDIDA: ")
    medida_valor = ctk.CTkLabel(janela, text="")


    button = ctk.CTkButton(janela, text='Calcular',width=120,height=30,command=lambda:calcular(peso,altura,medida_valor))
    button.pack(padx=10, pady=10)


    medida.pack()
    medida_valor.pack()

    janela.mainloop()

#MAIN CHAMANDO TUDO.
def main():
    janela()

main()

