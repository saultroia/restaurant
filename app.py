from modelos.restaurante import Restaurante

restaurante_chiaro = Restaurante('chiaro', 'Italiano')
restaurante_chiaro.receber_avaliacao('Pietro', 10)
restaurante_chiaro.receber_avaliacao('Yanka', 8)
restaurante_chiaro.receber_avaliacao('Lily', 5)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()