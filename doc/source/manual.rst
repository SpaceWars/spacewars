Manual do Usuário
=================

Requisitos
----------

-  AMD E-450, dual core 1,66Ghz
-  1GB DDR3
-  10MB (free space)

Instalando **SpaceWars** em seu computador
------------------------------------------

-  Baixe o `código
   fonte <https://github.com/SpaceWars/spacewars/archive/master.zip>`__.
-  Descompacte-o em seu lugar de preferencia.
-  É necessário que se possa executar arquivos no diretório, então evite
   lugares como um disco de partição FAT32/NTFS enquanto estiver usando
   sistemas Unix/Linux, assim como mídias moveis.
-  Instale as dependências:

   -  Python 2.7
   -  python-cocos2d (<=0.6.0)
   -  python-pyglet (<=1.2.4)
   -  python-six (<=1.9.0)

-  Para aqueles que possuem o *pip* instalado em seus computadores,
   podem instalar as depêndencias executando o seguinte comando na raiz
   do jogo:

::

  pip install -r requeriments

Executando **SpaceWars** em seu computador
------------------------------------------

Com as dependências instaladas, basta executar o arquivo **SpaceWars**
localizado na raiz do diretório onde o jogo foi descompactado. Para
àqueles que desejam que o jogo possa ser executado a partir de um
laucher ou de qualquer diretório a partir de um terminal, basta gerar um
link simbolico do executavel para a pasta */usb/bin* ou para a *~/bin*.
Tendo o endereço completo do executavel como
\*\*~/Downloads/SpaceWars/SpaceWars\* por exemplo, o seguinte comando
irá criar o desejavel link simbolico:

::

  ln -s ~/Downloads/SpaceWars/SpaceWars /usr/bin/SpaceWars

Desinstalando **SpaceWars** em seu computador
---------------------------------------------

**SpaceWars** não gera nenhum arquivo fora do seu diretório. Basta
remover a pasta pa se ver livre do jogo. Caso tenha criado um link
simbolico em */usb/bin*, será necessario remove-lo manualmente também.

Game Controls
=============

Teclado
-------

-  ← ↑ → ↓

   -  Controle da nave e navegação em menus.

-  Barra de Espaço

   -  Atira

-  Enter

   -  Confirmação de ação nos menus.

-  Esc

   -  Retorno de telas na navegação de menus ou abertura de menu durante
      o jogo.

Joystick
--------

-  Direcionais/Analogicos

   -  Controle da nave e navegação em menus.

-  Botões

   -  Atira
   -  Confirmação de ação nos menus.

-  Start

   -  Abertura de menu durante o jogo.

Game Interface
==============

.. image:: /img/game_cene.png
    :alt: Conceito - Fase
    :align: center


1. Você
2. Alguns *Rohinianos*
3. Aerólitos (Cuidado!)
4. Seu tiro

