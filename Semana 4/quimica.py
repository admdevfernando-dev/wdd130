from formula import interpretar_formula

NOME_INDICE = 0
MASSA_ATOMICA_INDICE = 1


def criar_tabela_periodica():
  
    dic_da_tabela_periodica = {
        # símbolo: [nome, massa atomica]
        "Ac": ["Actínio", 227],
        "Ag": ["Prata", 107.8682],
        "Al": ["Alumínio", 26.9815386],
        "Am": ["Amerício", 243],
        "Ar": ["Argônio", 39.948],
        "As": ["Arsênio", 74.9216],
        "At": ["Astato", 210],
        "Au": ["Ouro", 196.966569],
        "B": ["Boro", 10.811],
        "Ba": ["Bário", 137.327],
        "Be": ["Berílio", 9.012182],
        "Bh": ["Bóhrio", 272],
        "Bi": ["Bismuto", 208.9804],
        "Bk": ["Berquélio", 247],
        "Br": ["Bromo", 79.904],
        "C": ["Carbono", 12.0107],
        "Ca": ["Cálcio", 40.078],
        "Cd": ["Cádmio", 112.411],
        "Ce": ["Cério", 140.116],
        "Cf": ["Califórnio", 251],
        "Cl": ["Cloro", 35.453],
        "Cm": ["Cúrio", 247],
        "Cn": ["Copernício", 285],
        "Co": ["Cobalto", 58.933195],
        "Cr": ["Crômio", 51.9961],
        "Cs": ["Césio", 132.9054519],
        "Cu": ["Cobre", 63.546],
        "Db": ["Dúbnio", 268],
        "Ds": ["Darmstádio", 281],
        "Dy": ["Disprósio", 162.5],
        "Er": ["Érbio", 167.259],
        "Es": ["Einstênio", 252],
        "Eu": ["Európio", 151.964],
        "F": ["Flúor", 18.9984032],
        "Fe": ["Ferro", 55.845],
        "Fl": ["Fleróvio", 289],
        "Fm": ["Férmio", 257],
        "Fr": ["Frâncio", 223],
        "Ga": ["Gálio", 69.723],
        "Gd": ["Gadolínio", 157.25],
        "Ge": ["Germânio", 72.64],
        "H": ["Hidrogênio", 1.00794],
        "He": ["Hélio", 4.002602],
        "Hf": ["Háfnio", 178.49],
        "Hg": ["Mercúrio", 200.59],
        "Ho": ["Hólmio", 164.93032],
        "Hs": ["Hássio", 270],
        "I": ["Iodo", 126.90447],
        "In": ["Índio", 114.818],
        "Ir": ["Irídio", 192.217],
        "K": ["Potássio", 39.0983],
        "Kr": ["Kriptônio", 83.798],
        "La": ["Lantânio", 138.90547],
        "Li": ["Lítio", 6.941],
        "Lr": ["Laurêncio", 262],
        "Lu": ["Lutécio", 174.9668],
        "Lv": ["Livermório", 293],
        "Md": ["Mendelévio", 258],
        "Mg": ["Magnésio", 24.305],
        "Mn": ["Manganês", 54.938045],
        "Mo": ["Molibdênio", 95.96],
        "Mt": ["Meitnério", 276],
        "N": ["Nitrogênio", 14.0067],
        "Na": ["Sódio", 22.98976928],
        "Nb": ["Nióbio", 92.90638],
        "Nd": ["Neodímio", 144.242],
        "Ne": ["Neônio", 20.1797],
        "Nh": ["Nihônio", 286],
        "Ni": ["Níquel", 58.6934],
        "No": ["Nobélio", 259],
        "Np": ["Neptúnio", 237],
        "O": ["Oxigênio", 15.9994],
        "Og": ["Oganessônio", 294],
        "Os": ["Ósmio", 190.23],
        "P": ["Fósforo", 30.973762],
        "Pa": ["Protactínio", 231.03588],
        "Pb": ["Chumbo", 207.2],
        "Pd": ["Paládio", 106.42],
        "Pm": ["Promécio", 145],
        "Po": ["Polônio", 209],
        "Pr": ["Praseodímio", 140.90765],
        "Pt": ["Platina", 195.084],
        "Pu": ["Plutônio", 244],
        "Ra": ["Rádio", 226],
        "Rb": ["Rubídio", 85.4678],
        "Re": ["Rênio", 186.207],
        "Rf": ["Rutherfórdio", 267],
        "Rg": ["Roentgênio", 280],
        "Rh": ["Ródio", 102.9055],
        "Rn": ["Radônio", 222],
        "Ru": ["Rutênio", 101.07],
        "S": ["Enxofre", 32.065],
        "Sb": ["Antimônio", 121.76],
        "Sc": ["Escândio", 44.955912],
        "Se": ["Selênio", 78.96],
        "Sg": ["Seabórgio", 271],
        "Si": ["Silício", 28.0855],
        "Sm": ["Samário", 150.36],
        "Sn": ["Estanho", 118.71],
        "Sr": ["Estrôncio", 87.62],
        "Ta": ["Tântalo", 180.94788],
        "Tb": ["Térbio", 158.92535],
        "Tc": ["Tecnécio", 98],
        "Te": ["Telúrio", 127.6],
        "Th": ["Tório", 232.03806],
        "Ti": ["Titânio", 47.867],
        "Tl": ["Tálio", 204.3833],
        "Tm": ["Túlio", 168.93421],
        "Ts": ["Tenessino", 294],
        "U": ["Urânio", 238.02891],
        "V": ["Vanádio", 50.9415],
        "W": ["Tungstênio", 183.84],
        "Xe": ["Xenônio", 131.293],
        "Y": ["Ítrio", 88.90585],
        "Yb": ["Itérbio", 173.054],
        "Zn": ["Zinco", 65.38],
        "Zr": ["Zircônio", 91.224],
    }
    return dic_da_tabela_periodica


def calcular_massa_molar(lista_quantidade_simbolos, dic_da_tabela_periodica):
   
    massa_molar_total = 0

    for simbolo, quantidade in lista_quantidade_simbolos:
        massa_atomica = dic_da_tabela_periodica[simbolo][MASSA_ATOMICA_INDICE]
        massa_molar_total += massa_atomica * quantidade

    return massa_molar_total


def main():
    formula = input("Digite a fórmula química do composto (ex: H2O): ")
    massa_da_amostra = float(input("Digite a quantidade do composto em gramas: "))

    dic_da_tabela_periodica = criar_tabela_periodica()
    lista_quantidade_simbolos = interpretar_formula(formula, dic_da_tabela_periodica)

    massa_molar = calcular_massa_molar(lista_quantidade_simbolos, dic_da_tabela_periodica)
    print(f"A massa molar de {formula} é {massa_molar:.4f} g/mol")

    numero_mols = massa_da_amostra / massa_molar
    print(f"O número de mols em {massa_da_amostra} g de {formula} é {numero_mols:.4f} mols")


if __name__ == "__main__":
    main()