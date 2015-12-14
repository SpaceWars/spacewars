Cenários
=========

Menu Inicial
~~~~~~~~~~~~~

-  Objetivo: Descrever menu inicial
-  Contexto: Usuário abre o jogo
-  Atores: Jogador
-  Recursos: -
-  Episódios:

   -  Jogador seleciona INICIAR FASE.
   -  Jogador seleciona CONFIGURAÇÕES.
   -  Jogador seleciona CRÉDITOS.
   -  Jogador seleciona sair do jogo.


Iniciar Fase
~~~~~~~~~~~~~

-  Objetivo: Descrever preparativos para inicio do jogo
-  Contexto: Menu Inicial
-  Atores: Jogador
-  Recursos: -
-  Episódios:

   -  Jogador seleciona a fase desejada.

      -  Restrição 1: Jogador precisa ter concluído pelo menos a
         primeira fase.

Dinâmica do Spacewars
~~~~~~~~~~~~~~~~~~~~~~

-  Objetivo: Descrever a dinâmica do jogo
-  Contexto: Iniciar Fase
-  Atores: Jogador
-  Recursos: Spaceship, Aliens, detritos espaciais, Pontuação, tiro
-  Episódios:

   -  Jogador se a MOVIMENTA SPACESHIP na tela.
   -  Jogador ATIRA.
   -  Se o jogador for atingido por um Alien ou algum detrito espacial,
      então o jogador PERDE O JOGO.
   -  Se o jogador chegar ao final da fase sem ser atingido por Aliens
      ou detritos, então o jogador AVANÇA DE NÍVEL.

Movimenta Spaceship
~~~~~~~~~~~~~~~~~~~~~~~~~

-  Objetivo: Descrever modo como a Spaceship se movimenta
-  Contexto: Dinâmica do SpaceWars
-  Atores: Jogador
-  Recursos: Spaceship
-  Episódios:

   -  Se o jogador aperta a tecla direcional para cima, então a
      Spaceship se move para frente.

      -  Restrição: Spaceship não pode ultrapassar a metade da tela.

   -  Se o jogador aperta a tecla direcional para baixo, então a
      Spaceship se move para trás.

      -  Restrição: O jogador não pode ultrapassar a base da tela.

   -  Se o jogador aperta a tecla direcional para direita, então a
      Spaceship se move para direita.

      -  Restrição: O jogador não pode ultrapassar o lado direito da
         tela.

   -  Se o jogador aperta a tecla direcional para esquerda, então a
      Spaceship se move para esquerda.

      -  Restrição: O jogador não pode ultrapassar o lado esquerdo da
         tela.

Atira
~~~~~~

-  Objetivo: Descrever comportamento do tiro
-  Contexto: Iniciar Fase
-  Atores: Jogador(Spaceship)
-  Recursos: Spaceship, Aliens, detritos espaciais, Pontuação, tiro
-  Episódios:

   -  Se o jogador pressionou a barra de espaço, então a Spaceship lança
      um tiro no espaço.
   -  Se o tiro acertar um Alien, então o Alien morre.
   -  Se o tiro acertar um detrito, então o detrito e destruído

Perde o Jogo
~~~~~~~~~~~~~

-  Objetivo: Descrever a tela de fim de jogo
-  Contexto: Iniciar Fase
-  Atores: Jogador
-  Recursos: Spaceship, Aliens, detritos espaciais, Pontuação
-  Episódios:

   -  Jogador escolhe em REINICIAR FASE.
   -  Jogador escolhe em sair do jogo.

Avança de Nível
~~~~~~~~~~~~~~~~~

-  Objetivo: Descrever como o usuário ganha o jogo
-  Contexto: Iniciar Fase
-  Atores: Jogador
-  Recursos: Spaceship, Aliens, detritos espaciais, Pontuação
-  Episódios:

   -  Se o jogador jogar durante o tempo da fase, sem ser atingido por
      nenhum Alien nem detritos, então o jogador avança de nível.

Créditos
~~~~~~~~~~

-  Objetivo: Descrever a tela de fim de jogo
-  Contexto: Iniciar Fase
-  Atores: Jogador
-  Recursos: Spaceship, Aliens, detritos espaciais, Pontuação
-  Episódios:

   -  Jogador visualiza informação dos responsáveis pelo jogo.
   -  Jogador escolhe em voltar ao MENU INICIAL.

Configurações
~~~~~~~~~~~~~~

-  Objetivo: Descrever a tela de opções de jogo
-  Contexto: Menu Inicial
-  Atores: Jogador
-  Recursos: -
-  Episódios:

   -  Jogador seleciona volume de som do jogo.
   -  Jogador seleciona volume de música do jogo.
   -  Jogador seleciona modo fullscreen.
   -  Jogador escolhe em voltar ao MENU INICIAL.

Fluxo de Cenários
------------------

.. image:: /img/fluxo.png
    :alt: Fluxo de Cenários
    :align: center
