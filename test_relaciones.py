def test_eliminar_categoria_elimina_sus_productos(db_session):
    cat_ropa = CategoriaModel(nombre="Ropa")
    ProductoModel(nombre="Casaca", precio=120.0, categoria=cat_ropa)
    db_session.add(cat_ropa)
    db_session.commit()

    db_session.delete(cat_ropa)
    db_session.commit()

    prod_db = db_session.scalars(
        select(ProductoModel).filter_by(nombre="Casaca")
    ).first()
    assert prod_db is None