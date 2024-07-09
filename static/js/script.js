

// Función para mostrar productos ordenados
function mostrarProductosOrdenados(orden) {
    // Ordenar el array de productos según el criterio seleccionado
    const productosOrdenados = productos.sort((a, b) => {
        if (orden === "nombre") {
            return a.nombre.localeCompare(b.nombre);
        } else if (orden === "precio-asc") {
            return a.precio - b.precio; // Ordenar por precio ascendente
        } else if (orden === "precio-desc") {
            return b.precio - a.precio; // Ordenar por precio descendente
        } else {
            return 0; // Ordenar por ID por defecto
        }
    });

    mostrarProductos(productosOrdenados);
}

// Función para mostrar productos
function mostrarProductos(productosMostrar) {
    tarjetas.innerHTML = ""; // Limpiar tarjetas existentes

    productosMostrar.forEach(producto => {
        const tarjeta = document.createElement("article");
        tarjeta.classList.add("producto");
        tarjeta.innerHTML = `
            <img src="producto-${producto.id}.jpg" alt="${producto.nombre}">
            <h3>${producto.nombre}</h3>
            <p>Descripción breve del perfume.</p>
            <span class="precio">$ ${producto.precio}</span>
            <button>Añadir al carrito</button>
        `;
        tarjetas.appendChild(tarjeta);
    });
}

// Evento para detectar el cambio de opción en el select
selectOrdenar.addEventListener("change", () => {
    const orden = selectOrdenar.value;
    mostrarProductosOrdenados(orden);
});

// Mostrar productos iniciales
mostrarProductosIniciales();

