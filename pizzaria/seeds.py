from pizza_app.models import PizzaModel

dados = [
    {
        "pizza": "Quatro Queijos",
        "preco": 69.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-pizza-sabor-quatro-queijos-tele-entrega-florianopolis-sao-jose.png",
        "ingredientes": "Mussarela, provolone, parmesão e gorgonzola.",
    },
    {
        "pizza": "Calabresa",
        "preco": 69.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-pizza-sabor-calabresa-pizza-em-casa-florianopolis-sao-jose.png",
        "ingredientes": "Mussarela, calabresa e cebola.",
    },
    {
        "pizza": "Mussarela",
        "preco": 69.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-pizza-sabor-mussarela-pizzaria-delivery-florianopolis-sao-jose.png",
        "ingredientes": "Mussarela e tomate.",
    },
    {
        "pizza": "Portuguesa",
        "preco": 69.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-pizza-sabor-portuguesa-delivery-floripa-parque-sao-jorge.png",
        "ingredientes": "Mussarela, cebola, presunto e ovos.",
    },
    {
        "pizza": "Frango",
        "preco": 69.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-pizza-sabor-frango-pizzaria-online-santa-monica-florianopolis.png",
        "ingredientes": "Mussarela, frango desfiado e requeijão catupiry",
    },
    {
        "pizza": "Frango e Creme",
        "preco": 69.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-pizza-sabor-frango-e-creme-pizza-tele-entrega-lagoa-da-conceicao-floripa.png",
        "ingredientes": "Mussarela, frango desfiado, tomate e creme de leite com milho.",
    },
    {
        "pizza": "Rúcula",
        "preco": 69.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-pizza-sabor-rucula-pizza-delivery-rio-tavares-florianopolis.png",
        "ingredientes": "Mussarela, rúcula, tomate seco e parmesão.",
    },
    {
        "pizza": "Brócolis",
        "preco": 69.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-pizza-sabor-brocolis-tele-pizza-campeche-floripa.png",
        "ingredientes": "Mussarela, brócolis levemente temperado no alho e requeijão.",
    },
    {
        "pizza": "Marguerita",
        "preco": 69.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-pizza-sabor-marguerita-pizza-entrega-carianos-floripa.png",
        "ingredientes": "Mussarela, manjericão fresco, parmesão e tomate.",
    },
    {
        "pizza": "Napolitana",
        "preco": 69.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-pizza-sabor-napolitana-delivery-florianopolis-corrego-grande.png",
        "ingredientes": "Mussarela, presunto, tomate e parmesão.",
    },
    {
        "pizza": "Áglio",
        "preco": 69.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-pizza-sabor-aglio-pizzaria-itacorubi.png",
        "ingredientes": "Mussarela, pamesão e alho especial.",
    },
    {
        "pizza": "Milho",
        "preco": 69.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-pizza-sabor-milho-delivery-joao-paulo.png",
        "ingredientes": "Mussarela, milho e requeijão catupiry.",
    },
    {
        "pizza": "Bacon",
        "preco": 69.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-pizza-sabor-bacon-pizza-em-casa-bosque-das-mansoes-sao-jose.png",
        "ingredientes": "Bacon em cubos, mussarela e requeijão.",
    },
    {
        "pizza": "Lombo e Creme",
        "preco": 69.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-pizza-sabor-lombo-e-creme-pizzaria-online-saco-dos-limoes.png",
        "ingredientes": "Mussarela, lombo, creme de leite e milho.",
    },
    {
        "pizza": "Lombo e Catupiry",
        "preco": 69.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-pizza-sabor-lombo-e-catupiry-pizza-tele-entrega-lagoa-da-conceicao-florianopolis.png",
        "ingredientes": "Mussarela, lombo e requeijão catupiry.",
    },
    {
        "pizza": "Ilha da Magia",
        "preco": 69.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-pizza-sabor-ilhadamagia-pizza-delivery-rio-tavares-florianopolis.png",
        "ingredientes": "Mussarela, presunto, ovo, pimentão e tomate.",
    },
    {
        "pizza": "Sambaqui",
        "preco": 69.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-pizza-sabor-sambaqui-pizza-delivery-rio-tavares-florianopolis.png",
        "ingredientes": "Mussarela, calabresa, milho e requeijão catupiry.",
    },
    {
        "pizza": "Luz das Estrelas",
        "preco": 69.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-pizza-sabor-luzdasestrelas-pizza-delivery-rio-tavares-florianopolis.png",
        "ingredientes": "Calabresa, ovo e pimentão cobertos com mussarela.",
    },
    {
        "pizza": "Beringela",
        "preco": 69.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-pizza-sabor-beringela-pizza-delivery-rio-tavares-florianopolis.png",
        "ingredientes": "Mussarela, beringela grelhada e requeijão.",
    },
    {
        "pizza": "Tropical",
        "preco": 69.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-pizza-sabor-tropical-pizza-delivery-rio-tavares-florianopolis.png",
        "ingredientes": "Mussarela, frango, bacon e requeijão catupiry.",
    },
    {
        "pizza": "Corn Bacon",
        "preco": 69.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-pizza-sabor-cornbacon-pizza-delivery-rio-tavares-florianopolis.png",
        "ingredientes": "Mussarela, bacon e milho.",
    },
    {
        "pizza": "Joaquina",
        "preco": 69.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-pizza-sabor-joaquina-pizza-delivery-rio-tavares-florianopolis.png",
        "ingredientes": "Mussarela, bacon, tomate e requeijão catupiry.",
    },
    {
        "pizza": "Daniela",
        "preco": 69.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-pizza-sabor-daniela.png",
        "ingredientes": "Mussarela, milho, tomate e folhas de majericão.",
    },
    {
        "pizza": "Toscana",
        "preco": 69.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-pizza-sabor-toscana-pizza-delivery-rio-tavares-florianopolis.png",
        "ingredientes": "Mussarela, calabresa, cebola e requeijão.",
    },
    {
        "pizza": "Namorados",
        "preco": 69.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-pizza-sabor-namorados-pizza-delivery-rio-tavares-florianopolis.png",
        "ingredientes": "Mussarela, lombo, tomate e parmesão.",
    },
    {
        "pizza": "Atum",
        "preco": 76.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-pizza-sabor-atum-pizza-em-casa-monte-verde.png",
        "ingredientes": "Mussarela, atum e cebola.",
    },
    {
        "pizza": "Zermatt",
        "preco": 76.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-pizza-sabor-zermatt-delivery-floripa-costeira.png",
        "ingredientes": "Presunto, bacon, palmito e requeijão cobertos com mussarela.",
    },
    {
        "pizza": "Pepperoni",
        "preco": 76.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-pizza-sabor-pepperoni-tele-pizza-pantanal.png",
        "ingredientes": "Mussarela e pepperoni.",
    },
    {
        "pizza": "Supreme",
        "preco": 76.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-pizza-sabor-supreme-pizza-entrega-agronomica.png",
        "ingredientes": "Mussarela, pepperoni, champignon, pimentão e cebola.",
    },
    {
        "pizza": "Catuperu",
        "preco": 76.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-pizza-sabor-catuperu-delivery-florianopolis-trindade.png",
        "ingredientes": "Mussarela, peito de peru defumado e catupiry.",
    },
    {
        "pizza": "Escarola",
        "preco": 76.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-pizza-sabor-escarola-pizzaria-forquilinha-sao-jose.png",
        "ingredientes": "Mussarela, escarola, bacon, alho e cebola.",
    },
    {
        "pizza": "Vegetariana",
        "preco": 76.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-pizza-sabor-vegetariana-delivery-picadas-do-sul.png",
        "ingredientes": "Mussarela, brócolis, cebola, tomate, tomate seco, palmito e parmesão.",
    },
    {
        "pizza": "Palmito",
        "preco": 76.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-pizza-sabor-palmito-pizza-tele-entrega-rocado-sao-jose.png",
        "ingredientes": "Mussarela, palmito e requeijão.",
    },
    {
        "pizza": "Itália",
        "preco": 76.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-pizza-sabor-italia-pizza-delivery-trindade-floripa.png",
        "ingredientes": "Presunto, mussarela, palmito, requeijão e champignon.",
    },
    {
        "pizza": "Levíssima",
        "preco": 76.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-pizza-sabor-levissima-pizzaria-online-campinas-sao-jose.png",
        "ingredientes": "Mussarela, peito de chester light defumado, creme de leite e tomate",
    },
    {
        "pizza": "Tacchino",
        "preco": 76.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-pizza-sabor-tacchino-delivery-floripa-kobrasol-sao-jose.png",
        "ingredientes": "Mussarela, peito de peru defumado, cobertos com catupiry e alho poró.",
    },
    {
        "pizza": "Camarão",
        "preco": 84.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-pizza-sabor-camarao-pizza-tele-entrega-jardim-atlantico-sao-jose.png",
        "ingredientes": "Mussarela, camarão e parmesão.",
    },
    {
        "pizza": "Filet Mignon",
        "preco": 84.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-pizza-sabor-filet-mignon-tele-pizza-capoeiras-florianopolis.png",
        "ingredientes": "Mussarela, filet mignon e requeijão catupiry.",
    },
    {
        "pizza": "Super Light",
        "preco": 84.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-pizza-sabor-super-light-pizza-entrega-bairro-de-fatima-floripa.png",
        "ingredientes": "Mussarela, mussarela de búfala, rúcula, tomate seco e parmesão.",
    },
    {
        "pizza": "Javali",
        "preco": 84.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-pizza-sabor-javali-delivery-florianopolis-balneareo.png",
        "ingredientes": "Mussarela, alho poró e linguiça de javali.",
    },
    {
        "pizza": "Nordestina",
        "preco": 84.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-pizza-sabor-nordestina-delivery-itaguacu-floripa.png",
        "ingredientes": "Mussarela, carne seca desfiada e cebola.",
    },
    {
        "pizza": "Zucchini in Brie",
        "preco": 84.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-pizza-sabor-zucchini-in-brie-delivery-floripa-prainha.png",
        "ingredientes": "Finíssimas fatias de abobrinha preparadas no azeite de oliva extra",
    },
    {
        "pizza": "Búfala",
        "preco": 84.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-pizza-sabor-bufala-pizzaria-online-beira-mar-floripa.png",
        "ingredientes": "Mussarela, mussarela de búfala com tomate cereja, folhas de",
    },
    {
        "pizza": "Strogonoff",
        "preco": 84.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-pizza-sabor-strogonoff-pizza-tele-entrega-parque-sao-jorge-florianopolis.png",
        "ingredientes": "Mussarela, strogonoff de filet mignon, champingon e batata palha.",
    },
    {
        "pizza": "Capricciosa",
        "preco": 84.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-pizza-sabor-capricciosa-pizza-delivery-santa-monica-floripa.png",
        "ingredientes": "Carne seca desfiada, musarela, tomate picado, cebola e pimentão",
    },
    {
        "pizza": "Chocolate Preto",
        "preco": 69.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-pizza-sabor-chocolate-preto-pizza-delivery-floresta-sao-jose.png",
        "ingredientes": "Pouca mussarela, creme de leite e chocolate preto.",
    },
    {
        "pizza": "Chocolate Branco",
        "preco": 69.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-pizza-sabor-chocolate-branco-tele-pizza-fazenda-do-max-sao-jose.png",
        "ingredientes": "Pouca mussarela, creme de leite e chocolate branco.",
    },
    {
        "pizza": "Banana",
        "preco": 69.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-pizza-sabor-banana-tele-pizza-agronomica-florianopolis.png",
        "ingredientes": "Banana com cobertura de chocolate e canela.",
    },
    {
        "pizza": "Califórnia",
        "preco": 69.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-pizza-sabor-california-pizza-entrega-praia-comprida-sao-jose.png",
        "ingredientes": "Mussarela, molho de tomate, figo, abacaxi, pêssego e uma pitada de",
    },
    {
        "pizza": "Sensação",
        "preco": 69.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-pizza-sabor-sensacao-delivery-florianopolis-ponta-de-baixo-sao-jose.png",
        "ingredientes": "Chocolate preto, morango e creme de leite.",
    },
    {
        "pizza": "Prestígio Zermatt",
        "preco": 69.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-pizza-sabor-prestigio-zermatt-pizzaria-centro-sao-jose.png",
        "ingredientes": "Chocolate preto, coco ralado, leite condensado e uva itália.",
    },
    {
        "pizza": "Coca-Cola 1,5L",
        "preco": 12.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-coca-cola-delivery-pizza-online-pizzaria-floripa.png",
        "ingredientes": "O refrigerante que é sucesso no mundo inteiro.",
    },
    {
        "pizza": "Coca-Cola Lata",
        "preco": 6.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-coca-cola-delivery-pizza-online-pizzaria-floripa.png",
        "ingredientes": "O refrigerante que é sucesso no mundo inteiro.",
    },
    {
        "pizza": "Coca-Cola Zero 1,5L",
        "preco": 12.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-coca-cola-zero-delivery-florianopolis.png",
        "ingredientes": "O refrigerante que é sucesso no mundo inteiro.",
    },
    {
        "pizza": "Coca-Cola Zero Lata",
        "preco": 6.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-coca-cola-zero-delivery-florianopolis.png",
        "ingredientes": "O refrigerante que é sucesso no mundo inteiro.",
    },
    {
        "pizza": "Fanta Laranja 2L",
        "preco": 12.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-fanta-laranja-delivery-florianopolis-pedir-em-casa.png",
        "ingredientes": "O tradicional sabor da laranja.",
    },
    {
        "pizza": "Fanta Laranja Lata",
        "preco": 6.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-fanta-laranja-delivery-florianopolis-pedir-em-casa.png",
        "ingredientes": "O tradicional sabor da laranja.",
    },
    {
        "pizza": "Guaraná Antárctica 2L",
        "preco": 12.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-guarana-delivery-tele-entrega-pizzaria-floripa.png",
        "ingredientes": "O tradicional refrigerante de guaraná.",
    },
    {
        "pizza": "Guaraná Antárctica Lata",
        "preco": 6.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-guarana-delivery-tele-entrega-pizzaria-floripa.png",
        "ingredientes": "O tradicional refrigerante de guaraná.",
    },
    {
        "pizza": "Guaraná Antárctica Zero 2L",
        "preco": 12.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-guarana-zero-tele-entrega-pizza-em-casa.png",
        "ingredientes": "O tradicional refrigerante de guaraná.",
    },
    {
        "pizza": "Guaraná Antárctica Zero Lata",
        "preco": 6.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-guarana-zero-tele-entrega-pizza-em-casa.png",
        "ingredientes": "O tradicional refrigerante de guaraná.",
    },
    {
        "pizza": "Sprite 2L",
        "preco": 12.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-sprite-pizza-delivery-sao-jose.png",
        "ingredientes": "o refrigerante que refresca.",
    },
    {
        "pizza": "Sprite Lata",
        "preco": 6.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-sprite-pizza-delivery-sao-jose.png",
        "ingredientes": "o refrigerante que refresca.",
    },
    {
        "pizza": "Schweppes 1,5L",
        "preco": 12.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-schwepps-cardapio-pizzaria-florianopolis.png",
        "ingredientes": "O refrigerante que acaba com a sua sede.",
    },
    {
        "pizza": "Água Mineral Sem Gás 500ml",
        "preco": 4.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-agua-mineral-pizza-em-casa-delivery-floripa.png",
        "ingredientes": "A água que mata sua sede.",
    },
    {
        "pizza": "Suco Del Valle Sabor Uva Lata",
        "preco": 7.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-suco-sabor-uva-del-valle-pizza-em-casa-delivery.png",
        "ingredientes": "Bom para todos os dias.",
    },
    {
        "pizza": "Suco Del Valle Sabor Pêssego Lata",
        "preco": 7.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-suco-del-valle-sabor-pessego-pizzaria-delivery-floripa-sao-jose.png",
        "ingredientes": "Bom para todos os dias.",
    },
    {
        "pizza": "Skol Lata",
        "preco": 6.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-skol-lata-pedir-pizza-em-casa.png",
        "ingredientes": "A cerveja que desce redondo.",
    },
    {
        "pizza": "Heineken Lata",
        "preco": 8.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-heineken-lata-pedido-online-pizza-floripa-continente.png",
        "ingredientes": "Uma ótima opção para quem entende de cerveja.",
    },
    {
        "pizza": "Vinho Cabernet Sauvignon Salton Garrafa",
        "preco": 58.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-vinho-cabernet-sauvignon-pizza-em-casa-floripa-sao-jose.png",
        "ingredientes": "Degustação perfeita com qualquer sabor.",
    },
    {
        "pizza": "Vinho Merlot Salton Garrafa",
        "preco": 58.00,
        "imagem": "https://zermattpizza.com.br/imgs/produto-vinho-merlot-pedido-pizza-ilha-continente.png",
        "ingredientes": "Degustação perfeita com qualquer sabor.",
    }
]

def seed():
    for produto in dados:
        PizzaModel.objects.create(pizza=produto["pizza"], preco=produto["preco"], imagem=produto["imagem"], ingredientes=produto["ingredientes"]) 

