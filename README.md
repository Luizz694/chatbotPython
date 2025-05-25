# chatbotPython


No código estou usando uma biblioteca pra me auxiliar na criação ela se chama NLTK, peço o nome do usuário e logo depois dou as opções,
fiz apenas com coisas do meu dia dia, mas em caso de uso profissional poderíamos implementar por exemplo, um cardápio ou tipos de serviços
na implementação eu usei json's que são atribuidos por rotas diferentes, mas que dependendo da escolha do usuário (que no código está de 1 à 4)
vai para diferentes contextos no código, inclusive a variável tem o nome de contexto, usei um switch case ou em python "match", e implementei as rotas dos json's em uma variável chamada intents, logo depois essa variável vai para um for que está dentro de uma outra variável chamada combinações, nela tem as possíveis entradas e as sáidas dos json's, uma falha é que ainda está sem verificação
