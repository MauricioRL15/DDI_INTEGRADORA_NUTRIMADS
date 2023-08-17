from fastapi import APIRouter, HTTPException, Depends
from config.db import engine, conn
from models.nutrimads import usuario
from schemas.nutrimads import Usuario, EstatusEnum
from sqlalchemy.orm import Session
from config.db import get_db

router = APIRouter()


@router.get("/getAll")
def obtenerUsuarios():
    lista_tupla_usuarios = conn.execute(usuario.select()).fetchall()
    lista_diccionario_usuarios = []
    for tupla_usuario in lista_tupla_usuarios:
        diccionario_usuario = {
            "ID": tupla_usuario[0],
            "Nombre": tupla_usuario[1],
            "Genero": tupla_usuario[2],
            "Peso": tupla_usuario[3],
            "Talla": tupla_usuario[4],
            "Fecha_Nacimiento": tupla_usuario[5].strftime("%Y-%m-%d"),
            "Estatus": tupla_usuario[6],
            "Fecha_Registro": tupla_usuario[7].strftime("%Y-%m-%d %H:%M:%S"),
            "Fecha_Actualizacion": tupla_usuario[8].strftime("%Y-%m-%d %H:%M:%S")
            if tupla_usuario[8]
            else None,
        }
        lista_diccionario_usuarios.append(diccionario_usuario)
    return lista_diccionario_usuarios


@router.post("/insert")
def insertarUsuario(usuario_data: Usuario):
    conn.execute(usuario.insert().values(dict(usuario_data)))
    conn.commit()
    res = {"status": "Usuario insertado con éxito"}
    return res


@router.get("/getOne/{id_usuario}")
def obtenerUsuario(id_usuario):
    tupla_usuario = conn.execute(
        usuario.select().where(usuario.c.ID == id_usuario)
    ).first()
    if tupla_usuario:
        diccionario_usuario = {
            "ID": tupla_usuario[0],
            "Nombre": tupla_usuario[1],
            "Genero": tupla_usuario[2],
            "Peso": tupla_usuario[3],
            "Talla": tupla_usuario[4],
            "Fecha_Nacimiento": tupla_usuario[5].strftime("%Y-%m-%d"),
            "Estatus": tupla_usuario[6],
            "Fecha_Registro": tupla_usuario[7].strftime("%Y-%m-%d %H:%M:%S"),
            "Fecha_Actualizacion": tupla_usuario[8].strftime("%Y-%m-%d %H:%M:%S")
            if tupla_usuario[8]
            else None,
        }
        return diccionario_usuario
    else:
        res = {"status": "No existe ese usuario"}
        return res


@router.put("/update/{ID}")
def actualizarUsuario(usuarios: Usuario, ID):
    res = obtenerUsuario(ID)
    print(res)
    if res.get("status") == "No existe ese usuario":
        return res
    else:
        result = conn.execute(
            usuario.update().values(dict(usuarios)).where(usuario.c.ID == ID)
        ).last_updated_params()
        conn.commit()
    return result


@router.delete("/delete/{id_usuario}")
def eliminarUsuario(id_usuario):
    res = obtenerUsuario(id_usuario)
    if res.get("status") == "No existe ese usuario":
        return res
    else:
        conn.execute(usuario.delete().where(usuario.c.ID == id_usuario))
        conn.commit()
        res = {"status": "Usuario eliminado con éxito"}
        return res


@router.put("/update/{ID}")
def actualizarUsuario(ID: int, usuarios: Usuario, db: Session = Depends(get_db)):
    # Verificar si el usuario existe
    existing_user = db.execute(usuario.select().where(usuario.c.ID == ID)).first()
    if existing_user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    # Actualizar el usuario
    result = db.execute(
        usuario.update().values(dict(usuarios)).where(usuario.c.ID == ID)
    )

    if result.rowcount == 0:
        raise HTTPException(status_code=500, detail="Error al actualizar el usuario")

    db.commit()
    return {"status": "Usuario actualizado con éxito"}