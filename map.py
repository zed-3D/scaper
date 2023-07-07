a_escadarias = [
    ['#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', '#'],
    ['#', 'O', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#']
]

mapa_escritorio = [
    ['#', '#', '#', '#', '#'],
    ['#', ' ', 'O', ' ', '#'],
    ['#', ' ', '#', ' ', '#'],
    ['#', ' ', 'X', ' ', '#'],
    ['#', '#', '#', '#', '#']
]

mapa_cobertura = [
    ['#', '#', '#', '#', '#'],
    ['#', ' ', 'O', ' ', '#'],
    ['#', ' ', 'X', ' ', '#'],
    ['#', '#', '#', '#', '#']
]

mapa_terreo = [
    ['#', '#', '#', '#', '#'],
    ['#', 'O', 'X', ' ', '#'],
    ['#', '#', '#', '#', '#']
]

mapas_escadas = []
for i in range(11):
    mapa = [
        ['#', '#', '#', '#', '#', '#'],
        ['#', ' ', 'O', ' ', '#'],
        ['#', ' ', '#', ' ', '#'],
        ['#', ' ', 'X', ' ', '#'],
        ['#', '#', '#', '#', '#']
    ]
    mapas_escadas.append(mapa)

zonemap = {
    'escadarias': {
        'zonename': 'Escadarias',
        'descriptions': 'Descrições das escadarias',
        'examinations': 'Examinar as escadarias',
        'solved': False,
        'locked': True,  # Nova chave para indicar se as escadarias estão trancadas
        'up': ['frente', 'cima'],
        'down': ['baixo', 'trás'],
        'left': 'esquerda',
        'right': 'direita',
        'solved_places': {
            'a1': False, 'a2': False, 'a3': False, 'a4': False,
            'b1': False, 'b2': False, 'b3': False, 'b4': False,
            'c1': False, 'c2': False, 'c3': False, 'c4': False,
            'd1': False, 'd2': False, 'd3': False, 'd4': False
        }
    },
    'escritorio': {
        'zonename': 'Escritório',
        'descriptions': 'Descrições do escritório',
        'examinations': 'Examinar o escritório',
        'solved': False,
        'up': 'cima',
        'down': 'baixo',
        'left': 'esquerda',
        'right': 'direita',
        'solved_places': {
            'a1': False, 'a2': False, 'a3': False, 'a4': False, 'a5': False,
            'b1': False, 'b2': False, 'b3': False, 'b4': False, 'b5': False,
            'c1': False, 'c2': False, 'c3': False, 'c4': False, 'c5': False,
            'd1': False, 'd2': False, 'd3': False, 'd4': False, 'd5': False,
            'e1': False, 'e2': False, 'e3': False, 'e4': False, 'e5': False
        }
    },
    'cobertura': {
        'zonename': 'Cobertura',
        'descriptions': 'Descrições da cobertura',
        'examinations': 'Examinar a cobertura',
        'solved': False,
        'up': 'cima',
        'down': 'baixo',
        'left': 'esquerda',
        'right': 'direita',
        'solved_places': {
            'a1': False, 'a2': False, 'a3': False, 'a4': False,
            'b1': False, 'b2': False, 'b3': False, 'b4': False,
            'c1': False, 'c2': False, 'c3': False, 'c4': False
        }
    },
    'terreo': {
        'zonename': 'Térreo',
        'descriptions': 'Descrições do térreo',
        'examinations': 'Examinar o térreo',
        'solved': False,
        'up': 'cima',
        'down': 'baixo',
        'left': 'esquerda',
        'right': 'direita',
        'solved_places': {
            'a1': False, 'a2': False, 'a3': False,
            'b1': False, 'b2': False, 'b3': False
        }
    }
}

for i in range(11):
    zonename = f'escadas_{i+1}'
    zonemap[zonename] = {
        'zonename': f'Escadas {i+1}',
        'descriptions': f'Descrições das escadas {i+1}',
        'examinations': f'Examinar as escadas {i+1}',
        'solved': False,
        'up': ['frente', 'cima'],
        'down': ['baixo', 'trás'],
        'left': 'esquerda',
        'right': 'direita',
        'solved_places': {
            'a1': False, 'a2': False, 'a3': False, 'a4': False,
            'b1': False, 'b2': False, 'b3': False, 'b4': False,
            'c1': False, 'c2': False, 'c3': False, 'c4': False
        }
    }