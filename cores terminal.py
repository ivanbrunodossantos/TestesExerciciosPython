#como utilizar os códigos de escape sequence ANSI para configurar cores para os seus programas em Python. /
#Veja como utilizar o código \033[m com todas as suas principais possibilidades.

#     Style                                                        text         background

#     sem tipo.                              0             30      black        preto        40
#     (antigo) Negrito                       1             31      red          vermelho     41
#     (Sublinhado) Sublinhado                4             32      green        verde        42
#     (Negativo) Inverte letra e fundo       7             33      yellow       amarelo      43
#                                                          34      blue         azul         44
#                                                          35      Magenta      Magenta      45
#                                                          36      cyan         ciano        46
#                                                          37      grey         cinza        47
#                                                          97      white        branco       107
# exemplo:
print('\033[0;30;47mOlá mundo!\033[m')
