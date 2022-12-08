import numpy.random as nprandom


def crearmatriz():
    sizeheight = 5
    sizewidth = 5
    maxnumber = 5
    matrizcreada = nprandom.randint(maxnumber, size=(sizeheight, sizewidth))
    return matrizcreada


def numerosconsecutivos(mat):
    """Para simplificar, se realiza todo en un solo bucle anidado for, al comparar 4 números al mismo tiempo
    no es necesario guardar y comparar varias veces"""
    for i in range(2):
        for j in range(5):
            conditionvert = mat[j][i] + 3 == mat[j][i + 1] + 2 == mat[j][i + 2] + 1 == mat[j][i + 3]
            if conditionvert:
                print(f"Existen números consecutivos en forma vertical desde:"
                      f"x={j} y={i}  hasta: x={j} y={i + 3}")
            conditionvertinversa = mat[j][i] == mat[j][i + 1] + 1 == mat[j][i + 2] + 2 == mat[j][i + 3] + 3
            if conditionvertinversa:
                print(f"Existen números consecutivos en forma vertical inversa desde: "
                      f"x={i} y={j + 3}  hasta: x={i} y={j}")
            conditionhorizontal = mat[i][j] + 3 == mat[i + 1][j] + 2 == mat[i + 2][j] + 1 == mat[i + 3][j]
            if conditionhorizontal:
                print(f"Existen números consecutivos en forma horizontal desde:"
                      f"x={i} y={j}  hasta: x={i + 3} y={j}")
            conditionhorinversa = mat[i][j] == mat[i + 1][j] + 1 == mat[i + 2][j] + 2 == mat[i + 3][j] + 3
            if conditionhorinversa:
                print(f"Existen números consecutivos en forma horizontal inversa desde:"
                      f"x={i + 3} y={j}  hasta: x={i} y={j}")


numerosconsecutivos(crearmatriz())
