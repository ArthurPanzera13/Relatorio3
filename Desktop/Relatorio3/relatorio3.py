# coding: utf-8

def compiler(file_path):
    dict_mnemonicos = {
        'An': '0',
        'nAoB': '1',
        'AnB': '2',
        'zeroL': '3',
        'nAeB': '4',
        'Bn': '5',
        'AxB': '6',
        'ABn': '7',
        'AnoB': '8',
        'nAxB': '9',
        'copiaB': 'A',
        'AB': 'B',
        'umL': 'C',
        'AoBn': 'D',
        'AoB': 'E',
        'copiaA': 'F'
    }

    x = y = w = None

    # Abrir arquivo input e criar output
    with open(file_path, 'r') as input_file:
        with open('testeula.hex', 'w') as output_file:

            # Loop pela leitura das instruções
            for input_line in input_file:
                # Tratar linha de entrada
                input_line = input_line.replace('\n', '')
                input_line = input_line.replace(';', '')

                if input_line != 'inicio:' and input_line != 'fim.':

                    if 'X' in input_line or 'Y' in input_line:
                        if 'X' in input_line:
                            input_line = input_line.replace('X=', '')
                            x = input_line
                        elif 'Y' in input_line:
                            input_line = input_line.replace('Y=', '')
                            y = input_line

                    elif 'W' in input_line:
                        w = dict_mnemonicos[input_line.replace('W=', '')]

                        output_file.write(f'{x}{y}{w}\n')
                        print(f'{x}{y}{w}\n')


if __name__ == '__main__':
    file_path = 'testeula.ula'
    compiler(file_path)