let contenedorProductosLanzamiento = $("#contenedor-productos-lanzamiento");

mostrarProductosLanzamiento(productosLanzamiento);

function mostrarProductosLanzamiento(productosLanzamiento) {
  contenedorProductosLanzamiento.html("");

  for (const producto of productosLanzamiento) {
    contenedorProductosLanzamiento.append(`
            <div class="card-productos">
                <div>
                    <img class="producto-img" src=${producto.img} alt="producto-${producto.nombre}">
                    <p class="producto-marca">${producto.marca}</p>
                    <p class="producto-nombre">${producto.nombre}</p>
                </div>
            </div>
            `);
  }
}

let contenedorProductos = $("#contenedor-productos");

mostrarproductos(productos);

function mostrarproductos(productos) {
  contenedorProductos.html("");

  for (const producto of productos) {
    contenedorProductos.append(`
            <div class="card-productos">
                <div>
                    <img class="producto-img" src=${producto.img} alt="producto-${producto.nombre}">
                    <p class="producto-marca">${producto.marca}</p>
                    <p class="producto-nombre">${producto.nombre}</p>
                    <p class="producto-precio">$ ${producto.precio}</p>
                </div>
            </div>
            `);
  }
}
